N = int(input())
colors = input().split()


def hina_arare(colors):
    for color in colors:
        if color == "Y":
            return "Four"
    return "Three"


print(hina_arare(colors))
