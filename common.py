"""共通の関数たち"""
import os
import os.path
import argparse
def readfile(path: str | os.PathLike) -> str:
    with open(path, "r") as f:
        return f.read()
def writefile(path: str | os.PathLike, content: str) -> int:
    with open(path, "w") as f:
        return f.write(content)
def fileinsert(path: str, text: str) -> str:
    name: tuple = os.path.splitext(path)
    return name[0] + text + name[1]
def replaceall(raw:str, mapper: list[tuple[str, str]]):
    if not len(mapper): return raw
    return replaceall(raw.replace(mapper[0][0], mapper[0][1]), mapper[1:])
def parse(arguments:list[str]) -> dict:
    parser = argparse.ArgumentParser(description= "test desc", epilog= "test epilog")
    parser.add_argument("file", nargs= "?")
    parser.add_argument("-f", "--format", nargs= "?", const= True, default= False)
    parser.add_argument("-v", "--visualize", nargs= "?", const= True, default= False)
    return vars(parser.parse_args(arguments))
if __name__ == "__main__":
    print(parse(["-f", "test.ws", ]))