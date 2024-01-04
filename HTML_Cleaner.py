
def html_cleaner(html):
    t1 = html.replace("«»»", "").replace('"""', "")
    t2 = t1.replace("&lt;/li&gt;", "")
    t3 = t2.replace("&lt;li&gt;", "")
    t4 = t3.replace("Перепиши с дополнением оставляя html теги:", "")
    t5 = t4.replace("»»»", "")
    t6 = t5.replace("«»»", "")
    cl_html = t6.strip('"')
    return cl_html