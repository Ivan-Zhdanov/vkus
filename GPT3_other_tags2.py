# Создание нового текста от вопроса в OPENAI
import openai
import time
import re
import requests
from GPT3_API_cheker import api_cheker, list_api
from Get_url_Img_from_WP import take_url_img_from_wp
from Api_List import api_list
import threading
from log_write import log_api
# предыдущий ключ с аккаунта ivan.zhdanov.moscow4
# openai.api_key = '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'

# 28/09
# openai.api_key = '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'

# ключ от аккаунта helloword (5$)
# openai.api_key = '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'

model_id = 'gtp-3.5-turbo'
num_text = ()

apis = api_list
th_list = []
step = 5
#     return th_list


# def GPT3_Model(i, query):
#     api1 = apis[i]['api']
#     openai.api_key = api1
#     openai.organization = apis[i]['org']
#     print("Текущий АПИ = ", api1)
#     try:
#         print("КАКОЙ ЗАПРОС ________________________ ", query)
#         responce = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             # model="gpt-3.5-turbo-16k-0613",
#             max_tokens=3500,
#             messages=[
#                 {"role": "system", "content": ""},
#                 {"role": "user", "content": f"{query}"},
#             ]
#         )
#         text3 = responce['choices'][0]['message']['content']
#         print("************")
#         flag = True
#         break
#     except Exception as e:
#         print('Название ошибки --', e)
#         # if 'RPM' in e:
#         time.sleep(3)
#         apis[i]['err'] = 1
#
#         # запись в лог файл об ошибках по api
#         log_api(i, e, api1)
#
#         # берем следующий api
#         i = i + 1
#         if i > step: i = 0

