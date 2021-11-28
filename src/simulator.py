# The Simulator class will produce random characters, maintain the current state of the simulation, and post to the database when a mistake is made (run completed)


import random
import trie
from datetime import datetime
from __future__ import annotations

class Simulator:
    def __init__(self, trie: dict[str, dict|float|bool], valid_elements: str):
        self.trie = trie
        self.curr_node = trie
        self.curr_string = ''
        self.valid_elements = valid_elements

        self.done = False

    def next(self) -> tuple[str, float, str, str, bool] | None:
        # Generates a random character and updates internal state of simulator
        # Returns information according to the database schema including:
        # 1. Current generated string (character count derived from this string)
        # 2. Highest match percentage
        # 3. Corresponding work
        # 4. Datetime (UTC)
        # Also returns a flag denoting whether a mismatch has occurred, and therefore
        # the calling function should post the returned result to the database
        if self.done:
            return None

        next_element = random.choice(self.valid_elements)

        # Found a match
        if next_element in self.curr_node:
            self.curr_node = self.curr_node[next_element]
            self.curr_string += next_element
            if self.curr_node['is_done']:
                self.done = True
            return self.curr_string, self.curr_node['max_percentage'], self.curr_node['work_title'],
                    str(datetime.now()), self.done
        else:
            # Return info to post to database
            generated_string = self.curr_string
            match_percentage = self.curr_node['max_percentage']
            work = self.curr_node['work_title']
            time = str(datetime.now())
            self.curr_node = self.trie

            self.curr_string = ''
            
            return generated_string, match_percentage, work, time, True
