class Node:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, s):

        nd = self.root
        for i in range(len(s)):
            if nd.children[ord(s[i])-ord('a')]==None:
                nd.children[ord(s[i])-ord('a')] = Node()
            nd = nd.children[ord(s[i])-ord('a')]
        nd.isEndOfWord = True

    def search(self, s):

        nd = self.root
        for i in range(len(s)):
            if nd.children[ord(s[i])-ord('a')]==None:
                return False
            nd = nd.children[ord(s[i])-ord('a')]
        return nd.isEndOfWord

    def delete(self,s):

        nd = self.root
        for i in range(len(s)):
            if nd.children[ord(s[i])-ord('a')]==None:
                return
            nd = nd.children[ord(s[i])-ord('a')]
        nd.isEndOfWord = False


    def autoComplete(self, nd, prefix):
        if nd==None:
            return
        if nd.isEndOfWord:
            print(prefix)
        for i in range(26):
            self.autoComplete(nd.children[i], prefix + chr(i+ord('a')))

    def printAutoComplete(self, prefix):
        nd = self.root
        for chrr in prefix:
            if nd.children[ord(chrr)-ord('a')]==None:
                return
            nd = nd.children[ord(chrr)-ord('a')]
        self.autoComplete(nd, prefix)
        return


dict=Trie()

dict.insert("salam")
dict.insert("hello")
dict.insert("ola")
dict.insert("bonjour")
dict.insert("namaste")
dict.insert("salve")
dict.insert("hola")
dict.insert("sawubona")

print("\nAll words in the dictionsry: ")
dict.printAutoComplete("")
print(f'{" salam: ": <{10}}',dict.search("salam"))
print("sa..?")
dict.printAutoComplete("sa")

dict.delete("salam")
print("\nAll words in the dictionsry: ")
dict.printAutoComplete("")
print(f'{" salam: ": <{10}}',dict.search("salam"))
print("sa..?")
dict.printAutoComplete("sa")


