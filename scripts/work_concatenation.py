from __future__ import annotations

def concat_helper(start: int, end: int, title: str) -> None:
    # Concatenates work text files in order of works and writes the result to a new file called title.txt
    concat_str = ''
    for work in range(start, end+1):
        with open(f'../data/works/{work}.txt') as f:
            concat_str += f.read()

    with open(f'../data/concatenated_works/{title}.txt', 'w') as f:
        f.write(concat_str)

