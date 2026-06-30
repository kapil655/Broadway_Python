while True:
    i = 0
    count = 0
    found = False

    name = input("Enter a name: ")

    while i < len(name):
        ch = name[i]

        if ch in "aeiouAEIOU":
            count += 1
            found = True

        i += 1

    if found:
        print(f"Your name contains {count} vowel letter(s).")
    else:
        print("Name does not contain any vowel.")
        break