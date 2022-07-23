from os import listdir as lis
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, Template
from markdown_it import MarkdownIt

# jinja env
env = Environment(loader=FileSystemLoader("tpl"))

# read and write files
def readit(f):
    with open(f, "r") as file:
        my_content = file.read()
    return my_content

def writeit(f, c):
    with open(f, "w") as file:
        my_content = file.write(c)
    return my_content

# markdown a post
def marks(p):
    p = readit(f"posts/{p}")
    md = MarkdownIt("commonmark")
    return md.render(p)

# list posts
def allposts():
    posts = []
    for p in lis("./posts"):
        if p.endswith(".md"):
            posts.append(p)
    return posts

# Render posts
i_tpl = env.get_template("index.html")
p_tpl = env.get_template("posts.html")
posts = allposts()
htmls = []
for p in posts:
    html = p.replace(p[len(p) - 2:], "html")
    htmls.append(html)
    title = p[:-3].capitalize()
    # render posts
    dest = f"build/{html}"
    writeit(dest,p_tpl.render(title=title, content=marks(p)))

# render index as a posts list
writeit("build/index.html", i_tpl.render(title="My site", links=htmls))
