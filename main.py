word = input("Enter the word of which you want to find the acronym:\n")
acronym = word.split()
for items in acronym:
    print(items[0],end="")