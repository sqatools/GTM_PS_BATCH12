
import openpyxl

def read_excel_Sheet(file_path, Sheet_name, cell_name,):

    wb = openpyxl.load_workbook(file_path)

    sheet = wb [sheet_name]
