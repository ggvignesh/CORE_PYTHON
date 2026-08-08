#5. Write a function create_html_tag(tag, **attributes) that prints: <tag key='val' ...>. Example: create_html_tag('a', href='https://python.org', target='_blank')
def create_html_tag(tag, **attributes):
    html = "<" + tag
    for key, value in attributes.items():
        html += f" {key}='{value}'"
    html += ">"
    print(html)

create_html_tag("a",href="https://python.org",target="_blank")