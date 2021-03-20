import re
from django import template

BANNED_WORDS = ['сиськи', 'жопы', 'письки']

register = template.Library()


@register.filter(name='censor')
def censor(text, derivatives=False):
    def asteriskify(matchobj):
        word = matchobj[0]
        return word[0] + '*' * (len(word)-2) + word[-1]

    censored_text = text
    for banned_word in BANNED_WORDS:
        censored_text = re.sub(
            banned_word
            if derivatives else rf'(^|(?<=\W)){banned_word}((?=\W)|$)',
            asteriskify,
            censored_text,
            flags=re.IGNORECASE
        )
    return censored_text
