from yattag import Doc
from yattag import indent

doc, tag, text, line = Doc().ttl()
doc.asis('<!DOCTYPE html>')
with tag('html', lang="en"):
    with tag('head'):
        doc.stag('meta', charset="UTF-8")
        doc.stag('link', rel="stylesheet", href="styles.css")
        with tag("title"):
            text("Math")
    with tag('div', klass = "topnav"):
        with tag('a', href="index.html"):
            text("Home")
        with tag('a', klass="active", href="math.html"):
            text("Math")
        with tag('a', href="about.html"):
            text("About")
    with tag('body'):
        with tag('main'):
            with tag('h1'):
                text("Welcome to Math!")
            with tag('div', id = "main_page"):
                text("Below are expositions of topics I found interesting enough to generate.")
            with tag('ul'):
                with tag('li'):
                    with tag('a', href = "math\html\math_subpage.html"):
                        text("Math Subpage Test")
f = open("math.html",'w')
print(indent(doc.getvalue()), file=f)
# print(doc.getvalue())