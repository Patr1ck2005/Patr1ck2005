"""Build a captioned, 180-second tour from explicitly attributed public assets.

Input JSON is a list of {path, title, zh, en, seconds, source_url, kind}.
Local input paths are omitted from the published manifest. No source data is read.
Requires Pillow, PyAV and PyMuPDF; no network requests are made.
"""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path
import textwrap

import av
import fitz
from PIL import Image, ImageDraw, ImageFont


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--inputs',type=Path,required=True)
    parser.add_argument('--out',type=Path,default=Path('docs/demo'))
    parser.add_argument('--font',type=Path,required=True,help='Font supporting Latin and simplified Chinese')
    args=parser.parse_args()
    inputs=json.loads(args.inputs.read_text(encoding='utf-8'))
    assert sum(item['seconds'] for item in inputs)==180
    args.out.mkdir(parents=True,exist_ok=True)
    fonts={size:ImageFont.truetype(str(args.font),size) for size in (18,22,26,38)}
    records=[]
    frames=[]
    for i,item in enumerate(inputs):
        source=Path(item['path'])
        assert item['source_url'].startswith('https://github.com/Patr1ck2005/')
        if source.suffix.lower()=='.svg':
            document=fitz.open(stream=source.read_bytes(),filetype='svg')
            pix=document[0].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False)
            picture=Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')
        else:
            picture=Image.open(source).convert('RGB')
        frame=Image.new('RGB',(1280,960),'#101b2b')
        draw=ImageDraw.Draw(frame)
        draw.text((48,28),f'{i+1:02d} / {len(inputs):02d}   RESEARCH TOOLS',font=fonts[18],fill='#8bded2')
        draw.text((48,65),item['title'],font=fonts[38],fill='white')
        draw.text((48,124),item['kind'],font=fonts[18],fill='#bed0e5')
        # Contain the complete image; preserve axes, legends and original ratio.
        picture.thumbnail((1176,570),Image.Resampling.LANCZOS)
        draw.rounded_rectangle((40,166,1240,750),radius=8,fill='white')
        frame.paste(picture,((1280-picture.width)//2,173+(570-picture.height)//2))
        draw.text((48,780),item['zh'],font=fonts[26],fill='white')
        for row,line in enumerate(textwrap.wrap(item['en'],95)):
            draw.text((48,824+row*30),line,font=fonts[22],fill='#d4e0ee')
        draw.text((48,916),'Patr1ck2005  /  github.com/Patr1ck2005  /  my1ab.fyi',font=fonts[18],fill='#9db4ce')
        preview=args.out/f'chapter-{i+1:02d}.png'
        frame.save(preview)
        frames.append(frame)
        records.append({key:value for key,value in item.items() if key!='path'}|{
            'source_filename':source.name,'source_sha256':sha(source),
            'preview':preview.name,'preview_sha256':sha(preview)})
    output=args.out/'research-tools-tour.mp4'
    with av.open(str(output),'w') as container:
        stream=container.add_stream('libx264',rate=12)
        stream.width=1280;stream.height=960;stream.pix_fmt='yuv420p'
        stream.options={'crf':'24','preset':'veryfast'}
        index=0
        for frame,item in zip(frames,inputs):
            for _ in range(item['seconds']*12):
                current=frame.copy();draw=ImageDraw.Draw(current)
                draw.rectangle((0,954,round(1280*(index+1)/2160),959),fill='#8bded2')
                video=av.VideoFrame.from_image(current);video.pts=index
                for packet in stream.encode(video):container.mux(packet)
                index+=1
            print(json.dumps({'chapter':item['title'],'frames_written':index}),flush=True)
        for packet in stream.encode():container.mux(packet)
    with av.open(str(output)) as check:
        video=check.streams.video[0]
        assert video.frames==2160
        assert abs(float(video.duration*video.time_base)-180)<0.1
    manifest={'duration_seconds':180,'frames':2160,'fps':12,'format':'Silent captioned walkthrough; images are real computed outputs or attributed public software frames.',
              'video':output.name,'video_sha256':sha(output),'generator':'../../scripts/build_tour.py','generator_sha256':sha(Path(__file__)),
              'chapters':records,'versions':{'PyAV':av.__version__}}
    (args.out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (args.out/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Research tools / 科研工具</title><style>body{margin:24px auto;max-width:1100px;background:#101b2b;color:#eaf2ff;font:18px/1.6 system-ui;padding:0 18px}video{width:100%;height:auto}a{color:#8bded2}</style><h1>Research tools / 科研工具</h1><p>Three-minute captioned tour · 三分钟字幕导览。Computed synthetic outputs and attributed public software frames.</p><video controls preload="metadata" poster="chapter-01.png" src="research-tools-tour.mp4"></video><p><a href="manifest.json">Sources and hashes / 来源与校验</a> · <a href="../../README.md">Project directory / 项目目录</a></p></html>''',encoding='utf-8')
    print(json.dumps({'video':str(output),'seconds':180,'frames':2160,'sha256':sha(output)}))


if __name__=='__main__':main()
