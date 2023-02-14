from yattag import Doc
from yattag import indent

doc, tag, text, line = Doc().ttl()
doc.asis('<!DOCTYPE html>')
with tag('html', lang="en"):
    with tag('head'):
        doc.stag('meta', charset="UTF-8")
        doc.stag('link', rel="stylesheet", href="styles.css")
    with tag('div', klass = "topnav"):
        with tag('a',  href="index.html"):
            text("Home")
        with tag('a',href="math.html"):
            text("Math")
        with tag('a', klass = "active", href="about.html"):
            text("About")
    with tag('body'):
        with tag('main'):
            with tag('h1'):
                text("Welcome to About!")
            with tag('div', id = "main_page"):
                text("Text in about")
f = open("about.html",'w')
print(indent(doc.getvalue()), file=f)
# print(doc.getvalue())