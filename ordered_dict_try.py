from collections import OrderedDict

ordered_dict = OrderedDict()
print(f'type(ordered_dict) : {type(ordered_dict)}')
print(f'isinstance(ordered_dict,OrderedDict) : {isinstance(ordered_dict,OrderedDict)}')

# add values
ordered_dict['key1']=1
ordered_dict['key2']=2
ordered_dict['key1'] += 1
ordered_dict['key2'] += 2

# iterate
for key,value in ordered_dict.items():
    print(f'key : {key} , value : {value}')
