

object = ['car', 'table', 'cup', 'door', 'tv','ball']
color = ['blue', 'red', 'purple', 'black', 'green']

if len(object) == len(color):
    for i in range(len(object)):
        object_name = object[i]
        color_name = color[i]
        print(f"My {object_name} is {color_name}.")
else:
    print("Lists don't match")