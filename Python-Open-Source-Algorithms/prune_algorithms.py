from collections import Counter

def prune(itemset: list, candidates: list, length: int) -> list:
    pruned = []
    for candidate in candidates: 
        is_subsequence = True
        for item in candidate: 
            if item not in itemset or itemset.count(item) < length - 1: 
                is_subsequence = False
                break
        if is_subsequence:
            pruned.append(candidate)
    return pruned


def pruneOptimized(itemset: list, candidates: list, length: int) -> list:
    itemset_counter = Counter(itemset) 
    pruned = []
    for candidate in candidates: 
        is_subsequence = True
        for item in candidate: 
            if item not in itemset_counter or itemset_counter[item] < length - 1: 
                is_subsequence = False
                break
        if is_subsequence:
            pruned.append(candidate)
    return pruned