# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# 1. ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# 2. підсумкова довжина hashtag має бути не більше 140 символів.
# 3. кожне слово починається з великої літери.
# 4. якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string

def create_hashtag(input_string):
    # Удаляем знаки пунктуации
    translator = str.maketrans('', '', string.punctuation)
    clean_string = input_string.translate(translator)

    # Розбиваем на слова, удаляем пробельі и преобразование каждого слова начитнаться с большой буквьі
    words = clean_string.split()
    capitalized_words = [word.capitalize() for word in words]

    # формируем хештег
    hashtag = '#' + ''.join(capitalized_words)

    # если длина больше 140 символов, обрезаем до 140-го
    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

input_string = input("Введите ряд: ")
result = create_hashtag(input_string)
print(result)

# # # Вводим                                  должньі получить на вьіходе
# Python Community                    ->      #PythonCommunity
# i like python community!            ->      #ILikePythonCommunity
# Should, I. subscribe? Yes!          ->      #ShouldISubscribeYes
# t!e@s#t t%e^s&t'                    ->      #TestTest
