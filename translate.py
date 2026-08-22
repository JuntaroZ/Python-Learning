from google import genai

japanese_text = "Python は最も人気のあるプログラミング言語の1つです。" 
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="日本語を英語に翻訳（英語文１つだけ返してください）：" + japanese_text
)

print("")
print(japanese_text)
print(response.text)
