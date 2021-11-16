# Use a Trie to test whether the simulation is matching the works of Shakespeare
# Implemented as a nested dictionary, each key will be a value and point to its children and the largest percentage match for the current prefix
# Although a recursive implementation is cleaner in my opinion, it runs into issues of maximum recursion depth limit when saving the trie to file
# Still have to be careful though, as trying to print the full trie will result in a recursion error

# annotations allows for easy type hinting (dict, list)
from __future__ import annotations

def insert(trie: dict[str, dict|float|bool], work: str, work_id: int) -> None:
    # Inserts a work into our trie object
    node = trie
    for i, element in enumerate(work):
        if element not in node:
            node[element] = {'max_percentage': 0, 'is_done': False}
            node[element]['work_ids'] = [work_id]
        else:
            node[element]['work_ids'].append(work_id)
        
        percentage_done = (i + 1) / len(work)
        percentage_done = round(percentage_done * 100, 2)
        node[element]['max_percentage'] = max(node[element]['max_percentage'], percentage_done)

        # set done flag for last character
        if i == len(work) - 1:
            node[element]['is_done'] = True

        node = node[element]

def create_trie(works: list[str] | list[list[str]]) -> dict[str, dict|float|bool]:
    # Creates trie containing all of Shakespeares works
    # Currently represented as a nested dictionary
    trie = {'max_percentage': 0, 'is_done': False, 'work_ids': []}
    for i, work in enumerate(works):
        insert(trie, work, i)
    return trie
