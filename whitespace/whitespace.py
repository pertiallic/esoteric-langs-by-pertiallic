import os, sys, argparse
import common
FORMATTING_TABLE = [
    (" ", ""),
    ("s", " "),
    ("t", "\t"),
    ("n\n", "\n")
]
VISUALIZING_TABLE = [
    (" ", "[Space]"),
    ("\t", "[Tab]"),
    ("\n", "[LF]")
]
def visualizer(raw: str) -> str:
    return common.replaceAll(raw, VISUALIZING_TABLE)
def formatter(raw: str) -> str:
    return common.replaceAll(raw, FORMATTING_TABLE)
def parse(arguments: list[str]) -> dict:
    parser = argparse.ArgumentParser(description= "test desc", epilog= "test epilog")
    parser.add_argument("file", nargs= "?")
    parser.add_argument("-f", "--format", nargs= "?", const= True, default= False)
    parser.add_argument("-v", "--visualize", nargs= "?", const= True, default= False)
    return vars(parser.parse_args(arguments))
with open("test_formatted.ws","w") as f:
    print("")