from __future__ import annotations

def concat_helper(works: list[int], title: str) -> None:
    # Concatenates work text files in order of works and writes the result to a new file called title.txt
    concat_str = ''
    for work in works:
        with open(f'../data/works/{work}.txt') as f:
            concat_str += f.read()

    with open(f'{title}.txt') as f:
        f.write(concat_str)

