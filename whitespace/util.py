import os
import os.path
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
    return raw.replace(" ", "[space]").replace("\t", "[tab]").replace("\n", "[enter]\n")
def formatter(raw: str) -> str:
    return raw.replace(" ","").replace("s", " ").replace("t", "\t").replace("n\n", "\n")