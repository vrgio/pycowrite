# Pycowrite

Very *very* small site generator (less than 50 LOC).

Create markdown files and let it convert it to html. It does nothing more than that.

## Dependencies:
- [Jinja2](https://pypi.org/project/Jinja2/)
- [markdown-it-py](https://pypi.org/project/markdown-it-py/)

## Usage:

+ Install requirements `pip install -r requirements.txt`
+ Create markdown files inside `posts` directory
+ Throw static files (css, js, pics) anywhere in the `build` dir
+ Optionally edit templates in `tpl` directory
+ Run `python pycowrite.py`
+ Generated static site is in `build` directory

## Netlify:

**Basic build settings**

+ Build command: `python pycowrite.py`
+ Publish directory: `build`

## Credits:
CSS from [Milligram](https://milligram.io/)