def GPT3(query):
    org = ''
    api = ''
    # Создали список из потоков которые обрабатывают
    thread_id = threading.current_thread().ident
    print(f"Текущий номер потока: {thread_id}")

    if thread_id in th_list:
        pass
    else:
        try:
            th_list.append(thread_id)
        except:
            pass

    # time.sleep(21)
    # print('71')
    if th_list.index(thread_id) == 0:
        time.sleep(22)
        i = 0
        print('Первый поток 1111111')
        flag = False
        while flag == False:
            print('в потоке 1 api под номером - ', i)

            if apis[i]['err'] == 1:
                i = i + 1
                print('текущий апи с ошибкой следующий')
                continue
            # if i > step: i = 0

            api1 = apis[i]['api']
            openai.api_key = api1
            openai.organization = apis[i]['org']
            print("Текущий АПИ = ", api1)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text3 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                if 'maximum context length' in e:
                    pass
                time.sleep(4)
                apis[i]['err'] = 1

                # запись в лог файл об ошибках по api
                log_api(i, e, api1)

                # берем следующий api
                i = i + 1
                if i > step: i = 0
        return text3


    elif th_list.index(thread_id) == 1:
        time.sleep(22)
        j = step
        print('Второй поток 2222222')

        flag = False
        while flag == False:
            print('в потоке 2 api под номером - ', j)

            if apis[j]['err'] == 1:
                j = j + 1
                print('текущий апи с ошибкой следующий')
                continue
            # if j > step*2: j = step

            api2 = apis[j]['api']
            openai.api_key = api2
            openai.organization = apis[j]['org']
            print("Текущий АПИ = ", api2)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text32 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(4)
                apis[j]['err'] = 1

                # запись в лог файл об ошибках по api
                log_api(j, e, api2)

                # берем следующий api
                j = j + 1
                if j > step*2: j = step

        return text32

    elif th_list.index(thread_id) == 2:
        time.sleep(22)
        k = step*2
        print('Третий поток 333333333')
        flag = False
        while flag == False:
            print('в потоке 3 api под номером - ', k)

            if apis[k]['err'] == 1:
                k = k + 1
                print('текущий апи с ошибкой следующий')
                continue
            # if k > step*3: k = step*2

            api3 = apis[k]['api']
            openai.api_key = api3
            openai.organization = apis[k]['org']
            print("Текущий АПИ = ", api3)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)

                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text33 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(4)
                apis[k]['err'] = 1

                # запись в лог файл об ошибках по api
                log_api(k, e, api3)

                # берем следующий api
                k = k + 1
                if k > step*3: k = step*2
        return text33


    elif th_list.index(thread_id) == 3:
        time.sleep(22)
        h = step*3
        print('Четвертый поток')
        flag = False
        while flag == False:
            print('в потоке 4 api под номером - ', h)

            if apis[h]['err'] == 1:
                h = h + 1
                continue
            # if h > step*4: h = step*3

            api4 = apis[h]['api']
            openai.api_key = api4
            openai.organization = apis[h]['org']
            print("Текущий АПИ = ", api4)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text34 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(3)
                apis[h]['err'] = 1
                # запись в лог файл об ошибках по api
                log_api(h, e, api4)

                # берем следующий api
                h = h + 1
                if h > step*4: h = step*3
        return text34




    elif th_list.index(thread_id) == 4:
        time.sleep(22)
        g = step*4
        print('Пятый поток')
        flag = False
        while flag == False:
            print('в потоке 5 api под номером - ', g)

            if apis[g]['err'] == 1:
                g = g + 1
                continue
            # if g > step*5: i = step*4

            api5 = apis[g]['api']
            openai.api_key = api5
            openai.organization = apis[g]['org']
            print("Текущий АПИ = ", api5)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text35 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(3)
                apis[g]['err'] = 1
                # запись в лог файл об ошибках по api
                log_api(g, e, api5)

                # берем следующий api
                g = g + 1
                if g > step*5: g = step*4
        return text35


    elif th_list.index(thread_id) == 5:
        time.sleep(22)
        f = step * 5
        print('Шестой поток')
        flag = False
        while flag == False:
            print('в потоке 6 api под номером - ', f)
            api6 = apis[f]['api']
            openai.api_key = api6
            openai.organization = apis[f]['org']
            print("Текущий АПИ = ", api6)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text36 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(2)
                apis[f]['err'] = 1
                # запись в лог файл об ошибках по api
                log_api(f, e, api6)

                # берем следующий api
                f = f + 1
                if f > step * 6: f = step * 5
        return text36


    elif th_list.index(thread_id) == 6:
        time.sleep(22)
        s = step * 6
        print('Седьмой поток')
        flag = False
        while flag == False:
            print('в потоке 7 api под номером - ', s)
            api7 = apis[s]['api']
            openai.api_key = api7
            openai.organization = apis[s]['org']
            print("Текущий АПИ = ", api7)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text37 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as e:
                print('Название ошибки --', e)
                # if 'RPM' in e:
                time.sleep(2)
                apis[s]['err'] = 1
                # запись в лог файл об ошибках по api
                log_api(s, e, api7)

                # берем следующий api
                s = s + 1
                if s > step * 7: s = step * 6
        return text37


    elif th_list.index(thread_id) == 7:
        time.sleep(22)
        e = step * 7
        print('Восьмой поток')
        flag = False
        while flag == False:
            print('в потоке 8 api под номером - ', e)
            api8 = apis[e]['api']
            openai.api_key = api8
            openai.organization = apis[e]['org']
            print("Текущий АПИ = ", api8)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text38 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as ee:
                print('Название ошибки --', ee)
                # if 'RPM' in e:
                time.sleep(2)
                apis[e]['err'] = 1
                # запись в лог файл об ошибках по api
                log_api(e, ee, api8)

                # берем следующий api
                e = e + 1
                if e > step * 8: e = step * 7
        return text38


    elif th_list.index(thread_id) == 8:
        time.sleep(22)
        n = step * 8
        print('Девятый поток')
        flag = False
        while flag == False:
            print('в потоке 9 api под номером - ', n)
            api9 = apis[n]['api']
            openai.api_key = api9
            openai.organization = apis[n]['org']
            print("Текущий АПИ = ", api9)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text39 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as ee:
                print('Название ошибки --', ee)
                # if 'RPM' in e:
                time.sleep(2)
                apis[n]['err'] = 1
                # запись в лог файл об ошибках по api
                log_api(n, ee, api9)

                # берем следующий api
                n = n + 1
                if n > step * 9: n = step * 8
        return text39


    elif th_list.index(thread_id) == 9:
        time.sleep(22)
        t = step * 9
        print('Девятый поток')
        flag = False
        while flag == False:
            if apis[t]['err'] == 1:
                t = t + 1
                continue
            if t > step * 10: t = step * 9

            print('в потоке 9 api под номером - ', t)
            api10 = apis[t]['api']
            openai.api_key = api10
            openai.organization = apis[t]['org']
            print("Текущий АПИ = ", api10)
            try:
                print("КАКОЙ ЗАПРОС ________________________ ", query)
                responce = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    # model="gpt-3.5-turbo-16k-0613",
                    max_tokens=3500,
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": f"{query}"},
                    ]
                )
                text310 = responce['choices'][0]['message']['content']
                print("************")
                flag = True
                break
            except Exception as ee:
                print('Название ошибки --', ee)
                # if 'RPM' in e:
                time.sleep(2)
                apis[t]['err'] = 1
                # запись в лог файл об ошибках по api
                log_api(t, ee, api10)

                # берем следующий api
                t = t + 1
                if t > step * 10: t = step * 9
        return text310



