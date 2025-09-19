import openpyxl

def read_execel(file_path, sheet_name, cell_name):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]

    cell = sheet[cell_name]

    print(cell.value)
read_execel(file_path="test_data.XLSX", sheet_name="Sheet1", cell_name="A1")
