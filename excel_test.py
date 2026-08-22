import openpyxl

# エクセルを読み込む
book = openpyxl.load_workbook("./excel/translate.xlsx")
sheet = book.active

text = sheet["A1"].value

print(text)

