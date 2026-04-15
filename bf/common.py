"""共通の関数たち"""
import os
import os.path
def readFile(path: str|os.PathLike) -> str:
    with open(path, "r") as f:
        return f.read()
def writeFile(path: str|os.PathLike, content: str) -> int:
    with open(path, "w") as f:
        return f.write(content)
def fileNameInsert(path: str, text: str) -> str:
    name: tuple = os.path.splitext(path)
    return name[0] + text + name[1]
def replaceAll(raw: str, mapper: list[tuple[str, str]]):
    if not len(mapper): return raw
    return replaceAll(raw.replace(mapper[0][0], mapper[0][1]), mapper[1:])
def cleanup(raw: list, notallowed: list = [None, ""]) -> list:
    return list(filter(lambda x: (x not in notallowed), raw))