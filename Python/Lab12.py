
sentence = input("Enter a sentence: ")


words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

vowel_letters = "aeiouAEIOU"

for ch in sentence:
    if ch in vowel_letters:
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

total_characters = len(sentence)
total_letters = vowels + consonants

if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0


print("=" * 37)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 37)
print(f"Sentence: {sentence}")
print(f"Total characters: {total_characters}")
print()
print("--- Character Breakdown ---")
print(f"Words: {words}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special characters: {special}")
print()
print("--- Summary ---")
print(f"Total Letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")
print()
print("=" * 37)
print("Analysis Complete!")
print("=" * 37)