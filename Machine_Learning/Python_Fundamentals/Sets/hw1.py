info = {
    ("Alice","Maths"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Maths"),
    ("Bob","Maths"),
    ("Alice","English"),
    ("Charlie","English"),
}

unique_names = set()
unique_courses = set()

# for name,course in info:
#     unique_names.add(name)
#     unique_courses.add(course)
#     if(course=="English"):
#         print(name)

# print(unique_names)
# print(unique_courses)

dict = {}
for name,course in info:
    if(dict.get(name) == None):
        dict.update({
            name : set(),
        })
        dict[name].add(course)
    else:
        dict[name].add(course)


print(dict)