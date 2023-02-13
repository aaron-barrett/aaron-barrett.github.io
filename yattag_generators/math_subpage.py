from yattag import Doc
from yattag import indent

doc, tag, text, line = Doc().ttl()
doc.asis('<!DOCTYPE html>')
with tag('html', lang="en"):
    with tag('head'):
        doc.stag('link', rel="stylesheet", href="styles.css")
        with tag("title"):
            text("Math")
        doc.stag('link', rel='stylesheet', href='https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css', integrity='sha384-vKruj+a13U8yHIkAyGgK1J3ArTLzrFGBbBc0tDp4ad/EyewESeXE/Iv67Aj8gKZ0', crossorigin='anonymous')
        with tag('script', 'defer', src='https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js', integrity='sha384-PwRUT/YqbnEjkZO0zZxNqcxACrXe+j766U2amXcgMg5457rve2Y7I6ZJSm2A0mS4', crossorigin='anonymous'):
            text("")
        with tag("script", "defer", src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/contrib/auto-render.min.js", integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05", crossorigin="anonymous", onload="renderMathInElement(document.body);"):
            text("")
    with tag('div', klass = "topnav"):
        with tag('a', href="index.html"):
            text("Home")
        with tag('a', klass="active", href="math.html"):
            text("Math")
        with tag('a', href="about.html"):
            text("About")
    with tag('body'):
        with tag('main'):
            with tag('div', id = "prob_hw"):
                math_tex = open("../math/html/frag.html", "r")
                math_text_raw = math_tex.read()
                doc.asis(math_text_raw)
                math_tex.close()

f = open("math_subpage.html",'w')
print(indent(doc.getvalue()), file=f)
# print(doc.getvalue())