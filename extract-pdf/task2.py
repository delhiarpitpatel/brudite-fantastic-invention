import os
from fpdf import FPDF

font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'NotoSans-Regular.ttf')

pdf = FPDF()
pdf.add_page()

pdf.add_font("NotoSans", style="", fname=font_path, uni=True)

pdf.set_font("NotoSans", size=12)

text_content = ""
with open('data/file.txt', "r", encoding="utf-8") as f:
    store = True
    for line in f.readlines():
        if line.isspace():
            continue
        if store :
            text_content += line
        store = not store

print(text_content)

pdf.multi_cell(0, 10, txt=text_content)

pdf.output("data/file-new.pdf")
