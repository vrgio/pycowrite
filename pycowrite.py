from os import listdir as lis
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, Template
from markdown_it import MarkdownIt

# jinja env
env = Environment(loader=FileSystemLoader("tpl"))

def read_file(f):
    """Read the contents of a file."""
    with open(f, "r") as file:
        return file.read()

def write_file(f, c):
    """Write content to a file."""
    with open(f, "w") as file:
        file.write(c)

def render_markdown(p):
    """Render Markdown content to HTML."""
    content = read_file(f"posts/{p}")
    md = MarkdownIt("commonmark")
    return md.render(content)

def list_markdown_posts():
    """List all Markdown posts in the 'posts' directory."""
    posts = [p for p in lis("./posts") if p.endswith(".md")]
    return posts

def generate_html(post):
    """Generate HTML for a post."""
    html_filename = post.replace(".md", ".html")
    title = post[:-3].capitalize()
    html_content = render_markdown(post)
    return html_filename, title, html_content

def generate_site():
    """Generate the static site."""
    posts = list_markdown_posts()
    htmls = []

    # Generate HTML for each post
    for post in posts:
        html_filename, title, content = generate_html(post)
        htmls.append(html_filename)

        # Write HTML content to file
        dest = f"build/{html_filename}"
        write_file(dest, p_tpl.render(title=title, content=content))

    # Generate index.html
    write_file("build/index.html", i_tpl.render(title="My site", links=htmls))

if __name__ == "__main__":
    i_tpl = env.get_template("index.html")
    p_tpl = env.get_template("posts.html")
    generate_site()
