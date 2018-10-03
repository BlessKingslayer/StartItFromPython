from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <div class='xxx'>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            </div>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
for i, content in enumerate(soup.p.contents):
    print(i, content)

print(type(soup.p.contents))
print(type(soup.p.children))
print(type(soup.a.parent))
print(soup.a.parent)
print(type(soup.p.descendants))
print(type(soup.p.parents))
print('-' * 30, '所有祖先节点', '-' * 30)
print(list(enumerate(soup.a.parents)))