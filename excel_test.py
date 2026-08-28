import openpyxl

# エクセルを読み込む
book = openpyxl.load_workbook("./excel/translate.xlsx")
sheet = book.active

text = sheet["A1"].value

print(text)


# エクセルを上書きセーブする処理
# book.save("./excel/translate.xlsx")
