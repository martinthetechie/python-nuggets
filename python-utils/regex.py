import re

class RegexHelper:
    """
    Function to handle all regex related functions.
    """
    @staticmethod
    def find_all(pattern, text):
        """Find all occurrences of a pattern in the given text."""
        return re.findall(pattern, text)

    @staticmethod
    def find_first(pattern, text):
        """Find the first occurrence of a pattern in the given text."""
        match = re.search(pattern, text)
        return match.group() if match else None

    @staticmethod
    def match(pattern, text):
        """Check if the entire text matches the pattern."""
        return re.fullmatch(pattern, text) is not None

    @staticmethod
    def substitute(pattern, replacement, text):
        """Replace all occurrences of the pattern in the text with the replacement."""
        return re.sub(pattern, replacement, text)