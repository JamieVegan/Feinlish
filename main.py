import argparse
from vocabulary import *

parser = argparse.ArgumentParser(prog="Feinlish")

parser.add_argument("sentence")
args = parser.parse_args()

sentence = args.sentence

for noun in nouns:
    sentence = sentence.replace(noun, nouns.get(noun, ""))

for verb in verbs:
    sentence = sentence.replace(verb, verbs.get(verb, ""))

for thing in others:
    sentence = sentence.replace(thing, others.get(thing, ""))

print(sentence)
