import lxml.html

parser = lxml.html.parse('input.html')

all_links = parser.findall('//a')

for idx, val in enumerate(all_links):
    print(idx, val.__class__.__name__, val.text)
