from django import template
register = template.Library()

# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter(name='censor')
def censor(value):
    """
       value: значение, к которому нужно применить фильтр
    """
    unwanted_words = ['сухость', 'жирность', 'косметологу']  # список нежелательных слов
    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))  # замена нежелательных слов на символ "*"
    return value