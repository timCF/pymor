import sys
import json
import pymorphy2
from pipe import * 
@Pipe
def to_set(x): return set(x)
@Pipe
def encode(x): return json.dumps(x, ensure_ascii=False)
morph = pymorphy2.MorphAnalyzer()
map(lambda x: map(lambda p: map(lambda w: w.word, p.lexeme), morph.parse(x)), (sys.argv | skip(1))) | traverse | as_list | to_set | as_list | encode | stdout