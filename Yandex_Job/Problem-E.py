

class TrieNode:
    def __init__(self):
        self.children = {}
        self.popularity = -1 


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, popularity):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.popularity = max(node.popularity, popularity)

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return -1  
            node = node.children[char]

        return self._max_popularity(node)

    def _max_popularity(self, node):
        max_pop = node.popularity  
        for child in node.children.values():
            max_pop = max(max_pop, self._max_popularity(child))
        return max_pop


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N, Q = map(int, data[0].split())
    trie = Trie()

    for i in range(1, N + 1):
        word, popularity = data[i].rsplit(maxsplit=1)
        popularity = int(popularity)
        trie.insert(word, popularity)

    current_string = ""
    results = []

    for i in range(N + 1, N + Q + 1):
        command = data[i]
        if command[0] == '+':
            _, c = command.split()
            current_string += c
        elif command[0] == '-':
            current_string = current_string[:-1]

        result = trie.autocomplete(current_string)
        results.append(result)

    sys.stdout.write("\n".join(map(str, results)) + "\n")


if __name__ == "__main__":
    main()







class TrieNode:
    def __init__(self):
        self.children = {}
        self.max_popularity = -1 
        self.index_of_max = -1  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, popularity, index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if popularity > node.max_popularity:
                node.max_popularity = popularity
                node.index_of_max = index

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return -1  
            node = node.children[char]
        
        return node.index_of_max 

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N, Q = map(int, data[0].split())
    trie = Trie()

    for i in range(1, N + 1):
        word, popularity = data[i].rsplit(maxsplit=1)
        popularity = int(popularity)
        trie.insert(word, popularity, i - 1)  

    current_string = ""
    results = []

    for i in range(N + 1, N + Q + 1):
        command = data[i]
        if command[0] == '+':
            _, c = command.split()
            current_string += c
        elif command[0] == '-':
            current_string = current_string[:-1]

        result = trie.autocomplete(current_string)
        results.append(result)

    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
