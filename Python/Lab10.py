

print("=" * 40)
print(f"{'TEXT PROCESSING TOOL':^40}")
print("=" * 40)

sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

pos = int(input("Enter position for indexing: "))
if 0 <= pos < len(sentence):
    print(f"Character at position {pos}  : '{sentence[pos]}'")
else:
    print(f"Character at position {pos}  : Index out of range")

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
print(f"Sliced string [{start}:{end}]  : '{sentence[start:end]}'")
print(f"Uppercase                 : {sentence.upper()}")
print(f"Lowercase                 : {sentence.lower()}")


old_word = input("Enter word to replace       : ")
new_word = input("Enter replacement word      : ")
new_sentence = sentence.replace(old_word, new_word)
print(f"After replace             : {new_sentence}")
print(f"Length of sentence        : {len(sentence)}")
print("\n" + "=" * 40)
print("Analysis Complete!")
print("=" * 40)


