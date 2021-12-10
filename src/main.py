# Combines functionality of simulator and table utilities to provide a script that can run the simulation and post to the database when a simulation completes
from __future__ import annotations
from simulator import Simulator
from trie import create_trie
from time import sleep
import boto3

import sys
sys.path.append('../util/')
from table_utils import put_simulation_run

def create_simulator() -> Simulator:
    trie = create_trie()
    with open('../data/valid_chars.txt') as f:
        valid_chars = f.read()

    return Simulator(trie, valid_chars)

if __name__ == '__main__':
    simulator = create_simulator()
    dynamodb = boto3.resource('dynamodb')
    while True:
        number_runs = int(input('Enter number of times to run simulation: '))
        if number_runs == 0:
            print('Done simulating')
            break

        for _ in range(number_runs):
            generated_string, match_percentage, work_title, date, time, post = simulator.next()
            char_count = len(generated_string)
            print(generated_string)
            if post:
                response = put_simulation_run(date, time, char_count, match_percentage, 
                                                generated_string, work_title, dynamodb=dynamodb)
                print(response)

        
        sleep(10) # adjust this as needed