file_path = "Lekcja38 - Generowanie PDF"

from fpdf import FPDF

A4_WIDTH = 210
A4_HEIGHT = 297

pdf = FPDF()
pdf.add_page()

#             rodzina styl ścieżka unikodowe
pdf.add_font("DejaVu", "", f"{file_path}/assets/DejaVuSansCondensed.ttf", uni=True)
pdf.set_font("DejaVu", size = 32)
pdf.set_text_color("#2eacff")

pdf.text(text = "Oferta biura podróży", x = 40, y = 20)

pdf.output(f"{file_path}/OfertaGotowa.pdf")