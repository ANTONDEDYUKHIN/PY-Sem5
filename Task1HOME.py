# Напишите программу, удаляющую из текста все слова содержащие "абв".

text_old = "абв куда напрабваво абведем едем"

def delete_words(text_old):
    text_old = list(filter(lambda x: 'абв' not in x, text_old.split()))
    return " ".join(text_old)

text_old = delete_words(text_old)
print(text_old)