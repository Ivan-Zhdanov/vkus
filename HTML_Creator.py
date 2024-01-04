def html_creator(list_cort):
    html = ''
    for h2, tags in list_cort:
        html = html + '<h2>'+h2 +'</h2>'+ tags
    return html