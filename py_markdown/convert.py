import markdown

with open('things.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('things.html', 'w') as f:
    f.write(html)