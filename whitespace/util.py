"""本体(whitespace.py)にマージされる予定"""
import os
import os.path
import argparse
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
def replaceall(raw:str, mapper: list[tuple[str, str]]):
    if not len(mapper): return raw
    return replaceall(raw.replace(mapper[0][0], mapper[0][1]), mapper[1:])
def readfile(path: str | os.PathLike) -> str:
    with open(path, "r") as f:
        return f.read()
def writefile(path: str | os.PathLike, content: str) -> int:
    with open(path, "w") as f:
        return f.write(content)
def fileinsert(path: str, text: str) -> str:
    name: tuple = os.path.splitext(path)
    return name[0] + text + name[1]
def visualizer(raw: str) -> str:
    return replaceall(raw, VISUALIZING_TABLE)
def formatter(raw: str) -> str:
    return replaceall(raw, FORMATTING_TABLE)
def argparser(arguments:list[str]) -> dict:
    parser = argparse.ArgumentParser(description= "test desc", epilog= "test epilog")
    parser.add_argument("file")
    parser.add_argument("-f", "--format", nargs= "?", const= True, default= False)
    parser.add_argument("-v", "--visualize", nargs= "?", const= True, default= False)
    return vars(parser.parse_args(arguments))
if __name__ == "__main__":
    print(formatter("hello"))