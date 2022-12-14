import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
#worksheet.set_column('A:A', 254.86)
worksheet.set_column("A:A", 30)
worksheet.set_column("B:B", 160)
worksheet.set_column("C:C", 15)
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'user: Douglas (PROGRAMADOR)')
#worksheet.write('A2', 'user: Douglas (PROGRAMADOR)')

# Text with formatting.
worksheet.write('B1', 'Evento modified caminho: \\\\CAPSV\\Users\\Public\\01 - ASPER\\PROC�PIO\\RELAT�RIOS PROCOPIO\\REL. ANC. DOS CINTOS', bold)
worksheet.write('C1', 'diretorio? True')
# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.insert_image('B5', 'logo.png')

workbook.close()



