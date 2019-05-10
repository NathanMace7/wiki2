from django import template
import markdown
import re

wikiWord = re.compile(r"\[\[([A-Za-z0-9_]+)\]\]")

register = template.Library()


@register.filter
def markup(text):
    return markdown.markdown(text)


@register.filter
def wikify(text):
    return wikiWord.sub(r'''
    <a href="/wiki/\1/">\1</a>
    ''', text)
