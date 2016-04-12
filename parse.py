import lxml.html

parser = lxml.html.parse('input.html')

all_links = parser.findall('//a')  # list of lxml.html.HtmlElement objects

for idx, a in enumerate(all_links):
    print(idx, a.text, a.get('href'))