def Chat_converstaion_ppp(tag):
    html = ''
    print('ТЕКУЩИЙ ТЕГ:', tag)
    try:
        if tag.name == 'h2' or tag.name == 'h3':
            h2 = tag.text
            print(h2)
            html = '<h2>' + h2 + '</h2>'

        elif tag.name == 'p':
            abzac_str = tag.text
            flag = False
            if len(abzac_str) < 40:
                html = abzac_str
                flag = True
            while flag == False:
                try:
                    print('строка ', abzac_str)
                    # r1 = Chat_converstaion_p(abzac_str)
                    query21 = f'Перепиши, распиши с дополнениями:"""{abzac_str}"""'
                    r1 = GPT3(query21)
                    print('вызвали обработку р нейронкой')
                    r1_clean = re.sub(r'^([«»]+)|([«»]+)$', '', r1)
                    html = '<p>' + r1_clean + '</p>'
                    flag = True
                except Exception as e:
                    print('ошибка в теге Р ', e)
                    html = ''
                    print('ожидание 10c ...')
                    time.sleep(2)

        elif tag.name == 'ul' or tag.name == 'ol':
            # r2 = Chat_converstaion_ul_ol(tag)
            query22 = f'Перепиши с дополнением оставляя html теги:"""{tag}"""'
            r2 = GPT3(query22)
            print(tag, ' ---> ', r2)
            r21 = str(r2).replace("<li><li>","<li>").replace("</li></li>", "</li>")
            print('_____', r21)
            html = r21

        elif tag.name == 'table':
            # r3 = Chat_converstaion_table(tag)
            query23 = f'Перепиши таблицу с дополнением оставляя html теги:"""{tag}"""'
            r3 = GPT3(query23)
            print(tag, ' ---> ', r3)
            html = r3

        elif tag.name == 'blockquote':
            # r4 = Chat_converstaion_quote(tag)
            query24 = f'Перепиши с дополнением оставляя html  теги:"""{tag}"""'
            r4 = GPT3(query24)
            print(tag, ' ---> ', r4)
            html = r4

        # !!! необходимо чтобы найденный тег был простым !!!!
        elif tag.name == 'img':
            print('------_', tag)
            print('img_1')
            src_value = None
            # src_list = ['data-wpfc-original-srcset']
            src_list = ['src', 'srcset', 'data-wpfc-original-src', 'data-src', 'src-lazy']


            for s in src_list:
                print('img_2')
                print('вид src оторый нашли', s)
                src_value = tag.get(s)
                print('valueeeeeeeee', src_value)


                # нашли первый src
                if src_value:
                    break
            if src_value:
                print('valuee intooooo', src_value)
                # domain = 'https://foodandhealth.ru'
                domain = ' https://fructberry.com'
                print(domain)
                # закрыл обработку если урл не полный и его соединение с базовым урлом
                # full_url = requests.compat.urljoin(url_1, src_value)
                if rf'{domain}' in src_value:
                    full_url = src_value
                    print('555', full_url)
                else:
                    # full_url = 'https://polzaivrededy.ru' + src_value

                    print('777')
                    # full_url = domain + src_value
                    full_url = src_value
                    print('888')
                print(full_url)
                img_str = full_url
                # Добавление тега с картиной с урлом
                try:
                    img_str = take_url_img_from_wp(full_url)
                except:
                    img_str = ""
                    print('ошибка в заливке картинки')
                print('полученный адрес картинки', img_str)
            html = '<img class="alignnone size-medium wp-image-29881" src="' + img_str + '"/>'
        elif tag.name == 'iframe':
            print(tag, ' ---> ')
            html = str(tag)
        else:
            print('тег не найден')
    except:
        print('какая то ошибка с тегами')
    return html
