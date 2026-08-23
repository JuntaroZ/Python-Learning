import openpyxl
from google import genai

# エクセルを読み込む
book = openpyxl.load_workbook("./excel/translate.xlsx")
sheet = book.active

source_lang = sheet["A1"].value # 翻訳元言語
target_lang = sheet["B1"].value # 翻訳先言語

print("翻訳元言語：" + source_lang  + "、翻訳先言語：" + target_lang)

client = genai.Client()

index = 2 # A2から開始
while True: # 無限ループ
    # A列の文章を読み取る
    translate_text = sheet[f"A{index}"].value
    if translate_text is None or translate_text == "":
        break

    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = source_lang + "を" + target_lang + "に翻訳（最適な結果を１つだけ返してください）：" + translate_text
    )
    # B列に結果を書き込む
    sheet[f"B{index}"].value = response.text
    index += 1

book.save("./excel/translate.xlsx")
