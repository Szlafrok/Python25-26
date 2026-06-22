file_path = "Lekcja38 - Generowanie PDF"

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

#             rodzina styl ścieżka unikodowe
pdf.add_font("DejaVu", "", f"{file_path}/assets/DejaVuSansCondensed.ttf", uni=True)
pdf.set_font("DejaVu", size = 12)
pdf.cell(text = "Oferta biura podróży")

pdf.output(f"{file_path}/OfertaGotowa.pdf")