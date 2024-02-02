class TrieNode:
    """A node in the Trie data structure.

    Each TrieNode represents a character in a word. It contains a dictionary
    of its children nodes, representing the next characters in the word, and
    a boolean flag indicating whether the current node represents the end of a word.
    """

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    """
    A Trie data structure implementation.

    The Trie data structure is used for efficient retrieval of strings.
    It allows for fast insertion, deletion, and searching of words.

    Attributes:
        root (TrieNode): The root node of the Trie.

    Methods:
        add(word): Inserts a word into the Trie.
        search(word): Searches for a word in the Trie.

    Example:
        trie = Trie()
        trie.add("apple")
        trie.add("banana")
        trie.search("apple")  # Returns True
        trie.search("orange")  # Returns False
    """

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to be inserted into the Trie.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        """
        Searches for a word in the Trie.

        Args:
            word (str): The word to be searched in the Trie.

        Returns:
            bool: True if the word is found in the Trie, False otherwise.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def starts_with(self, prefix):
        """
        Searches for a prefix in the Trie.

        Args:
            prefix (str): The prefix to be searched in the Trie.

        Returns:
            bool: True if the prefix is found in the Trie, False otherwise.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
