from collections import OrderedDict


def cort(tags):
    print('Созданеие кортежей...')
    h2 = ""
    abzac_str = ""
    cort_list = []
    cort_h2_tags = ()
    # Сформировать кортеж Н2 и Tags
    for tag in tags:
        # print('====', tag.name)
        cort_h2_tags = (h2, abzac_str)
        if tag.name == 'h2':
            # print('__', tag.text)
            abzac_str = ''
            h2 = str(tag.text).strip()
            # h2 = tag
            # Добавление тега Н2 в кортеж
            all_empty = all(element == '' for element in cort_h2_tags)
            if all_empty:
                print('пустой кортеж')
            else:
                cort_list.append(cort_h2_tags)
        else:
            # добавление тегов в виде текста
            # abzac_str = abzac_str + str(tag) + ''
            # добавление только названий тегов для тестирования
            # abzac_str = abzac_str + str(tag.name) + ''
            abzac_str = abzac_str + str(tag)
            # abzac_str = abzac_str + tag
            # print('--', abzac_str)

        # print('текущий кортеж ', cort_list)

    # Если в названии есть слово содержание то удаляем этот кортеж
    try:
        for el in cort_list:
            index = cort_list.index(el)
            if 'содержание' in el[0].lower():
                del cort_list[index]
    except:
        pass

    print('*** Создание кортежей ****', cort_list)
    return cort_list