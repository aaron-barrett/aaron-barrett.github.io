from yattag import Doc
from yattag import indent

doc, tag, text, line = Doc().ttl()
doc.asis('<!DOCTYPE html>')
with tag('html', lang="en"):
    with tag('head'):
        doc.stag('meta', charset="UTF-8")
        doc.stag('link', rel="stylesheet", href="styles.css")
    with tag('div', klass = "topnav"):
        with tag('a', klass = "active", href="index.html"):
            text("Home")
        with tag('a',href="math.html"):
            text("Math")
        with tag('a', href="about.html"):
            text("About")
    with tag('body'):
        with tag('main'):
            with tag('h1'):
                text("Welcome to my Website!")
            with tag('div', id = "main_page"):
                text("Welcome to my website! The only tab that has content now is the math tab, and it does not have much. This is intentional. The goal of this website is to talk about things that interest me such as mathematics, music theory, and possibly programming, and the focus will be mathematics, for now. While this could be thought of as a display of self-promotion, it is not self-aggrandizing; this is not a blog, and it never will be.")
f = open("index.html",'w')
print(indent(doc.getvalue()), file=f)
# print(doc.getvalue())