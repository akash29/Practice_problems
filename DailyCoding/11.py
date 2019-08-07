class TrieNode(object):
    def __init__(self):
        self.node = [None] * 26

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []
    
    def add_words(self, word):
        self.start_node = self.root
        for i in range(len(word)):
            node = self.start_node.node
            char_index = ord(word[i]) - ord('a')
            if not node[char_index]:
                node[char_index] = TrieNode()
            self.start_node = node[char_index]

    def search_words(self, start_word):
        for i in range(len(start_word)):
            char_index = ord(start_word[i]) - ord('a')
            if self.root.node[char_index]:
                node = self.root.node[char_index]
                self.root = node
            else:
                return None
        return self.find_words(start_word)
    
    def find_words(self, start_w):
        for i in range(len(self.root.node)):
            temp_a = []
            if self.root.node[i] is not None:
                for p in start_w:
                    temp_a.append(p)
                temp_a.append(chr(97+i))
                self.dfs_util(self.root.node[i], temp_a)
                self.word_list.append(temp_a)
    
    def dfs_util(self, node, str_list):
        for i in range(len(node.node)):
            if node.node[i] is not None:
                temp = chr(97+i)
                str_list.append(temp)
                self.dfs_util(node.node[i], str_list)
                print(str_list)
                k = str_list.copy()
                self.word_list.append(k)
                str_list.pop()
        

                

        

dict_words = ["abcd","abd","ade"]
t = Trie()
for i in dict_words:
    t.add_words(i)
t.search_words("abc")
for k in t.word_list:
    temp_str = ''.join(k)
    if temp_str in dict_words:
        print(temp_str)
