import re

with open ("steam_description_data.csv", encoding='utf-8') as file:
    str = file.read()
    reg_for_chars = re.compile('\w')
    print("Количество символов в файле:", len(reg_for_chars.findall(str)))
    reg_for_words = re.compile('\w[\s.,!?_-]')
    print("Количество слов в файле:", len(reg_for_words.findall(str)))
    reg_for_sent = re.compile('\w[.,!?_-]')
    print("Количество слов в файле:", len(reg_for_sent.findall(str)))
