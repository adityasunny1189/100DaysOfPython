# Error and Exception handling

# try:
#     with open('data.txt', 'r') as file:
#         file.read()
# except FileNotFoundError:
#     print('file not found')
# except KeyError:
#     print('invalid key pressed')
# finally:
#     print('this is finally block')


# fruits = ["Apple", "Pear", "Orange"]
#
#
# def get_fruit_cake(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit, "pie")
#
#
# get_fruit_cake(2)
# get_fruit_cake(4)


# Likes Comments Share

facebook_posts = [
    {"Likes": 21, "Comments": 4},
    {"Likes": 12, "Comments": 6, "Share": 2},
    {"Likes": 32, "Comments": 31, "Share": 5},
    {"Comments": 34, "Share": 9},
    {"Comments": 1},
    {"Share": 45}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        pass

print(total_likes)



























