
def check_agenta(h2_text_img_new):
    print('Чистка списка кортежей по содержанию...')
    ls2 = []
    print('Чистка списка кортежей ls0', h2_text_img_new)

    # Удаление кортежей с пустыми элементами в тексте, наличии кодировок, мусорных слов
    ls2 = list(filter(lambda x: x[1] != '', h2_text_img_new))
    print('Чистка списка кортежей ls2', ls2)

    ls3 = list(filter(lambda x: 'Ð' not in x[1], ls2))
    print('Чистка списка кортежей ls3', ls3)

    # опция удаления если текста меньше 60 символов
    # ls4 = list(filter(lambda x: len(x[1]) > 60, ls3))
    # print('ls4', ls4)

    ls41 = list(filter(lambda x: 'регистрац' or 'скидк' or 'социальные сети' or 'Профи ' not in x[1], ls3))
    print('Чистка списка кортежей ls41', ls41)
    ls42 = list(filter(lambda x: 'телефон' not in x[1], ls41))
    print('Чистка списка кортежей ls42', ls42)
    ls5 = list(filter(lambda x: 'mail' not in x[1], ls42))
    print('Чистка списка кортежей.. Итоговый список', ls5)

    # непонятно что делает код ???? Удаление вроде если нет заголовка
    # ls6 = []
    # for i in ls5:
    #     # print(i)
    #     if i[0] != '' or ls5.index(i) != 0:
    #         ls6.append(i)
    # h2_text_img_new_clear = ls6

    h2_text_img_new_clear = ls5
    return h2_text_img_new_clear

# ls =  [('', 'ppul'), ('', ''), ('Вред фиников', 'pulpppulpul'), ('', ''), ('Вред фиников', 'pulpimgpblockquotepppp'), ('', ''), ('Вред фиников', 'pulpimgulpp'), ('', ''), ('', 'imgpimgimgpppulpp'), ('Вред и противопоказания', 'ppppppp'), ('Как выбирать и хранить финики', 'ppp'), ('Финики в кулинарии', 'ppulpppulpp'), ('Вред и противопоказания', 'pppppppppppp'), ('', 'ulul'), ('Содержание', 'ul'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('Содержание', 'ul'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('Содержание', 'ul'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('Содержание', 'ul'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('Содержание', 'ul'), ('Содержание', 'ul'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'ppppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'pppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'ppp'), ('', 'imgimgimgimgulppp'), ('Что надо знать о финиках', 'p'), ('Чем полезны финики: 8 свойств', 'ph3pph3pph3pph3imgppph3pph3pph3pimgph3pp'), ('Вред фиников', 'pp'), ('Комментарий эксперта', 'imgppppppppppppppulpppppp'), ('Что надо знать о финиках', 'p'), ('Чем полезны финики: 8 свойств', 'ph3ppph3ppph3ppph3imgpimgimgimgpppppph3ppph3ppph3pimgpimgimgimgppph3ppp'), ('Вред фиников', 'ppp')]
# check_agenta(ls)