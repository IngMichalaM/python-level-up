# count the numbers of unique words and how often they occur
# ignore case

from collections import Counter


def count_word(file_name: str, top_words: int = 20, length_limit=1):
    print('-------------- Include everything --------------')
    with open(file_name, 'r') as file:
        text = file.read().lower()
        words = text.split()

    word_count = Counter(words)

    print(f"There are {len(words)} words in the file.")
    print(f"There are {len(word_count)} unique words in the file.")
    print(f"The {top_words} most often words are:")

    for word, count in word_count.most_common(top_words):
        print(f"{word:<15}{count}")

    print(f'-------------- Only include words longer or equal to {length_limit} letters --------------')

    with open(file_name, 'r') as file:
        text = file.read().lower()
        words = text.split()
        longer_words = [word for word in words if len(word) >= length_limit]

    word_count = Counter(longer_words)

    print(f"There are {len(longer_words)} words in the file.")
    print(f"There are {len(longer_words)} unique words in the file.")
    print(f"The {top_words} most often words are:")

    for word, count in word_count.most_common(top_words):
        print(f"{word:<15}{count}")


count_word('text_for_counting.txt', 20, 4)
