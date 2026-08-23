import openpyxl
from google import genai

# エクセルを読み込む
book = openpyxl.load_workbook("./excel/translate.xlsx")
sheet = book.active

SOURCE_LANG = sheet["A1"].value # 翻訳元言語
TARGET_LANG = sheet["B1"].value # 翻訳先言語

print("翻訳元言語：" + SOURCE_LANG  + "、翻訳先言語：" + TARGET_LANG)

client = genai.Client()

index = 2 # A2から開始
while True: # 無限ループ
    # A列の文章を読み取る
    translate_text = sheet[f"A{index}"].value
    # A列が空白の場合はループを抜ける
    if translate_text is None or translate_text == "":
        break
    # 翻訳を実行する
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = SOURCE_LANG + "を" + TARGET_LANG + "に翻訳（最適な結果を１つだけ返してください）：" + translate_text
    )
    # B列に結果を書き込む
    sheet[f"B{index}"].value = response.text
    # 次の行に移動する
    index += 1

book.save("./excel/translate.xlsx")
