#pset 2 - camel
def main():
    camelCase = input ("camelCase: ").strip()
    snake_case = "".join("_" + c.lower() if c.isupper() else c for c in camelCase)
    print ("snake_case:", snake_case)

main()