import sys
import os
from fpdf import FPDF


def process_jpg_floder(path):

    pdf = FPDF()
    pdf.set_auto_page_break(0)

    imagelist = [i for i in os.listdir(path)]

    for image in sorted(imagelist):
        if image.endswith('.jpg'):
            pdf.add_page()
            pdf.image(os.path.join(path, image))

    pdf.output(os.path.join(path, "Output.pdf"), "F")


def process_jpg(path):
    pdf = FPDF()
    pdf.set_auto_page_break(0)
    pdf.add_page()
    pdf.image(path)
    ext = os.path.splitext(path)
    pdf.output(ext[0]+'.pdf', "F")


if __name__ == '__main__':

    floder_list = sys.argv[1:]

    for path in floder_list:

        if os.path.isdir(path):
            process_jpg_floder(path)
        elif os.path.isfile(path):
            process_jpg(path)
