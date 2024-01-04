import difflib
import spacy
from spacy.lang.ru import Russian
# Для установки
# python -m spacy download ru_core_news_lg

nlp = spacy.load("ru_core_news_lg")


def similarity_dif(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

def agenta (ls):
    print('Кластеризация и упорядочивание списка кортежей..')
    # Выделение списка содержания
    all_headers = [i for i, *j in ls]
    print(all_headers)

    # НАКИДАЛИ ВСЕ В ОДНО И ПОТОМ ОЧИСТИЛИ
    # all_headers = list(chain(headers, s22, s11))
    # print(all_headers)
    for h2 in all_headers:
        noh2 = [x for x in all_headers if x != h2]
        q1 = nlp(h2)
        for el in noh2:
            q2 = nlp(el)
            if q1.similarity(q2) > 0.7 or similarity_dif(h2, el) > 0.5:
                try:
                    all_headers.remove(h2)
                except:
                    pass
    # for el in all_headers:
        # print('***', el)

    # МИКСОВАНИЕ СОЗДАННОГО СОДЕРЖАНИЯ (1)
    # Идем постепенно по общему содержанию, если видим что, что-то имеет близкую связь то ставим после
    index = 0
    new_all__headers = []
    end = len(all_headers)
    while index < end:
        elem = all_headers[index]
        if elem not in new_all__headers:
            new_all__headers.append(elem)
        # print('****************** ', elem)
        noh2 = all_headers.copy()
        del noh2[index]
        # print('noh2 --->', noh2)
        q1 = nlp(elem)
        for ee in noh2:
            q2 = nlp(ee)
            if q1.similarity(q2) > 0.3:
                # print(elem, '-----', ee, '---- ', q1.similarity(q2))
                # print('2222', new_all__headers)
                if ee not in new_all__headers:
                    new_all__headers.append(ee)
                break


        index = index + 1
    # print(new_all__headers)
    # print(len(new_all__headers))

    h2_text_img_new = [('<h2>' + h + '</h2>', t) for h, t in ls if h in new_all__headers]
    return h2_text_img_new

# ------------------------------------------
# ls = [('', 'ppul'), ('Что такое финики', 'pimgpblockquoteppp'), ('Финики химический состав и пищевая ценность', 'ppulppp'), ('Калорийность фиников', 'imgulpp'), ('Польза фиников для женщин', 'ppulpppppppp'), ('Польза фиников для мужчин', 'ppp'), ('', ''), ('10 полезных свойств фиников', 'imgpol'), ('Вред фиников', 'pulpppulpul'), ('Что такое финики', 'pimgpblockquoteppp'), ('Финики химический состав и пищевая ценность', 'ppulppp'), ('Калорийность фиников', 'imgulpp'), ('Польза фиников для женщин', 'ppulpppppppp'), ('Польза фиников для мужчин', 'ppp'), ('', ''), ('10 полезных свойств фиников', 'imgpol'), ('Вред фиников', 'pulpimgpblockquotepppp'), ('Финики химический состав и пищевая ценность', 'ppulppp'), ('Калорийность фиников', 'imgulpp'), ('Польза фиников для женщин', 'ppulpppppppp'), ('Польза фиников для мужчин', 'ppp'), ('', ''), ('10 полезных свойств фиников', 'imgpol'), ('Вред фиников', 'pulpimgulpp'), ('Польза фиников для женщин', 'ppulpppppppp'), ('Польза фиников для мужчин', 'ppp'), ('', ''), ('', 'imgimgimgimgulppp'), ('Что надо знать о финиках', 'p'), ('Калорийность фиников', 'pulpul'), ('Чем полезны финики: 8 свойств', 'ph3pph3pph3pph3imgppph3pph3pph3pimgph3pp'), ('Вред фиников', 'pp'), ('Как выбрать и хранить финики', 'pimgppp'), ('Комментарий эксперта', 'imgppppppppppppppulpppppp'), ('Что надо знать о финиках', 'p'), ('Калорийность фиников', 'pulpul'), ('Чем полезны финики: 8 свойств', 'ph3ppph3ppph3ppph3imgpimgimgimgpppppph3ppph3ppph3pimgpimgimgimgppph3ppp'), ('Вред фиников', 'ppp'), ('', 'imgimgimgpp'), ('История фиников\xa0', 'ppp'), ('Польза фиников\xa0', 'ppiframeppp'), ('Состав фиников', 'table'), ('Вред фиников', 'pppimg'), ('Применение фиников в медицине\xa0', 'ppimgpimgpp'), ('Применение фиников в кулинарии\xa0', 'ph3pimgtableph3pimgtablepimgpp'), ('Как выбрать и хранить финики', 'pp'), ('Популярные вопросы и\xa0ответы', 'imgimgimgolpp'), ('История фиников\xa0', 'ppp'), ('Польза фиников\xa0', 'ppiframeppp'), ('Состав фиников', 'table'), ('Вред фиников', 'pppimg'), ('Применение фиников в медицине\xa0', 'ppimgpimgpp'), ('Применение фиников в кулинарии\xa0', 'ph3pimgtableph3pimgtablepimgpp'), ('Как выбрать и хранить финики', 'pp'), ('Популярные вопросы и\xa0ответы', 'pp'), ('История фиников\xa0', 'ppp'), ('Польза фиников\xa0', 'ppiframeppp'), ('Состав фиников', 'table'), ('Вред фиников', 'pppimg'), ('Применение фиников в медицине\xa0', 'ppimgpimgpp'), ('Применение фиников в кулинарии\xa0', 'ph3pimgtableph3pimgtablepimgpp'), ('Как выбрать и хранить финики', 'pp'), ('Популярные вопросы и\xa0ответы', 'pp'), ('История фиников\xa0', 'ppp'), ('Польза фиников\xa0', 'ppiframeiframeiframeppp'), ('Состав фиников', 'tabletable'), ('Вред фиников', 'pppimgimgimgimgimg'), ('Применение фиников в медицине\xa0', 'ppimgimgimgpimgimgimgimgimgpp'), ('Применение фиников в кулинарии\xa0', 'ph3pimgimgimgtabletableph3pimgimgimgtabletablepimgppimgimgimgpppp'), ('', 'ulul'), ('Содержание', 'ul'), ('\n\r\n\t Питательная ценность и состав фиников\r\n\n', 'pimgpulppppppp'), ('\n\r\n\t Чем полезны финики\r\n\n', 'pppppp'), ('\n\r\n\t Чем финики полезны для женщин\r\n\n', 'ppp'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('\n\r\n\t Можно ли есть финики при похудении?\r\n\n', 'ppp'), ('\n\r\n\t Как выбрать финики\r\n\n', 'ppppppulul'), ('Содержание', 'ul'), ('\n\r\n\t Питательная ценность и состав фиников\r\n\n', 'pimgpulppppppp'), ('\n\r\n\t Чем полезны финики\r\n\n', 'pppppp'), ('\n\r\n\t Чем финики полезны для женщин\r\n\n', 'ppp'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('\n\r\n\t Можно ли есть финики при похудении?\r\n\n', 'ppp'), ('\n\r\n\t Как выбрать финики\r\n\n', 'ppppppulul'), ('Содержание', 'ul'), ('\n\r\n\t Питательная ценность и состав фиников\r\n\n', 'pimgpulppppppp'), ('\n\r\n\t Чем полезны финики\r\n\n', 'pppppp'), ('\n\r\n\t Чем финики полезны для женщин\r\n\n', 'ppp'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('\n\r\n\t Можно ли есть финики при похудении?\r\n\n', 'ppp'), ('\n\r\n\t Как выбрать финики\r\n\n', 'ppppppulul'), ('Содержание', 'ul'), ('\n\r\n\t Питательная ценность и состав фиников\r\n\n', 'pimgpulppppppp'), ('\n\r\n\t Чем полезны финики\r\n\n', 'pppppp'), ('\n\r\n\t Чем финики полезны для женщин\r\n\n', 'ppp'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('\n\r\n\t Можно ли есть финики при похудении?\r\n\n', 'ppp'), ('\n\r\n\t Как выбрать финики\r\n\n', 'pppppp'), ('Содержание', 'ul'), ('Содержание', 'ul'), ('\n\r\n\t Питательная ценность и состав фиников\r\n\n', 'pimgpulppppppp'), ('\n\r\n\t Чем полезны финики\r\n\n', 'pppppp'), ('\n\r\n\t Чем финики полезны для женщин\r\n\n', 'ppp'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'pppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'ppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'pp'), ('\n\r\n\t Можно ли есть финики при похудении?\r\n\n', 'ppp'), ('\n\r\n\t Как выбрать финики\r\n\n', 'ppppp'), ('\n\r\n\t Питательная ценность и состав фиников\r\n\n', 'ppimgpimgimgppimgimgulppppppppppppppppppppp'), ('\n\r\n\t Чем полезны финики\r\n\n', 'ppppppp'), ('\n\r\n\t Чем финики полезны для женщин\r\n\n', 'pppp'), ('\n\r\n\t Какая польза фиников для мужчин\r\n\n', 'ppppp'), ('\n\r\n\t Как финики могут навредить организму?\r\n\n', 'pppppp'), ('\n\r\n\t Можно ли есть финики каждый день?\r\n\n', 'ppp')]
# list_h2 = [i for i, *j in ls]
# # print(list_h2)
# h2_new = agenta(list_h2)    # -> получили список очищенныый и кластеризованный
# h2_text_img_new = [(h, t) for h, t in ls if h in h2_new]
# print('Итоговый кортеж -->', h2_text_img_new)
# print('Длина Итоговый кортеж -->', len( h2_text_img_new))

#
#
# def similarity_dif(s1, s2):
#   normalized1 = s1.lower()
#   normalized2 = s2.lower()
#   matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
#   return matcher.ratio()
#
# #  -------------------
# doc_1 = nlp('язык python')
# doc_2 = nlp('программирование на питоне')
#
# print(doc_1.similarity(doc_2))