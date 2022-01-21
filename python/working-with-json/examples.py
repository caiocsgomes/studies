import json
from mimetypes import init

person_dict = {
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

# dict to json string (serializing)
person_json = json.dumps(person_dict)  # or json.dumps(person_dict, indent=4)
print(person_json)
print(type(person_json))


# json string to dict (deserializing)
person_dict = json.loads(person_json)
print(person_dict)
print(type(person_dict))


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


# class to json
personclass_json = json.dumps(john.reprJSON(), cls=ComplexEncoder)
print(personclass_json)
print(type(personclass_json))

# json to class
