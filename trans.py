rom googletrans import Translator

translator = Translator()
text = "Hello, how are you?"
translated = translator.translate(text, dest='hi)print(translated.text)  # Outputs: "नमस्ते, आप कैसे हैं?"
