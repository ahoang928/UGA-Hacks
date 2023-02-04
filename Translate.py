from googletrans import Translator
import googletrans

translator = Translator()
# print(googletrans.LANGUAGES)
# print("test if work")


message = input("Please type the word or sentence you want to translate.\n")


transLang = input("Please type the language you want to translate it to!\n")

try:
    if transLang not in googletrans.LANGCODES:
        raise Exception("This is not a valid language, please try again")


    word = translator.translate(message,dest=transLang)

    print(word.text)
except Exception as f:
    print(f)