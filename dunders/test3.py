class Word(str):
    """Define string comparison based on word length."""
    def __new__(cls, word):
        # str is immutable, so we must use __new__ to initialize it at creation
        if " " in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(" ")]

            # Word is now all chars before first space
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
