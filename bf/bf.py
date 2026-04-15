import sys, argparse, re
import common
SYMBOLS = ['+', '-', '>', '<', '[', ']', ',', '.']
COMPRESS = ['+', '-', '>', '<']
def compress(raw: str) -> str:
    rawlist = re.findall(r"((.)\2*)", raw)
    out = ""
    for s in rawlist:
        if s[0][0] in COMPRESS:
            out += s[0][0] + str(len(s[0]))
        else:
            out += s[0]
    return out
def decompress(raw: str) -> str:
    rawlist = re.findall(r"(?a:\D|\d+)", raw)
    out = ""
    for s in rawlist:
        if len(out) > 0 and s.isdecimal() and out[-1] in COMPRESS:
            out += out[-1]*(int(s)-1)
        else:
            out += s
    return out
def parse(arguments: list[str]) -> dict:
    parser = argparse.ArgumentParser(description= "test desc", epilog= "test epilog")
    parser.add_argument("file", nargs= "?")
    parser.add_argument("-d", "--decompress", nargs= "?", const= True, default= False)
    parser.add_argument("-c", "--compress", nargs= "?", const= True, default= False)
    return vars(parser.parse_args(arguments))
def run(code: str) -> None:
    return
if __name__ == "__main__":
    args = parse([""])
    input()
    
    
    