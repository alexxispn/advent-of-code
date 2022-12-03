#!/usr/bin/env python3

def sum_calories(elf: list) -> int:
    return sum([int(item) for item in elf if item])


def get_elves():
    with open('01-input.txt') as f:
        items = f.read().split('\n\n')
        elves = [item.split('\n') for item in items]
        elves_table = {}
        for i, elf in enumerate(elves):
            elves_table[i] = sum_calories(elf)
        return elves_table


def get_top_three(elves: dict) -> list:
    return sorted(elves.items(), key=lambda x: x[1], reverse=True)[:3]


def sum_top_three(elves: list) -> int:
    return sum([item[1] for item in elves])


if __name__ == '__main__':
    elves = get_elves()
    top_3 = get_top_three(elves)
    print(sum_top_three(top_3))
