from fpdf import FPDF
import os

def capitalize_words(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

class Certificate(FPDF):
    def header(self):
        self.set_font('Arial', '', 45)
        self.cell(0, 25, 'Certificate', align='C')

# List of names
names = ["Mohamed Aly", "Mohamed Ayman"]

for name in names:
    certificate = Certificate(format=(3300, 2550))
    certificate.add_page()

    certificate_template = 'sample-certificate.jpg'
    certificate.image(certificate_template, x=0, y=0, w=3300, h=2550)

    certificate_text = capitalize_words(name)

    certificate.set_font('Arial', 'B', 700)
    certificate.set_text_color(55, 55, 55)

    # Calculate the position to center the text horizontally
    text_width = certificate.get_string_width(certificate_text)
    text_x = (certificate.w - text_width) / 2

    certificate.text(text_x, 1300, certificate_text)

    output_file = name + '.pdf'

    # Check if the file already exists
    counter = 1
    while os.path.exists(output_file):
        # If the file already exists, append a counter to the filename
        output_file = f"{name}_{counter}.pdf"
        counter += 1

    certificate.output(output_file)