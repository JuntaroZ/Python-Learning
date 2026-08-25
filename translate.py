from google import genai

japanese_text = "Python は最も人気のあるプログラミング言語の1つです。" 
client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash-lite")

response = chat.send_message(
    "日本語を英語に翻訳（英語文１つだけ返してください）：" + japanese_text
)

print("")
print(japanese_text)
print(response.text)
