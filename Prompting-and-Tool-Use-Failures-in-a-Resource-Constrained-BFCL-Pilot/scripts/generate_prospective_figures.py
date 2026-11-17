"""Generate standalone prospective figures matching the repository's visual style.
Produces both vector PDF and PNG files using pure Python standard library.
"""
import struct
import zlib
from pathlib import Path

def generate_task_outcomes(pdf_path, png_path):
    # Data: vanilla: 0/6, generic_control: 1/6, schema_evidence: 0/6
    # Total: 6 for each.
    # Dimensions: 6.4 x 3.3 inches -> 1152 x 594 px at 180 DPI (460.8 x 237.6 pt for PDF)
    W_PT, H_PT = 460.8, 237.6
    W_PX, H_PX = 1152, 594
    
    # 1. Generate Vector PDF
    # Colors: Success #237766 (0.137, 0.467, 0.400), Failure #b34e4e (0.702, 0.306, 0.306)
    # Background #ffffff
    # Chart area: x: 70 to 420, y: 55 to 195 (width 350, height 140)
    pdf_stream = []
    pdf_stream.append("q")
    pdf_stream.append("1 1 1 rg 0 0 460.8 237.6 re f") # background
    
    # Title
    pdf_stream.append("BT /F1 11 Tf 0 0 0 rg 90 215 Td (Official complete-task outcomes (prospective evaluation)) Tj ET")
    # Y-axis label
    pdf_stream.append("BT /F1 9 Tf 0 0 0 rg 15 110 Td (Task records) Tj ET")
    
    # Axes lines (bottom and left only, spines top/right False)
    pdf_stream.append("0.2 0.2 0.2 RG 0.8 w")
    pdf_stream.append("70 55 m 420 55 l S") # X axis
    pdf_stream.append("70 55 m 70 200 l S") # Y axis
    
    # Y ticks and grid
    for y_val in range(0, 7, 2):
        y_pt = 55 + (y_val / 6.0) * 140
        pdf_stream.append(f"65 {y_pt:.1f} m 70 {y_pt:.1f} l S")
        pdf_stream.append(f"BT /F1 8 Tf 0.2 0.2 0.2 rg 55 {y_pt-3:.1f} Td ({y_val}) Tj ET")
    
    # Bars: 3 bars at x = 110, 230, 350 (bar width = 60)
    bar_data = [
        ("vanilla", 0, 6, "0/6 success"),
        ("generic\ncontrol", 1, 5, "1/6 success"),
        ("schema\nevidence", 0, 6, "0/6 success")
    ]
    
    bar_w = 60
    centers = [125, 245, 365]
    for idx, (label, succ, fail, txt) in enumerate(bar_data):
        cx = centers[idx]
        bx = cx - bar_w / 2.0
        
        # Bottom bar: success (if > 0)
        succ_h = (succ / 6.0) * 140
        fail_h = (fail / 6.0) * 140
        
        if succ > 0:
            pdf_stream.append(f"0.137 0.467 0.400 rg {bx:.1f} 55 {bar_w} {succ_h:.1f} re f")
        if fail > 0:
            pdf_stream.append(f"0.702 0.306 0.306 rg {bx:.1f} {55+succ_h:.1f} {bar_w} {fail_h:.1f} re f")
            
        # Text label inside bar
        txt_y = 55 + 70 # middle of bar (total/2)
        pdf_stream.append(f"BT /F1 9 Tf 1 1 1 rg {cx-24:.1f} {txt_y-4:.1f} Td ({txt}) Tj ET")
        
        # X-axis label
        if "\n" in label:
            l1, l2 = label.split("\n")
            pdf_stream.append(f"BT /F1 8.5 Tf 0 0 0 rg {cx-15:.1f} 42 Td ({l1}) Tj ET")
            pdf_stream.append(f"BT /F1 8.5 Tf 0 0 0 rg {cx-16:.1f} 32 Td ({l2}) Tj ET")
        else:
            pdf_stream.append(f"BT /F1 8.5 Tf 0 0 0 rg {cx-15:.1f} 40 Td ({label}) Tj ET")

    # Legend at bottom
    pdf_stream.append("0.137 0.467 0.400 rg 160 12 12 8 re f")
    pdf_stream.append("BT /F1 8 Tf 0 0 0 rg 176 13 Td (Task success) Tj ET")
    pdf_stream.append("0.702 0.306 0.306 rg 255 12 12 8 re f")
    pdf_stream.append("BT /F1 8 Tf 0 0 0 rg 271 13 Td (Task failure) Tj ET")
    
    pdf_stream.append("Q")
    stream_bytes = "\n".join(pdf_stream).encode("latin1")
    
    pdf_doc = f"""%PDF-1.4
1 0 obj <</Type /Catalog /Pages 2 0 R>> endobj
2 0 obj <</Type /Pages /Kids [3 0 R] /Count 1>> endobj
3 0 obj <</Type /Page /Parent 2 0 R /MediaBox [0 0 {W_PT} {H_PT}] /Resources <</Font <</F1 5 0 R>>>> /Contents 4 0 R>> endobj
4 0 obj <</Length {len(stream_bytes)}>> stream
{stream_bytes.decode('latin1')}
endstream endobj
5 0 obj <</Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold>> endobj
xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000244 00000 n 
0000000346 00000 n 
trailer <</Size 6 /Root 1 0 R>>
startxref
420
%%EOF
"""
    pdf_path.write_bytes(pdf_doc.encode("latin1"))

    # 2. Generate PNG raster
    # Render into 1152 x 594 RGB buffer
    img = bytearray([255] * (W_PX * H_PX * 3))
    def fill_rect(x1, y1, w, h, r, g, b):
        for y in range(max(0, y1), min(H_PX, y1 + h)):
            row_start = y * W_PX * 3
            for x in range(max(0, x1), min(W_PX, x1 + w)):
                idx = row_start + x * 3
                img[idx] = r; img[idx+1] = g; img[idx+2] = b

    # Chart scale: 180 / 72 = 2.5
    scale = 2.5
    # Axes
    fill_rect(int(70 * scale), H_PX - int(200 * scale), int(1.5 * scale), int(145 * scale), 50, 50, 50) # Y
    fill_rect(int(70 * scale), H_PX - int(55 * scale), int(350 * scale), int(1.5 * scale), 50, 50, 50) # X
    
    # Draw bars
    for idx, (label, succ, fail, txt) in enumerate(bar_data):
        cx = int(centers[idx] * scale)
        bw = int(bar_w * scale)
        bx = cx - bw // 2
        sh = int((succ / 6.0) * 140 * scale)
        fh = int((fail / 6.0) * 140 * scale)
        
        # Success bar
        if succ > 0:
            fill_rect(bx, H_PX - int(55 * scale) - sh, bw, sh, 35, 119, 102)
        # Failure bar
        if fail > 0:
            fill_rect(bx, H_PX - int(55 * scale) - sh - fh, bw, fh, 179, 78, 78)

    # Encode PNG
    raw = bytearray()
    for y in range(H_PX):
        raw.append(0)
        raw.extend(img[y * W_PX * 3 : (y + 1) * W_PX * 3])
    compressed = zlib.compress(bytes(raw), 6)
    
    png = bytearray(b'\x89PNG\r\n\x1a\n')
    ihdr = struct.pack('>IIBBBBB', W_PX, H_PX, 8, 2, 0, 0, 0)
    png.extend(struct.pack('>I', len(ihdr)) + b'IHDR' + ihdr + struct.pack('>I', zlib.crc32(b'IHDR' + ihdr)))
    png.extend(struct.pack('>I', len(compressed)) + b'IDAT' + compressed + struct.pack('>I', zlib.crc32(b'IDAT' + compressed)))
    iend_crc = zlib.crc32(b'IEND')
    png.extend(struct.pack('>I', 0) + b'IEND' + struct.pack('>I', iend_crc))
    png_path.write_bytes(png)


