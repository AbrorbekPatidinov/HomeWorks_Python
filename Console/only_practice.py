# only for practice, no need to check !

from functools import reduce

# list_prog_languages = ['Python', 'C/C++', 'PHP', 'JavaScript', 'Assembler']
# print("Programming languages in list type: ")
# print(type(list_prog_languages))
# print(f"Length of the list named 'list_prog_languages': {len(list_prog_languages)}")
# list_prog_languages.append("C#")
# list_prog_languages.insert(6, "Swift")
# list_prog_languages.remove("Python")
# list_prog_languages.pop(3)
# print(f"Index of 'C/C++' in prog languages list : {list_prog_languages.index('C/C++')}")
# print(f"Count of prog language: {list_prog_languages.count('PHP')}")
# # list_prog_languages.sort()
# # list_prog_languages.reverse()
# for list_prog_lang in list_prog_languages:
#     print(list_prog_lang)


# tuple_prog_languages = ('Ruby', 'Delphi', 'Java', 'HTML', 'CSS')
# print("Programming languages in tuple type:")
# print(type(tuple_prog_languages))
# print(f"Length of the tuple named 'tuple_prog_languages': {len(tuple_prog_languages)}")
# print(f"Index of 'Ruby' in prog languages tuple: {tuple_prog_languages.index('Ruby')}")
# print(f"Count of 'Java' in prog languages tuple: {tuple_prog_languages.count('Java')}")
# for tuple_prog_lang in tuple_prog_languages:
#     print(tuple_prog_lang)


# set_prog_languages = {'Kotlin', 'Elixir', 'Carbon', 'TypeScript', 'Rust'}
# print("Programming languages in SET type")
# print(type(set_prog_languages))
# print(f"Length of the SET prog languages: {len(set_prog_languages)}")
# set_prog_languages.add("Objective-C")
# set_prog_languages.remove("Objective-C")
# set_prog_languages.discard("Elixir")
# set_prog_languages.pop()
# set_prog_languages.clear()
# for set_prog_lang in set_prog_languages:
#     print(set_prog_lang)


# dict_prog_languages = {'low_level': 'binary code, machine language', 'middle_level': 'Assembly, C/C++',
#                        'high_level': 'Python, Java'}
# dict_mock_prog_languages = {'super_level': '???, ???'}
# print("Programming languages in dict type")
# print(type(dict_prog_languages))
# print(f"Length of the dict prog languages: {len(dict_prog_languages)}")
# print(f"Key of 'binary code, machine language' is: {dict_prog_languages['low_level']}")
# print(f"The 'middle_level' key includes: {dict_prog_languages.get('middle_level')}")
# print(f"All keys in dict prog languages: {dict_prog_languages.keys()}")
# print(f"All values in dict prog languages: {dict_prog_languages.values()}")
# print(f"Items in dict prog languages: {dict_prog_languages.items()}")
# dict_prog_languages.pop('low_level')
# # dict_prog_languages.popitem() - deletes random key in the dict
# dict_prog_languages.update(dict_mock_prog_languages)
# for dict_prog_lang in dict_prog_languages:
#     print(dict_prog_lang)


list1 = [1, 2, 3, 4, 5]
squared = list(map(lambda num: num ** 2, list1))
print(squared)


