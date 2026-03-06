from itertools import combinations


def two_characters(s):
    max_len = 0
    chars = list(set(s))
    for char_pair in combinations(chars, 2):
        filtered = [c for c in s if c in char_pair]
        is_valid = True
        for i in range(len(filtered) - 1):
            if filtered[i] == filtered[i + 1]:
                is_valid = False
                break
        if is_valid:
            max_len = max(max_len, len(filtered))
    return max_len
