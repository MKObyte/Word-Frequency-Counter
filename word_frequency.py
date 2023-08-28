from collections import Counter
import re
import sys

def word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = re.findall(r'\w+', text.lower())
        word_counts = Counter(words)
        most_common = word_counts.most_common()
        return most_common

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    top_words = word_frequency(input_file)
    
    print("Top words:")
    for word, count in top_words:
        print(f"{word}: {count}")
