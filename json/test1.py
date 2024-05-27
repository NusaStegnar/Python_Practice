import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Nick"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

print(json.dumps(x, indent=4))

# {
#     "name": "John",
#     "age": 30,
#     "married": true,
#     "divorced": false,
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "pets": null,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ]
# }

print(json.dumps(x, indent=4, separators=(". ", " = ")))

# {
#     "name" = "John".
#     "age" = 30.
#     "married" = true.
#     "divorced" = false.
#     "children" = [
#         "Ann".
#         "Billy"
#     ].
#     "pets" = null.
#     "cars" = [
#         {
#             "model" = "BMW 230".
#             "mpg" = 27.5
#         }.
#         {
#             "model" = "Ford Edge".
#             "mpg" = 24.1
#         }
#     ]
# }

print(json.dumps(x, indent=4, sort_keys=True))

# {
#     "age": 30,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ],
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "divorced": false,
#     "married": true,
#     "name": "John",
#     "pets": null
# }