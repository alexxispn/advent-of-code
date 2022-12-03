#!/usr/bin/env python3

import os
import sys

extensions = ['.py', '.ts', '-input.txt']
year = sys.argv[1]
advent_days = 25


def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def create_file(file):
    if not os.path.exists(file):
        open(file, 'a').close()


def get_md_content(year, day):
    return f'# Advent of Code {year} - Day {day}' \
           f' \r\n\r\n> :bulb:️ **Problem Description**'


def create_advent_year_structure(year):
    for advent_day in range(1, advent_days + 1):
        day = f'{advent_day:02}'
        folder = f'{year}/{day}'
        create_folder(folder)
        with open(f'{folder}/README.md', 'w') as f:
            f.write(get_md_content(year, day))
        for extension in extensions:
            file = f'{folder}/{day}{extension}'
            create_file(file)


if __name__ == '__main__':
    create_advent_year_structure(year)
