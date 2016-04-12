import re
import lxml.html

IS_EPISODE = re.compile('Episodio (\d{1,3})')

parser = lxml.html.parse('input.html')

all_links = parser.findall('//a')  # list of lxml.html.HtmlElement objects

for idx, a in enumerate(all_links):
    matches = IS_EPISODE.findall(a.text)
    if matches:
        print(idx, matches, a.text, a.get('href'))
