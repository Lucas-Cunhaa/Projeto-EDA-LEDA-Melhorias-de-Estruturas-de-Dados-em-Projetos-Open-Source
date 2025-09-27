import unittest
from prune_algorithms import prune, pruneOptimized

class TestPruneFunctions(unittest.TestCase):

    def test_basic(self):
        itemset = ['a', 'b', 'c', 'a']
        candidates = [['a', 'b'], ['b', 'c'], ['a', 'a', 'b'], ['d']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_empty_candidates(self):
        itemset = ['a', 'b', 'c']
        candidates = []
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_empty_itemset(self):
        itemset = []
        candidates = [['a'], ['b']]
        length = 1
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_length_greater_than_itemset(self):
        itemset = ['a', 'b']
        candidates = [['a'], ['b'], ['a', 'b']]
        length = 3
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_multiple_occurrences(self):
        itemset = ['a', 'a', 'b', 'b', 'c']
        candidates = [['a', 'a'], ['b', 'b'], ['a', 'b'], ['c', 'c']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_candidate_with_missing_items(self):
        itemset = ['x', 'y', 'z']
        candidates = [['x', 'y'], ['x', 'a'], ['y', 'z']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_candidate_longer_than_itemset(self):
        itemset = ['a', 'b']
        candidates = [['a', 'b', 'c'], ['b', 'a'], ['c']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_itemset_with_repeated_elements(self):
        itemset = ['a', 'a', 'b', 'b', 'c', 'c']
        candidates = [['a', 'b', 'c'], ['a', 'a', 'b'], ['b', 'b', 'c', 'c']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_all_candidates_invalid(self):
        itemset = ['m', 'n']
        candidates = [['x'], ['y', 'z'], ['a', 'b']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_length_one(self):
        itemset = ['p', 'q', 'r']
        candidates = [['p'], ['q'], ['s']]
        length = 1
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))
        
    def test_repeated_items_below_length_minus_one(self):
        itemset = ['a', 'a', 'b']
        candidates = [['a', 'a', 'b'], ['a', 'b']]
        length = 4  # length - 1 = 3, 'a' aparece só 2 vezes
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_empty_candidate_list(self):
        itemset = ['x', 'y', 'z']
        candidates = [[]]  # candidato vazio
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_empty_itemset_length_greater_than_one(self):
        itemset = []
        candidates = [['a'], ['b']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_candidate_with_more_repeats_than_itemset(self):
        itemset = ['a', 'b']
        candidates = [['a', 'a'], ['b', 'b'], ['a', 'b']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

    def test_mixed_type_items(self):
        itemset = ['1', '1', '1.0']
        candidates = [['1', '1'], ['1.0', '1'], ['1', '1']]
        length = 2
        self.assertEqual(prune(itemset, candidates, length), pruneOptimized(itemset, candidates, length))

if __name__ == "__main__":
    unittest.main()