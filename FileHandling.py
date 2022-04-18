class FileHandling():
    def longest_word(filename):
        with open(filename, 'r') as infile:
            words = infile.read().split()
        max_len = len(max(words, key=len))
        # OR
        max_len = max(len(w) for w in words)
        return [word for word in words if len(word) == max_len]

    print(longest_word('samplefile.txt'))