import pickle
data={'name':'youssef','id':1}
with open('data.pickle','wb') as f1:
    pickle.dump(data,f1)
    print('Pickling Completed.')
with open('data.pickle','rb') as f2:
    data=pickle.load(f2)
    print(data)
    print('UnPickling completed')

"""
Pickle Module: It is another way to serialize and deserialize Python objects.
It serializes the Python object in a binary format, due to which it is not human-readable. 
It is faster and it also works with custom-defined objects. 
The Python pickle module is a better choice for serialization and deserialization of python objects.
If you don’t need a human-readable format or if you need to serialize custom objects then it is recommended to use the pickle module. 
"""