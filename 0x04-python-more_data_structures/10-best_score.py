#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    items = list(a_dictionary.items())
    best_score_key, best_score = items[0]
    for key, score in items[1:]:
        if score > best_score:
            best_score_key = key
            best_score = score
    return best_score_key
