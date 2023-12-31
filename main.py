from fpdf import FPDF
import os

# ################################################################################# global variables

# Import the external font and register it
font_path = r"fonts\Alice-Regular.ttf"  # Replace with the correct file path
font_name = "Alice"      # A custom name for the font, you can choose any name

# Change these based on the use
input_file = 'level2_names.txt'
certificate_template = 'level_2.png'
output_folder = "level_2"

# Initialize the names list and rank
names = []
ranks = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th"]
rank = 0

# ################################################################################# functions


def capitalize_words(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


# Read names from the text file and add them to the names list
with open(input_file, 'r') as file:
    for line in file:
        names.append(line.strip())


# ################################################################################# Our Class
class Certificate(FPDF):
    def header(self):
        # self.set_font('Arial', '', 45)
        # self.add_font(arabic_font, '', arabic_path, uni=True)  # Set is_rtl to True for Arabic text
        self.add_font(font_name, '', font_path, uni=True)
        self.set_font(font_name, '', 45)
        self.cell(0, 25, 'Certificate', align='C')


# ################################################################################# Main work
for name in names:
    # writing the name

    certificate = Certificate(format=(2000, 1414))
    certificate.add_page()
    certificate.image(certificate_template, x=0, y=0, w=2000, h=1414)

    certificate_text = capitalize_words(name)

    # set different font size for each name size
    words = name.split()
    if len(words) == 2:
        certificate.set_font(font_name, '', 350)
    if len(words) == 3:
        certificate.set_font(font_name, '', 320)
    if len(words) > 3:
        certificate.set_font(font_name, '', 220)

    certificate.set_text_color(55, 55, 55)
    name_width = certificate.get_string_width(certificate_text)
    name_x = (certificate.w - name_width) / 2
    certificate.text(name_x, 585, certificate_text)

    # writing the rank
    certificate.set_font(font_name, '', 210)
    certificate.set_text_color(55, 55, 55)
    rank_width = certificate.get_string_width(ranks[rank])
    rank_x = (certificate.w - rank_width) / 2
    certificate.text(rank_x, 950, ranks[rank])
    rank += 1

    output_file = name + '.pdf'
    # Set the output file path in the certificates folder
    output_file = os.path.join(output_folder, name + '.pdf')

    # Check if the file already exists
    counter = 1
    while os.path.exists(output_file):
        # If the file already exists, append a counter to the filename
        output_file = os.path.join(output_folder, f"{name}_{counter}.pdf")
        counter += 1

    certificate.output(output_file)
    