class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for idx in range(len(word)):
            if word[idx] not in curr.children:
                return False
            curr = curr.children[word[idx]]
            if idx == len(word) - 1 and curr.endOfWord:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for idx in range(len(prefix)):
            if prefix[idx] not in curr.children:
                return False
            curr = curr.children[prefix[idx]]
        return True
        