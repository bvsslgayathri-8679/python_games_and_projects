from googletrans import Translator

sen=input("enter a string!!!!!.....")

translator=Translator()
translated_sentence=translator.translate(sen,src="en",dest="ca")


print(translated_sentence.text)



