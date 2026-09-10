#pset2-twtter
#to remove the vowels from a given input.
vowels = "aeiou"
Input = input("Enter a string: ").strip()
output = ""
for char in Input:
    if char.lower() in vowels:
        continue
    output += char

print (output)



