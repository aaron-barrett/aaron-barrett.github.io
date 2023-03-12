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
                text("Below are expositions.")
            with tag('ul'):
                with tag('li'):
                    # TODO: Possibly iterate this process for when there are many subpages
                    # That might be here, that might be in the main run.py
                    # Question: Best way to automate name generation below. Might not be automated.
                    with tag('a', href = "math\html\math_subpage_test.html"):
                        text("Two HW Questions")
f = open("math.html",'w')
print(indent(doc.getvalue()), file=f)
# print(doc.getvalue())