# -*- coding: utf-8 -*-
"""Insertion in Tries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uLKU87CdulxM9CU8EduOCZTU5sbAnPAL
"""

class TrieNode:
    def __init__(self):
        self.children  = {}
        self.enfofString = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertString(self,word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node =  TrieNode()
                current.children.update({ch:node})
            current = node
        current.endofString = True
        print("Successfully Inserted")
newTrie = Trie()
newTrie.insertString(input())
newTrie.insertString(input())

# Time Complexity - O(m)
# Space Complexity - O(m)
# Where m is the length of word that we are trying to insert