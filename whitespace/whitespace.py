import os, sys
from .. import common
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
    return common.replaceall(raw, VISUALIZING_TABLE)
def formatter(raw: str) -> str:
    return common.replaceall(raw, FORMATTING_TABLE)
with open("test_formatted.ws","w") as f:
    print("")