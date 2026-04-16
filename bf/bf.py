import os, sys, argparse, re
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
    parser = argparse.ArgumentParser(description= "brainf*ckのインタプリタ(+α)です")
    parser.add_argument("file", nargs= "?", default= "", help= "指定するとそのfileの中身を実行します　指定されない or 存在しない場合はソースコードの入力が求められます")
    parser.add_argument("-d", "--decompress", nargs= "?", const= " ", default= False, help= "元のソースコードを圧縮した形で表示します　file名が指定された場合そのfileの中に書き込みます")
    parser.add_argument("-c", "--compress", nargs= "?", const= " ", default= False, help= "圧縮されたソースコードを解凍して表示します　file名が指定された場合そのfileの中に書き込みます")
    return vars(parser.parse_args(arguments))
def run(code: str) -> None:
    parentheses:dict[int,int] = {}
    pareStack:list[int] = []
    memory:list[int] = [0]
    pointer:int = 0
    programPointer:int = 0
    for i, c in enumerate(code):
        match c:
            case "[":
                pareStack.append(i)
            case "]":
                if not len(pareStack):
                    print("正しくかっこが対応付けされていません")
                    return
                right = pareStack.pop()
                parentheses[right] = i
                parentheses[i] = right
    while programPointer < len(code):
        match code[programPointer]:
            case ">":
                pointer += 1
                if pointer >= len(memory):
                    memory.append(0)
            case "<":
                pointer -= 1
                if pointer < 0:
                    pointer = 0
            case "+":
                memory[pointer] += 1
                memory[pointer] %= 256
            case "-":
                memory[pointer] -= 1
                memory[pointer] %= 256
            case ",":
                inp = input()
                if inp == "":
                    inp = "\0"
                memory[pointer] = ord(inp)
            case ".":
                print(chr(memory[pointer]))
            case "[":
                if not memory[pointer]:
                    programPointer = parentheses[programPointer] - 1
            case "]":
                if memory[pointer]:
                    programPointer = parentheses[programPointer] - 1
        programPointer += 1
def main() -> None:
    args = parse(sys.argv[1:])
    print(args)
    code:str
    if not args["file"]:
        code = input()
    elif os.path.exists(args["file"]):
        code = common.readFile(args["file"])
    else:
        code = input(f"{args["file"]}が存在しません (絶対パス: {os.path.abspath(args["file"])})\n内容を入力してください\n")
    if not args["decompress"]:
        pass
    elif args["decompress"] == " ":
        print(decompress(code))
        return
    else:
        common.writeFile(args["decompress"], decompress(code))
        return
    if not args["decompress"]:
        pass
    elif args["compress"] == " ":
        print(compress(code))
        return
    else:
        common.writeFile(args["compress"], compress(code))
        return
    run(code)
if __name__ == "__main__":
    main()