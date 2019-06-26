from django import template
import markdown
import re

#When creating a page on the Wiki, these are the only characters you can use
wikiWord = re.compile(r"\[\[([A-Za-z0-9_]+)\]\]")
register = template.Library()

#Implements Markdown 
@register.filter
def markup(text):
    return markdown.markdown(text)

#Sets up the URL path, but excludes '/wiki/'
@register.filter
def wikify(text):
    return wikiWord.sub(r'''
    <a href="/wiki/\1/">\1</a>
    ''', text)
