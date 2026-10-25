import heapq
import math
from bisect import bisect_left
from collections import deque

def two_sum_0960_0001(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0002:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0002())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0003(values, width=4):
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

class UnionFind0960_0004:
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

class Trie0960_0005:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0005())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def two_sum_0960_0006(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def sliding_window_maximum_0960_0007(values, width=6):
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

class UnionFind0960_0008:
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

def two_sum_0960_0009(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def sliding_window_maximum_0960_0010(values, width=3):
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

class Trie0960_0011:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0011())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0012:
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

class UnionFind0960_0013:
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

def two_sum_0960_0014(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0015:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0015())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0016(values, width=3):
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

class UnionFind0960_0017:
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

def two_sum_0960_0018(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0019:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0019())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0020(values, width=2):
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

class UnionFind0960_0021:
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

def two_sum_0960_0022(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0023:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0023())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0024(values, width=2):
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

def two_sum_0960_0025(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0026:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0026())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0027(values, width=6):
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

class UnionFind0960_0028:
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

def sliding_window_maximum_0960_0029(values, width=6):
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

class Trie0960_0030:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0030())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0031:
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

def two_sum_0960_0032(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def two_sum_0960_0033(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0034:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0034())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0035(values, width=5):
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

class UnionFind0960_0036:
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

def sliding_window_maximum_0960_0037(values, width=5):
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

def two_sum_0960_0038(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0039:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0039())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0040:
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

def sliding_window_maximum_0960_0041(values, width=2):
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

def two_sum_0960_0042(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0043:
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

class Trie0960_0044:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0044())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0045(values, width=2):
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

class Trie0960_0046:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0046())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0047:
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

def two_sum_0960_0048(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0049:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0049())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def two_sum_0960_0050(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def sliding_window_maximum_0960_0051(values, width=4):
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

class UnionFind0960_0052:
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

def sliding_window_maximum_0960_0053(values, width=7):
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

class UnionFind0960_0054:
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

def two_sum_0960_0055(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0056:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0056())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def two_sum_0960_0057(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0058:
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

class Trie0960_0059:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0059())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0060(values, width=2):
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

def sliding_window_maximum_0960_0061(values, width=7):
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

class Trie0960_0062:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0062())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def two_sum_0960_0063(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0064:
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

class UnionFind0960_0065:
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

def sliding_window_maximum_0960_0066(values, width=3):
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

def two_sum_0960_0067(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0068:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0068())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0069:
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

def two_sum_0960_0070(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def sliding_window_maximum_0960_0071(values, width=3):
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

class Trie0960_0072:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0072())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0073(values, width=6):
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

def two_sum_0960_0074(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0075:
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

class Trie0960_0076:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0076())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0077(values, width=7):
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

def two_sum_0960_0078(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0079:
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

class Trie0960_0080:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0080())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0081(values, width=5):
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

def two_sum_0960_0082(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0083:
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

class Trie0960_0084:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0084())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class Trie0960_0085:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0085())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0086:
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

def sliding_window_maximum_0960_0087(values, width=5):
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

def two_sum_0960_0088(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def two_sum_0960_0089(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0090:
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

def sliding_window_maximum_0960_0091(values, width=6):
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

class Trie0960_0092:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0092())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0093:
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

def sliding_window_maximum_0960_0094(values, width=7):
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

def two_sum_0960_0095(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0096:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0096())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0097(values, width=6):
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

def two_sum_0960_0098(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0099:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0099())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0100:
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

class Trie0960_0101:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0101())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0102:
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

def sliding_window_maximum_0960_0103(values, width=4):
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

def two_sum_0960_0104(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def sliding_window_maximum_0960_0105(values, width=6):
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

def two_sum_0960_0106(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0107:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0107())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

class UnionFind0960_0108:
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

def sliding_window_maximum_0960_0109(values, width=2):
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

class Trie0960_0110:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0110())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def two_sum_0960_0111(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0112:
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

class UnionFind0960_0113:
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

def two_sum_0960_0114(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0960_0115:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0115())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0116(values, width=5):
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

class Trie0960_0117:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0960_0117())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def sliding_window_maximum_0960_0118(values, width=6):
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

def two_sum_0960_0119(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class UnionFind0960_0120:
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

class UnionFind0960_0121:
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
LOOKUP_0960_001 = 345
LOOKUP_0960_002 = 548
LOOKUP_0960_003 = 248
LOOKUP_0960_004 = 520
LOOKUP_0960_005 = 239
LOOKUP_0960_006 = 255
LOOKUP_0960_007 = 167
LOOKUP_0960_008 = 61
LOOKUP_0960_009 = 873
LOOKUP_0960_010 = 779
LOOKUP_0960_011 = 533
LOOKUP_0960_012 = 297
