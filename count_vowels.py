def count_vowel(text):
    vowels=["a","e","i","o","u"]
    vowel_count=0
    for character in text.lower():
        if character in vowels:
            vowel_count+=1
    return vowel_count

print(count_vowel("omondi"))