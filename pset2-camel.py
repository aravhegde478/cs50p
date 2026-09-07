#pset 2 - camel
def main():
    camel_case = input("camelCase: ").strip()
    print("snake_case: ", end="")
    change_format(camel_case)

def change_format(word):
    for letter in word:
        if letter.isupper():
            print (f"_{letter.lower()}", end = "")
        else:
            print (letter, end = "")
    print()

main()