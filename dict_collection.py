inverse_vocab = {0: '<pad>', 1: 'the', 2: 'wide',
                 3: 'road', 4: 'shimmered', 5: 'in', 
                 6: 'hot', 7: 'sun'}

# iterate dict
for item in inverse_vocab.items():
    print(item)


for key,value in inverse_vocab.items():
    print(key,value)


# iterate keys
for key in inverse_vocab.keys():
    print(key)


# iterate value
for value in inverse_vocab.values():
    print(value)


# add value      
inverse_vocab['key1']='value1'           