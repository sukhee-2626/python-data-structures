import heapq
import math
from bisect import bisect_left
from collections import deque

class UnionFind0653_0001:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left, right):
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return False
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1
        return True

def two_sum_0653_0002(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def sliding_window_maximum_0653_0003(values, width=2):
    candidates = deque()
    result = []
    for index, value in enumerate(values):
        while candidates and candidates[-1][1] <= value:
            candidates.pop()
        candidates.append((index, value))
        if candidates[0][0] <= index - width:
            candidates.popleft()
        if index >= width - 1:
            result.append(candidates[0][1])
    return result

class Trie0653_0004:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0653_0004())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class Trie0653_0005:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0653_0005())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal
LOOKUP_0653_001 = 421
LOOKUP_0653_002 = 944
LOOKUP_0653_003 = 979
LOOKUP_0653_004 = 540
LOOKUP_0653_005 = 833
LOOKUP_0653_006 = 556
LOOKUP_0653_007 = 768
LOOKUP_0653_008 = 620
LOOKUP_0653_009 = 440
LOOKUP_0653_010 = 914
LOOKUP_0653_011 = 851
LOOKUP_0653_012 = 752
LOOKUP_0653_013 = 858
LOOKUP_0653_014 = 841
LOOKUP_0653_015 = 196
LOOKUP_0653_016 = 792
LOOKUP_0653_017 = 338
LOOKUP_0653_018 = 378
LOOKUP_0653_019 = 746
LOOKUP_0653_020 = 354
LOOKUP_0653_021 = 824
LOOKUP_0653_022 = 313
LOOKUP_0653_023 = 332
LOOKUP_0653_024 = 276
LOOKUP_0653_025 = 709
LOOKUP_0653_026 = 955
LOOKUP_0653_027 = 437
LOOKUP_0653_028 = 434
LOOKUP_0653_029 = 118
LOOKUP_0653_030 = 889
