
def parse_html(html_str, open_tag_callback, data_callback, close_tag_callback):
    i = 0
    # Список для открытых тегов
    list_teg = []
    while html_str.find('<', i) != -1:
        i = html_str.find('<', i)
        # Обработка открывающего тега
        if html_str[i+1] != '/':
            j = html_str.find('>', i)
            open_tag_callback(html_str[i:j+1])
            list_teg.append([html_str[i:j+1], j+1])
            i = j
        # Обработка закрывающего тега и текста между тегами
        else:
            j = html_str.find('>', i)
            teg_now = '<' + html_str[i+2:j+1]
            for k in range(len(list_teg)-1, -1, -1):
                if list_teg[k][0] == teg_now:
                    data_callback(html_str[list_teg[k][1]:i])
                    del list_teg[k]
                    break
            close_tag_callback(html_str[i:j+1])
            i = j
    # Тут я вызываю функцию обработчик текста в случае, если так и не был встречен закрывающий тег
    # Возможно этого не надо было делать, я просто думвлв так учесть, что бывают только открывающие теги
    if list_teg:
        for teg in list_teg:
            data_callback(html_str[teg[1]:])


# Функция для тестирования через mock
def foo(s):
    print(s)
