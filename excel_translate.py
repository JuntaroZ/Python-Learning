import openpyxl
from google import genai

# エクセルを読み込む
book = openpyxl.load_workbook("./excel/translate.xlsx")
sheet = book.active

client = genai.Client()

# A2～A11を順番に処理
for row in range(2, 11):

    # A列の日本語を読み取る
    japanese_text = sheet.cell(row=row, column=1).value

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="日本語を英語に翻訳（英語文１つだけ返してください）：" + japanese_text
    )
    # エクセルに書き込む
    sheet.cell(row=row, column=2).value = response.text

book.save("./excel/translate.xlsx")
