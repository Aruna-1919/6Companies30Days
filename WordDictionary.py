class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_helper(self, word: str, node: TrieNode) -> bool:
        for i, char in enumerate(word):
            if char == '.':
                for child in node.children.values():
                    if self.search_helper(word[i+1:], child):
                        return True
                return False
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root)

