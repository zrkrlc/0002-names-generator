# -*- coding: utf-8 -*-

from os import path
from random import randint
from sys import argv
from sys import exit as close

#number = argv

def main():
        prompt = "Enter number of names to be generated: \n"
        try:
                answer = int(raw_input(prompt))
                print generate_names(answer)
                raw_input()
                close(0)
        except Exception:
                print "Try again. \n"
                main()

# get_lines :: IO() -> [Char] or something like that
def get_lines(path):
        try:
                f = open(path)
        except IOError:
                f = ['']
                pass
        lister = [i.strip() for i in f]
        return lister

# generate_names :: IO() -> [Char]
def generate_names(n):
        prefix = sorted(get_lines("prefix.txt"))
        infix = sorted(get_lines("infix.txt"))
        suffix = sorted(get_lines("suffix.txt"))

        lister = [a + " " + b + " " + c for a in prefix for b in infix for c in suffix]

        counter = 0
        while counter < n:
                print "あ    " + lister[randint(0, len(lister))]
                counter += 1

        return ''


main()
