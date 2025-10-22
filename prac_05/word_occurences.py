"""
Word occurrences prac_05
Input a string
Count the number of times each word appears
Estimate: 25mins
Actual: 30mins
"""

def main():
    words = input("Text: ").lower()
    words = words.split()
    # print(count_words(words))
    word_to_count = count_words(words)
    max_length = max(len(word) for word in list(word_to_count.keys()))
    word_to_count = dict(sorted(word_to_count.items()))
    for word, count in word_to_count.items():
        print(f"{word:{max_length}} : {count}")

def count_words(words):
    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
    return word_to_count

main()
