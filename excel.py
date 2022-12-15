
import xlsxwriter

def createNewExcelFile(nome_do_novo_arquivo):
    try:
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook(nome_do_novo_arquivo)
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
        ##worksheet.write(2, 0, 123)
        ##worksheet.write(10, 0, 123.456)

        # Insert an image.
        ##worksheet.insert_image('B5', 'logo.png')

        workbook.close()
    except xlsxwriter.exceptions.FileCreateError:
        print("\033[31;1mFATAL ERROR!!!\033[m")
        print("\033[31;1mNão é possivel executar o programa se a tabela do excel estiver aberta!!!\033[m")

###O codigo acima serve somente para criar a planilha excel, então se você rodar esse programa e ja existir uma planilha
###do excel criada ele ira sobrescrever o conteudo da mesma e você perdera todo o conteudo!



###Já o codigo a baixo serve para adicionar conteudos novos a uma planilha do excel já existente, então se você codar
###Esse programa ele não irá sobrescrever o conteudo ja existente e sim acrescentar mais conteudo. Todavia você não
###perdera nenhum conteudo porem poderá adicionar um conteudo novo indesejado na sua planilha!



import openpyxl

def append(nome_do_arquivo_xlsx, usuario, evento, tipo):
    try:
        workbook_obj = openpyxl.load_workbook(nome_do_arquivo_xlsx)
        sheet_obj = workbook_obj.active
        col1 = f'user: {usuario}'
        col2 = f'Evento: {evento}'
        col3 = f'Tipo: {tipo}'###O parametro tipo e referencia a se é um diretorio ou nao!!!

        sheet_obj.append([col1, col2, col3])
        workbook_obj.save(nome_do_arquivo_xlsx)
    except PermissionError:
        print("\033[31;1mFATAL ERROR!!!\033[m")
        print("\033[31;1mNão é possivel executar o programa se a tabela do excel estiver aberta!!!\033[m")

append('teste.xlsx')

