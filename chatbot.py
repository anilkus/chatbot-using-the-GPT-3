import openai
import speech_recognition as sr
import pyttsx3

# OpenAI API anahtarını ayarlama
openai.api_key = "API-KEY"

# Sesli soru sorma ve cevap verme işlemlerini gerçekleştirme
def ask_question(prompt):
  # Soru sorma
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print(prompt)
    audio = r.listen(source)

  # Soru metnini alma
  question = r.recognize_google(audio, language="tr-TR")
  print(f"Soru: {question}")

  # GPT-3 dil modelini kullanarak cevap verme
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=question,
      max_tokens=1024,
      temperature=0.5,
  ).choices[0].text
  print(f"Cevap: {response}")

  # Cevap sesli olarak okuma
  engine = pyttsx3.init()
  engine.say(response)
  engine.runAndWait()

# Örnek soru sorma
ask_question("Merhaba! Ben bir chatbot'um. Sizden bir soru sormamı ister misiniz?")
