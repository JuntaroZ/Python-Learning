import openpyxl
from google import genai
from itertools import count

# エクセルを読み込む
book = openpyxl.load_workbook("./excel/translate.xlsx")
sheet = book.active

SOURCE_LANG = sheet["A1"].value # 翻訳元言語をシートA1から取得
TARGET_LANG = sheet["B1"].value # 翻訳先言語をシートB1から取得

print("翻訳元言語：" + SOURCE_LANG  + "、翻訳先言語：" + TARGET_LANG)

client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash-lite")

for index in count(2): # 無限ループ
    # A列の文章を読み取る
    translate_text = sheet[f"A{index}"].value
    # A列が空白の場合はループを抜ける
    if translate_text is None or translate_text == "":
        break
    # 翻訳を実行する
    response = chat.send_message(
        SOURCE_LANG + "を" + TARGET_LANG + 
        "に翻訳（翻訳結果を１つ返してください）：" + translate_text
    )
    # B列の各行に結果(response.text)を書き込む
    sheet[f"B{index}"].value = response.text

book.save("./excel/translate.xlsx")