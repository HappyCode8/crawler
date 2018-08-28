__author__ = 'wyj'
import json

j= [{"name":"我们", "age":23}]
k= [{"name":"它们", "age":34}]
with open("..\\file\\test.json", "a", encoding='utf-8') as f:
    f.write(','+json.dumps(k, indent=4,ensure_ascii=False)[1:-1])