# How to use json with python

If you are building an API using python like I'm doing now you will certainly need to learn how to use json with python. When you receive data from an endpoint you need to convert it to a class usually, and when you are sending data from an API you need to transform it into json before sending it. Here are some scenarios that probably will happen and we need to know how to handle.

First lets get a dictionary to work on: 

```python
person = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

## dict -> json (serializing)
```python
person_json = json.dumps(person)  # or json.dumps(person_dict, indent=4)
print(person_json)
print(type(person_json))
```

## json -> dict (deserializing)
```python
person_dict = json.loads(person_json)
print(person_dict)
print(type(person_dict))
```

Lets define a class to work on the next examples:
```python

class Partner:
    def __init__(self, name) -> None:
        self.name = name

    def reprJSON(self):
        return dict(name=self.name)


class Company:
    def __init__(self, name: str, partner: Partner) -> None:
        self.name = name
        self.partner = partner

    def reprJSON(self):
        return dict(name=self.name, partner=self.partner)


class Person:
    def __init__(self, age: int, languages: dict, company: Company) -> None:
        self.age = age
        self.languages = languages
        self.company = company

    def reprJSON(self):
        return dict(age=self.age, languages=self.languages, company=self.company)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            json.JSONEncoder.default(self, obj)

john = Person(28, {
    "first": "portuguese",
    "second": "english"
}, Company("Itau", Partner("BB")))
```

## class -> json
```python
personclass_json = json.dumps(john.reprJSON(), cls=ComplexEncoder)
print(personclass_json)
print(type(personclass_json))
```

## json -> class
```python

```