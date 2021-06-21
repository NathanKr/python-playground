import ujson


obj = [1,True, {'key1':1,'key2':2,'key3':3}]

json_obj = ujson.dumps(obj) # encode
print(f'json_obj : {json_obj}')

back_obj = ujson.loads(json_obj)
print(f'obj : {back_obj}')

print(f'obj == back_obj : {obj == back_obj}')
