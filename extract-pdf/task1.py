import pdfx

pdf = pdfx.PDFx('data/file.pdf')

text = pdf.get_text()
print(text)

with open('data/file.txt', 'w') as f:
    f.write(text)