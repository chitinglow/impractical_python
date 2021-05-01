"""Find palinromes (leter panlingrams) in a dictionary file."""

import load_dictionary
word_list = load_dictionary.load(r'C:\Users\ctlow\Dropbox\python_project\impractical_python\dictionary\International\2of4brif.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindroms found = {}\n".format(len(pali_list)))
print(*pali_list, sep="\n")