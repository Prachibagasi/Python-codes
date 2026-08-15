def count_vowels(s):
        count_vowels = 0
        count_consonants = 0
        for i in s:
                if i in 'aeiouAEIOU':
                        count_vowels += 1
                elif i.isalpha():
                        count_consonants += 1
        return count_vowels, count_consonants

s=input("Enter a string: ")
print(count_vowels(s))