def start_spring(**kwargs):
    info = {}
    for value, key in kwargs.items():
        if key not in info:
            info[key] = []
        info[key].append(value)

    sorted_info = sorted(info.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for collection, elements in sorted_info:
        result += f"{collection}:\n"
        for element in sorted(elements):
            result += f"-{element}\n"

    return result


# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

