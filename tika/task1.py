from tika import parser

parsed_pdf = parser.from_file("data/file.pdf")
data = parsed_pdf['content']
print(parsed_pdf)
print(data)