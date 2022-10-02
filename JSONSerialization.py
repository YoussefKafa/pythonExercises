import json
students='{"id":"1","name":"youssef"}'
#convert string to python dict
# serialization
student_dict=json.loads(students)
print(student_dict)

#deserialization
print(student_dict['name'])


"""
JSON is a widely used format for data exchange and it is very convenient.
It is human-readable and language-independent, and it’s lighter than XML.
"""