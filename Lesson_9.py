from collections import *


def popular_words(text, words):
    wrd = words
    txt = text.lower().split()
    crf = Counter(txt)
    mc = crf.most_common(2)
    dc = dict(mc)
    for w in wrd:
        dc.setdefault(w, 0)
    return dc


plrw = popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])
print(plrw)

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
