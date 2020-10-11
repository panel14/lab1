import re

with open ('steam_description_data.csv', encoding='utf-8') as file:
    str = file.read()
    reg_for_chars = re.compile('\w')
    reg_for_words = re.compile('\w[\s.,!?_-]')
    reg_for_sent = re.compile('\w[.!?]')
    print('Количество символов в файле:', len(reg_for_chars.findall(str)),
          '\nКоличество слов в файле:', len(reg_for_words.findall(str)),
          '\nКоличество предложений в файле:', len(reg_for_sent.findall(str)))
