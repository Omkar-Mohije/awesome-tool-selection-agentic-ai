#!/usr/bin/env python3
"""Generate labeled prospective P07 figures without third-party packages.

Writes new prospective PDF and PNG files; existing development figures are untouched.
"""
from __future__ import annotations

import argparse
import struct
import zlib
from pathlib import Path

WIDTH_PT, HEIGHT_PT = 460.8, 237.6
DPI_SCALE = 2.5
WIDTH_PX, HEIGHT_PX = round(WIDTH_PT * DPI_SCALE), round(HEIGHT_PT * DPI_SCALE)
SUCCESS = (35, 119, 102)
FAILURE = (179, 78, 78)
BLUE = (61, 101, 140)
DARK = (38, 48, 58)
GRID = (220, 225, 230)
WHITE = (255, 255, 255)
FONT = {
    "A": ("01110","10001","10001","11111","10001","10001","10001"),
    "B": ("11110","10001","10001","11110","10001","10001","11110"),
    "C": ("01111","10000","10000","10000","10000","10000","01111"),
    "D": ("11110","10001","10001","10001","10001","10001","11110"),
    "E": ("11111","10000","10000","11110","10000","10000","11111"),
    "F": ("11111","10000","10000","11110","10000","10000","10000"),
    "G": ("01111","10000","10000","10111","10001","10001","01111"),
    "H": ("10001","10001","10001","11111","10001","10001","10001"),
    "I": ("11111","00100","00100","00100","00100","00100","11111"),
    "J": ("00111","00010","00010","00010","10010","10010","01100"),
    "K": ("10001","10010","10100","11000","10100","10010","10001"),
    "L": ("10000","10000","10000","10000","10000","10000","11111"),
    "M": ("10001","11011","10101","10101","10001","10001","10001"),
    "N": ("10001","11001","10101","10011","10001","10001","10001"),
    "O": ("01110","10001","10001","10001","10001","10001","01110"),
    "P": ("11110","10001","10001","11110","10000","10000","10000"),
    "Q": ("01110","10001","10001","10001","10101","10010","01101"),
    "R": ("11110","10001","10001","11110","10100","10010","10001"),
    "S": ("01111","10000","10000","01110","00001","00001","11110"),
    "T": ("11111","00100","00100","00100","00100","00100","00100"),
    "U": ("10001","10001","10001","10001","10001","10001","01110"),
    "V": ("10001","10001","10001","10001","10001","01010","00100"),
    "W": ("10001","10001","10001","10101","10101","10101","01010"),
    "X": ("10001","10001","01010","00100","01010","10001","10001"),
    "Y": ("10001","10001","01010","00100","00100","00100","00100"),
    "Z": ("11111","00001","00010","00100","01000","10000","11111"),
    "0": ("01110","10001","10011","10101","11001","10001","01110"),
    "1": ("00100","01100","00100","00100","00100","00100","01110"),
    "2": ("01110","10001","00001","00010","00100","01000","11111"),
    "3": ("11110","00001","00001","01110","00001","00001","11110"),
    "4": ("00010","00110","01010","10010","11111","00010","00010"),
    "5": ("11111","10000","10000","11110","00001","00001","11110"),
    "6": ("01110","10000","10000","11110","10001","10001","01110"),
    "7": ("11111","00001","00010","00100","01000","01000","01000"),
    "8": ("01110","10001","10001","01110","10001","10001","01110"),
    "9": ("01110","10001","10001","01111","00001","00001","01110"),
    "-": ("00000","00000","00000","11111","00000","00000","00000"),
    "/": ("00001","00010","00010","00100","01000","01000","10000"),
    ":": ("00000","00100","00100","00000","00100","00100","00000"),
    ".": ("00000","00000","00000","00000","00000","00110","00110"),
    "%": ("11001","11010","00100","01000","10110","00110","00000"),
    "(": ("00010","00100","01000","01000","01000","00100","00010"),
    ")": ("01000","00100","00010","00010","00010","00100","01000"),
    "_": ("00000","00000","00000","00000","00000","00000","11111"),
    " ": ("00000",)*7,
}

def rgb_pdf(color):
    return " ".join(f"{channel / 255:.4f}" for channel in color)

def escape_pdf(text):
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

