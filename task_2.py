from trie import Trie, TrieNode


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if len(strings) == 0:
            return ""

        # Очищуємо дерево, щоб працювати лише з новим набором слів
        self.root = TrieNode()
        self.size = 0

        for word in strings:
            self.put(word, word)

        # Пошук найдовшого спільного префікса шляхом проходу по єдиному нащадку
        prefix = ""
        current = self.root
        while len(current.children) == 1 and current.value is None:
            char = next(iter(current.children))
            prefix += char
            current = current.children[char]
        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("Всі перевірки пройдено успішно.")
