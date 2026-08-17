from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Pythonの魅力を3つ教えてください。"
)

print("")
print(response.text)