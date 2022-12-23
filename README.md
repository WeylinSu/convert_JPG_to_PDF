# convert_JPG_to_PDF
Convert JPG file to PDF with python fpdf library. 

## Usage 1

Passing the path of jpg file or floder. Multiple argument is supported.

```cmd
# python3 convert.py ./test.jpg

# python3 convert.py ./test/

# python3 convert.py ./test.jpg ./test/
```

The same titled PDF file will be created on the same path when passed argument is JPG file. 

However, a file named Output.pdf file will be created in a certain floder if the passed path argument is floder.

## Usage 2

Pyinstaller can be ultilized if your colleagues want to use it while those who have not python environment.

```cmd
# pyinstaller -D -p .\env\Lib -i .\favicon.ico  .\convert.py
```