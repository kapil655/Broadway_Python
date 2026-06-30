def name(n):
    if len(n) % 2 != 0:
        return n[0]
    else:
        return "even"

print(name("kapil"))   
print(name("rajiv"))   
print(name("sanjiv"))  



def check_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if word[0].lower() in vowels:
        return "word "+ word[0]
    else:
        return word[0] + " isn't vowel word "

print(check_word("kapil"))   # not vowel start
print(check_word("apple"))  # word