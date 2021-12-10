# Use a Trie to test whether the simulation is matching the works of Shakespeare
# Implemented as a nested dictionary, each key will be a value and point to its children and the largest percentage match for the current prefix
# Although a recursive implementation is cleaner in my opinion, it runs into issues of maximum recursion depth limit when saving the trie to file
# Still have to be careful though, as trying to print the full trie will result in a recursion error


# annotations allows for easy type hinting (dict, list)
from __future__ import annotations
from pathlib import Path

def insert(trie: dict[str, dict|float|bool], work: str, work_title: str, work_len: int) -> None:
    # Inserts a work into our trie object
    node = trie
    for i, element in enumerate(work):
        if element not in node:
            node[element] = {'max_percentage': 0, 'is_done': False}
            node[element]['work_title'] = work_title
            node[element]['work_len'] = work_len
        
        percentage_done = (i + 1) / len(work)
        percentage_done = round(percentage_done * 100, 2)
        existing_percentage = node[element]['max_percentage']
        existing_len = node[element]['work_len']
        update_curr_info = ((percentage_done > existing_percentage) or 
                            (percentage_done == existing_percentage and work_len > existing_len))

        if update_curr_info:
            node[element]['max_percentage'] = percentage_done
            node[element]['work_title'] = work_title
            node[element]['work_len'] = work_len

        # set done flag for last character
        if i == len(work) - 1:
            node[element]['is_done'] = True

        node = node[element]

def create_trie() -> dict[str, dict|float|bool]:
    # Creates trie containing all of Shakespeares works
    # Currently represented as a nested dictionary
    trie = {'max_percentage': 0, 'is_done': False, 'work_title': '', 'work_len': 0}
    work_directory = '../data/concatenated_works/'
    works_path = Path(work_directory)
    for work_path in works_path.glob('*'):
        work_title = filename_to_title(str(work_path.relative_to(works_path)))
        with open(work_path) as f:
            work = f.read()
            insert(trie, work, work_title, len(work))
    return trie

def filename_to_title(filename: str) -> str:
    # Turns filename to space separated title
    # e.g. romeo_and_juliet.txt -> Romeo and Juliet

    # Remove file extension
    filename = filename[:filename.index('.')]

    title = ' '.join(filename.split('_'))
    return title.title()

if __name__ == '__main__':
    create_trie()
