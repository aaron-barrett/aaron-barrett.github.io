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
                text("Hi. I am Aaron Barrett, like the website. I recently obtained my Master's of Mathematics from the University of Kansas in May 2022, and I was a music performance major for one of my undergraduate degrees along with mathematics. The goal of this website is a small, potentially unwanted platform to share fun math results, and the focus will be on computational mathematics and numerical linear algebra. Other concepts may creep in such as music theory or programming paradigms, but they also may not. This is not a blog, however, and never will be. Enjoy!")
f = open("about.html",'w')
print(indent(doc.getvalue()), file=f)
# print(doc.getvalue())