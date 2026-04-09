import os,sys
import os.path
def visualizer(raw: str) -> str:
    return raw.replace(" ", "[space]").replace("\t", "[tab]").replace("\n", "[enter]\n")
def readfile(path: str | os.PathLike) -> str:
    with open(path, "r") as f:
        return f.read()
def writefile(path: str | os.PathLike, content: str) -> int:
    with open(path, "w") as f:
        return f.write(content)
def fileinsert(path: str, text: str) -> str:
    name: tuple = os.path.splitext(path)
    return name[0] + text + name[1]
def main() -> None:
    args:list = sys.argv
    args.append(0)
    FILEPATH = args[1] or input()
    writefile(fileinsert(FILEPATH, "_visualized"),visualizer(readfile(FILEPATH)))
if __name__ == "__main__":
    main()