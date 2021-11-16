# The Simulator class will produce random characters, check them against a trie, and present information on the current status of the challenge

# TODO:
# 1. add datetime to next() (once schema is known)
import random
import trie
from __future__ import annotations

class Simulator:
    def __init__(self, trie: dict[str, dict|float|bool], valid_elements: str|list[str]):
        self.trie = trie
        self.curr_node = trie
        self.curr_string = ''
        self.valid_elements = valid_elements
        if type(self.valid_elements) == str:
            self.using_chars = True

        self.done = False

    def next(self) -> tuple[str, int] | tuple[None, None]:
        # Gets a random character and returns the generated character and updated completion percentage
        if self.done:
            return (None, None)

        next_element = random.choice(self.valid_elements)
        if next_element in self.curr_node:
            self.curr_node = self.curr_node[next_element]
            if self.using_chars:
                self.curr_string += next_element
            else:
                self.curr_string += next_element + ' '
        else:
            self.curr_node = self.trie
            self.curr_string = ''

        if self.curr_node['is_done']:
            self.done = True

        return (next_element, self.curr_node['max_percentage'])

    def get_current_percentage(self) -> int:
        return self.curr_node['max_percentage']

    def get_current_string(self) -> str:
        return self.curr_string
    
    def get_matched_works(self) -> List[str]:
        return self.curr_node['work_ids']
