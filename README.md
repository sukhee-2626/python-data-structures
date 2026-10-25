<div align="center">

# 🐍 Python Data Structures

**A 1,000-file synthetic Python corpus of data-structure implementations,
built to train and evaluate code language models.**

![Files](https://img.shields.io/badge/Files-1%2C000-2563eb?style=for-the-badge)
![Lines](https://img.shields.io/badge/Lines-1,739,445-16a34a?style=for-the-badge)
![Size](https://img.shields.io/badge/Size-51_MB-7c3aed?style=for-the-badge)
![Algorithms](https://img.shields.io/badge/Algorithms-4-db2777?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

> **Synthetic dataset.** Every module is machine-generated from a template bank of
> algorithm implementations. It is training data for a custom code model, not
> production library code.

## Overview

This repository is one of a ten-part thematic corpus. It contains **1,000 standalone
Python modules** covering data-structure algorithms: UnionFind, Trie, two_sum, sliding_window_maximum.

Each file ranges from **100 to 4,000 lines**; every module compiles and every symbol
is namespaced with a file/block suffix so the whole corpus can be imported together.

## At a glance

| Property | Value |
| :-- | --: |
| Files (`.py`) | **1,000** |
| Total lines | **1,739,445** |
| Total size | **50.8 MiB** |
| Lines per file | **100 – 4,000** |
| Algorithms | **4** |
| Compile pass rate | **1,000 / 1,000** |
| Encoding / newlines | **UTF-8 / LF** |

## Algorithms

| Symbol | Algorithm | Average time | Variants |
| :-- | :-- | :-- | --: |
| `UnionFind` | Union-Find | `O(alpha(n))` | 26,813 |
| `Trie` | Trie | `O(L)` | 26,871 |
| `two_sum` | Two Sum | `O(n)` | 26,914 |
| `sliding_window_maximum` | Sliding Window Maximum | `O(n)` | 26,890 |

## File layout

```
algorithms/algorithm-XXXX.py
├── imports            # heapq, math, bisect, collections
├── ALGORITHM BLOCKS   # shuffled definitions, suffixed _XXXX_YYYY
├── LOOKUP_XXXX_NNN    # module constants for the exact line count
```

**Naming convention:** `{algorithm}_{file_index}_{block_index}` — for example,
`UnionFind_0042_0001`. The suffix makes every symbol in the corpus unique.

## Sample

Excerpt from `algorithms/algorithm-0042.py`:

```python
class UnionFind0042_0001:
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
    ...
```

## Quality gates

- ✅ **Compiles cleanly** — every module passed `compile(source, path, "exec")`.
- ✅ **Exact line budget** — each file hits its 100–4,000 line target to the line.
- ✅ **Pure code** — no comments, no docstrings, no prose.
- ✅ **Deterministic** — a per-file seeded RNG reproduces the corpus.
- ✅ **Collision-free symbols** — all definitions carry a unique suffix.

## Intended use

Fine-tuning and pretraining code models; synthetic-data, tokenizer, retrieval, and
version-control experiments. Not suitable as production code or as a benchmark of
human-written style.

## License

No license has been specified yet. Until one is added, treat the content as all
rights reserved by the repository owner.
