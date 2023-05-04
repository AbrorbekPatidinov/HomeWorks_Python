# only for practice, no need to check !


def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one = {
    'name': 'Abror',
    'age': 16,
    'phone_number': 998905703302,
}

new_person = increase_person_age(person_one)
print(id(new_person))
print(id(person_one))
print(new_person['age'])
print(person_one['age'])

