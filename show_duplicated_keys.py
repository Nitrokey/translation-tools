#!/usr/bin/env python3
from collections import defaultdict

import Levenshtein  # pip3 install python-Levenshtein --user
import sys

import click


@click.command()
@click.option('--thresh', default=4, type=int, help='Maximum Levenshtein distance')
@click.option('--case_sensitive', default=False, type=bool, help='Make comparision case sensitive')
def process(thresh: int, case_sensitive: bool):
    prev = '=' * 20

    results = defaultdict(list)

    for line in sys.stdin:
        line = line.strip().replace('<source>', '').replace('</source>', '')
        if not line: continue
        if not case_sensitive:
            distance = Levenshtein.distance(line.lower(), prev.lower())
        else:
            distance = Levenshtein.distance(line, prev)
        if distance < thresh:
            results[distance].append((line, prev))
        prev = line

    for distance in sorted(results.keys(), reverse=True):
        print('Distance: {} / case sensitive: {}'.format(distance, case_sensitive).center(110, '='))
        for res in results[distance]:
            line, prev = res
            print('{:^50} \t\t {:^50}'.format(line, prev))

    print(results.keys())
    t = 0
    for distance in sorted(results.keys(), reverse=True):
        v = len(results[distance])
        print('{}: {}'.format(distance, v))
        t += v
    print('Total: {}'.format(t))

if __name__ == '__main__':
    process()
