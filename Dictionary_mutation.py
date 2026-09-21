def add_entry(d):
    d["age"] = 25
    print("Inside add_Entry:", d)

def reassign_dict(d):
    d = {"name": "Bob", "age": 30}
    print("Inside reassign_dict:", d)


my_dict={"name": "Alice", "age": 20}
print("Before add_entry:", my_dict)

add_entry(my_dict)
print("After add_entry:", my_dict)

reassign_dict(my_dict)
print("After reassign_dict:", my_dict)

