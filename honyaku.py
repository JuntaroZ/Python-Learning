from google import genai

# クライアントの初期化（環境変数 GEMINI_API_KEY を自動参照）
client = genai.Client()

# チャットを作成してメッセージを送信
chat = client.chats.create(model="gemini-3.6-flash")
response = chat.send_message("Pythonの魅力を3つ教えてください。")

print(response.text)