def pdf_page(title, plot_commands):
    stream = ("q\n" + "\n".join(plot_commands) + "\nQ\n").encode("ascii")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {WIDTH_PT} {HEIGHT_PT}] "
        "/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>".encode("ascii"),
        b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"endstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    data = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, obj in enumerate(objects, 1):
        offsets.append(len(data))
        data.extend(f"{index} 0 obj\n".encode("ascii"))
        data.extend(obj)
        data.extend(b"\nendobj\n")
    xref_offset = len(data)
    data.extend(f"xref\n0 {len(offsets)}\n".encode("ascii"))
    data.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        data.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    data.extend(f"trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("ascii"))
    return bytes(data)

class Raster:
    def __init__(self):
        self.data = bytearray(WHITE * (WIDTH_PX * HEIGHT_PX))

    def rect(self, x, y, width, height, color):
        x0, y0 = max(0, int(x)), max(0, int(y))
        x1, y1 = min(WIDTH_PX, int(x + width)), min(HEIGHT_PX, int(y + height))
        row = bytes(color)
        for py in range(y0, y1):
            start = (py * WIDTH_PX + x0) * 3
            self.data[start:(py * WIDTH_PX + x1) * 3] = row * max(0, x1 - x0)

    def line(self, x0, y0, x1, y1, color, thickness=1):
        x0,y0,x1,y1 = map(int,(x0,y0,x1,y1))
        dx,dy=abs(x1-x0),abs(y1-y0)
        sx,sy=(1 if x0<x1 else -1),(1 if y0<y1 else -1)
        err=dx-dy
        while True:
            self.rect(x0-thickness//2,y0-thickness//2,thickness,thickness,color)
            if x0==x1 and y0==y1: break
            e2=2*err
            if e2>-dy: err-=dy; x0+=sx
            if e2<dx: err+=dx; y0+=sy

    def text(self, x, y, text, color, scale=2, align="left"):
        text=text.upper()
        char_w=6*scale
        width=max(0,len(text)*char_w-scale)
        if align=="center": x-=width/2
        elif align=="right": x-=width
        x=int(x); y=int(y)
        for char in text:
            glyph=FONT.get(char,FONT[" "])
            for row,bits in enumerate(glyph):
                for col,bit in enumerate(bits):
                    if bit=="1": self.rect(x+col*scale,y+row*scale,scale,scale,color)
            x+=char_w

    def png(self, path):
        raw=bytearray()
        stride=WIDTH_PX*3
        for y in range(HEIGHT_PX):
            raw.append(0)
            raw.extend(self.data[y*stride:(y+1)*stride])
        compressed=zlib.compress(bytes(raw),9)
        png=bytearray(b"\x89PNG\r\n\x1a\n")
        def chunk(name, payload):
            png.extend(struct.pack(">I",len(payload))+name+payload+struct.pack(">I",zlib.crc32(name+payload)&0xffffffff))
        chunk(b"IHDR",struct.pack(">IIBBBBB",WIDTH_PX,HEIGHT_PX,8,2,0,0,0))
        chunk(b"IDAT",compressed)
        chunk(b"IEND",b"")
        Path(path).write_bytes(png)

def text_cmd(x,y,text,size=8,color=DARK,align="center"):
    estimated=len(text)*size*0.56
    if align=="center": x-=estimated/2
    elif align=="right": x-=estimated
    return f"BT /F1 {size} Tf {rgb_pdf(color)} rg 1 0 0 1 {x:.2f} {y:.2f} Tm ({escape_pdf(text)}) Tj ET"

def rect_cmd(x,y,w,h,color):
    return f"{rgb_pdf(color)} rg {x:.2f} {y:.2f} {w:.2f} {h:.2f} re f"

def line_cmd(x1,y1,x2,y2,color=GRID,width=0.6):
    return f"{rgb_pdf(color)} RG {width:.2f} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S"

def render_task_figure(pdf_path,png_path):
    cmds=[]
    cmds.append(text_cmd(WIDTH_PT/2,218,"COMPLETE-TASK OUTCOMES (N=6 PER CONDITION)",11,DARK))
    left,bottom,plot_w,plot_h=72,62,350,128
    for tick in (0,2,4,6):
        y=bottom+plot_h*tick/6
        cmds.extend((line_cmd(left,y,left+plot_w,y,GRID,0.5),text_cmd(left-10,y-2,str(tick),8,DARK,"right")))
    cmds.extend((line_cmd(left,bottom,left+plot_w,bottom,DARK,0.9),line_cmd(left,bottom,left,bottom+plot_h,DARK,0.9)))
    conditions=[("VANILLA",0),("GENERIC CONTROL",1),("SCHEMA EVIDENCE",0)]
    centers=[left+plot_w*.19,left+plot_w*.50,left+plot_w*.81]
    bar_w=62
    for (label,success),cx in zip(conditions,centers):
        fail=6-success
        good_h=plot_h*success/6
        bad_h=plot_h*fail/6
        if success: cmds.append(rect_cmd(cx-bar_w/2,bottom,bar_w,good_h,SUCCESS))
        if fail: cmds.append(rect_cmd(cx-bar_w/2,bottom+good_h,bar_w,bad_h,FAILURE))
        cmds.append(text_cmd(cx,bottom+plot_h+8,f"{success}/6",8,DARK))
        cmds.append(text_cmd(cx,bottom-14,label,7,DARK))
    cmds.extend((rect_cmd(158,12,10,8,SUCCESS),text_cmd(173,13,"SUCCESS",7,DARK,"left"),
                 rect_cmd(250,12,10,8,FAILURE),text_cmd(265,13,"FAILED",7,DARK,"left")))
    Path(pdf_path).write_bytes(pdf_page("task outcomes",cmds))

    img=Raster()
    s=DPI_SCALE
    def X(v): return v*s
    def Y(v): return HEIGHT_PX-v*s
    def r(x,y,w,h,c): img.rect(X(x),Y(y+h),X(w),X(h),c)
    def ln(x1,y1,x2,y2,c=GRID,t=1): img.line(X(x1),Y(y1),X(x2),Y(y2),c,max(1,round(t*s)))
    def tx(x,y,text,c=DARK,fs=8,align="center"):
        scale=max(1,round(fs*s/9))
        yy=Y(y)-round(7*scale*0.85)
        img.text(X(x),yy,text,c,scale,align)
    tx(WIDTH_PT/2,218,"COMPLETE-TASK OUTCOMES (N=6 PER CONDITION)",DARK,11)
    for tick in (0,2,4,6):
        yy=bottom+plot_h*tick/6
        ln(left,yy,left+plot_w,yy,GRID,.5)
        tx(left-10,yy-2,str(tick),DARK,8,"right")
    ln(left,bottom,left+plot_w,bottom,DARK,.9);ln(left,bottom,left,bottom+plot_h,DARK,.9)
    for (label,success),cx in zip(conditions,centers):
        good_h=plot_h*success/6;bad_h=plot_h*(6-success)/6
        if success:r(cx-bar_w/2,bottom,bar_w,good_h,SUCCESS)
        if 6-success:r(cx-bar_w/2,bottom+good_h,bar_w,bad_h,FAILURE)
        tx(cx,bottom+plot_h+8,f"{success}/6",DARK,8)
        tx(cx,bottom-14,label,DARK,7)
    r(158,12,10,8,SUCCESS);tx(173,13,"SUCCESS",DARK,7,"left")
    r(250,12,10,8,FAILURE);tx(265,13,"FAILED",DARK,7,"left")
    img.png(png_path)

def render_failure_figure(pdf_path,png_path):
    cmds=[]
    cmds.append(text_cmd(WIDTH_PT/2,218,"FIRST REPORTED TASK FAILURES",11,DARK))
    left,bottom,plot_w=90,75,320
    max_count=18
    for tick in (0,5,10,15,18):
        x=left+plot_w*tick/max_count
        cmds.extend((line_cmd(x,bottom,x,bottom+75,GRID,.5),text_cmd(x,bottom-13,str(tick),8,DARK)))
    cmds.extend((line_cmd(left,bottom,left+plot_w,bottom,DARK,.9),line_cmd(left,bottom,left,bottom+75,DARK,.9)))
    cmds.append(text_cmd(left,165,"INSTANCE-STATE MISMATCH",8,DARK,"left"))
    bw=plot_w*17/max_count
    cmds.append(rect_cmd(left,bottom+18,bw,28,BLUE))
    cmds.append(text_cmd(left+bw+13,bottom+30,"17 / 18",9,DARK,"left"))
    cmds.append(text_cmd(WIDTH_PT/2,25,"FAILED CONDITION/TASK RECORDS",8,DARK))
    Path(pdf_path).write_bytes(pdf_page("failure types",cmds))

    img=Raster();s=DPI_SCALE
    def X(v): return v*s
    def Y(v): return HEIGHT_PX-v*s
    def ln(x1,y1,x2,y2,c=GRID,t=1):img.line(X(x1),Y(y1),X(x2),Y(y2),c,max(1,round(t*s)))
    def r(x,y,w,h,c):img.rect(X(x),Y(y+h),X(w),X(h),c)
    def tx(x,y,text,c=DARK,fs=8,align="center"):
        scale=max(1,round(fs*s/9));img.text(X(x),Y(y)-round(7*scale*.85),text,c,scale,align)
    tx(WIDTH_PT/2,218,"FIRST REPORTED TASK FAILURES",DARK,11)
    for tick in (0,5,10,15,18):
        x=left+plot_w*tick/max_count
        ln(x,bottom,x,bottom+75,GRID,.5);tx(x,bottom-13,str(tick),DARK,8)
    ln(left,bottom,left+plot_w,bottom,DARK,.9);ln(left,bottom,left,bottom+75,DARK,.9)
    tx(left,165,"INSTANCE-STATE MISMATCH",DARK,8,"left")
    r(left,bottom+18,bw,28,BLUE);tx(left+bw+13,bottom+30,"17 / 18",DARK,9,"left")
    tx(WIDTH_PT/2,25,"FAILED CONDITION/TASK RECORDS",DARK,8)
    img.png(png_path)

def generate(root):
    root=Path(root)
    outdirs=[root/"paper"/"figures",root/"results"/"prospective"/"ATR-P07-v1-20261117"]
    for out in outdirs:
        out.mkdir(parents=True,exist_ok=True)
        render_task_figure(out/"prospective_task_outcomes.pdf",out/"prospective_task_outcomes.png")
        render_failure_figure(out/"prospective_failure_types.pdf",out/"prospective_failure_types.png")

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",default=".",help="Repository root (default: current directory)")
    args=p.parse_args()
    generate(args.root)