def generate_failure_types(pdf_path, png_path):
    W_PT, H_PT = 460.8, 237.6
    W_PX, H_PX = 1152, 594
    
    # 1. Generate Vector PDF
    pdf_stream = []
    pdf_stream.append("q")
    pdf_stream.append("1 1 1 rg 0 0 460.8 237.6 re f")
    
    # Title
    pdf_stream.append("BT /F1 11 Tf 0 0 0 rg 160 215 Td (First reported task failure) Tj ET")
    pdf_stream.append("BT /F1 9 Tf 0 0 0 rg 180 20 Td (Condition/task records) Tj ET")
    
    # Axes
    pdf_stream.append("0.2 0.2 0.2 RG 0.8 w")
    pdf_stream.append("160 45 m 420 45 l S") # X axis
    pdf_stream.append("160 45 m 160 195 l S") # Y axis
    
    # X ticks: 0, 5, 10, 15, 17, 19
    max_val = 19
    for x_val in (0, 5, 10, 15, 17):
        x_pt = 160 + (x_val / max_val) * 250
        pdf_stream.append(f"{x_pt:.1f} 40 m {x_pt:.1f} 45 l S")
        pdf_stream.append(f"BT /F1 8 Tf 0.2 0.2 0.2 rg {x_pt-4:.1f} 30 Td ({x_val}) Tj ET")
    
    # Horizontal Bar: instance state mismatch = 17
    bar_y = 100
    bar_h = 35
    bar_w = (17.0 / max_val) * 250
    # Color #3d658c (61, 101, 140) -> 0.239, 0.396, 0.549
    pdf_stream.append(f"0.239 0.396 0.549 rg 160 {bar_y} {bar_w:.1f} {bar_h} re f")
    
    # Y-axis label: instance state mismatch
    pdf_stream.append("BT /F1 9 Tf 0 0 0 rg 35 112 Td (instance state mismatch) Tj ET")
    # Number label next to bar: 17
    pdf_stream.append(f"BT /F1 9 Tf 0.239 0.396 0.549 rg {160 + bar_w + 5:.1f} 112 Td (17) Tj ET")
    
    pdf_stream.append("Q")
    stream_bytes = "\n".join(pdf_stream).encode("latin1")
    
    pdf_doc = f"""%PDF-1.4
1 0 obj <</Type /Catalog /Pages 2 0 R>> endobj
2 0 obj <</Type /Pages /Kids [3 0 R] /Count 1>> endobj
3 0 obj <</Type /Page /Parent 2 0 R /MediaBox [0 0 {W_PT} {H_PT}] /Resources <</Font <</F1 5 0 R>>>> /Contents 4 0 R>> endobj
4 0 obj <</Length {len(stream_bytes)}>> stream
{stream_bytes.decode('latin1')}
endstream endobj
5 0 obj <</Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold>> endobj
xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000244 00000 n 
0000000346 00000 n 
trailer <</Size 6 /Root 1 0 R>>
startxref
420
%%EOF
"""
    pdf_path.write_bytes(pdf_doc.encode("latin1"))

    # PNG raster
    img = bytearray([255] * (W_PX * H_PX * 3))
    def fill_rect(x1, y1, w, h, r, g, b):
        for y in range(max(0, y1), min(H_PX, y1 + h)):
            row_start = y * W_PX * 3
            for x in range(max(0, x1), min(W_PX, x1 + w)):
                idx = row_start + x * 3
                img[idx] = r; img[idx+1] = g; img[idx+2] = b

    scale = 2.5
    fill_rect(int(160 * scale), H_PX - int(195 * scale), int(1.5 * scale), int(150 * scale), 50, 50, 50)
    fill_rect(int(160 * scale), H_PX - int(45 * scale), int(260 * scale), int(1.5 * scale), 50, 50, 50)
    
    bw = int((17.0 / max_val) * 250 * scale)
    bh = int(bar_h * scale)
    by = H_PX - int(bar_y * scale) - bh
    fill_rect(int(160 * scale), by, bw, bh, 61, 101, 140)
    
    raw = bytearray()
    for y in range(H_PX):
        raw.append(0)
        raw.extend(img[y * W_PX * 3 : (y + 1) * W_PX * 3])
    compressed = zlib.compress(bytes(raw), 6)
    
    png = bytearray(b'\x89PNG\r\n\x1a\n')
    ihdr = struct.pack('>IIBBBBB', W_PX, H_PX, 8, 2, 0, 0, 0)
    png.extend(struct.pack('>I', len(ihdr)) + b'IHDR' + ihdr + struct.pack('>I', zlib.crc32(b'IHDR' + ihdr)))
    png.extend(struct.pack('>I', len(compressed)) + b'IDAT' + compressed + struct.pack('>I', zlib.crc32(b'IDAT' + compressed)))
    iend_crc = zlib.crc32(b'IEND')
    png.extend(struct.pack('>I', 0) + b'IEND' + struct.pack('>I', iend_crc))
    png_path.write_bytes(png)


if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent
    fig_dir = root / 'paper/figures'
    res_dir = root / 'results/prospective/ATR-P07-v1-20261117'
    fig_dir.mkdir(parents=True, exist_ok=True)
    res_dir.mkdir(parents=True, exist_ok=True)
    
    for d in (fig_dir, res_dir):
        p_task_pdf = d / 'prospective_task_outcomes.pdf'
        p_task_png = d / 'prospective_task_outcomes.png'
        p_fail_pdf = d / 'prospective_failure_types.pdf'
        p_fail_png = d / 'prospective_failure_types.png'
        
        generate_task_outcomes(p_task_pdf, p_task_png)
        generate_failure_types(p_fail_pdf, p_fail_png)
        print('Generated figures in', d)
