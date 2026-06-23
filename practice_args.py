def name(n):
    if len(n) % 2 != 0:
        return n[0]
    else:
        return "even"

print(name("kapil"))   # 5 letters → odd → 'k'
print(name("rajiv"))   # 5 letters → 'r'
print(name("sanjiv"))  # 6 letters → even → 'even'



def check_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if word[0].lower() in vowels:
        return "word "+ word[0]
    else:
        return "not vowel start "+ word[0]

print(check_word("kapil"))  # not vowel start
print(check_word("apple"))  # word