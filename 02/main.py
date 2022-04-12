
def parse_html(html_str, open_tag_callback, data_callback, close_tag_callback):
    i = 0
    list_teg = []
    while html_str.find('<', i) != -1:
        i = html_str.find('<', i)
        if html_str[i+1] != '/':
            j = html_str.find('>', i)
            open_tag_callback(html_str[i:j+1])
            list_teg.append([html_str[i:j+1], j+1])
            i = j
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
    if list_teg:
        for teg in list_teg:
            data_callback(html_str[teg[1]:])


def foo(s):
    print(s)
