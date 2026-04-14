"""@deprecated"""
import argparse
def argparser(arguments:list[str]) -> dict:
    parser = argparse.ArgumentParser(description= "test desc", epilog= "test epilog")
    parser.add_argument("file")
    parser.add_argument("-f", "--format", nargs= "?", const= True, default= False)
    parser.add_argument("-v", "--visualize", nargs= "?", const= True, default= False)
    return vars(parser.parse_args(arguments))
if __name__ == "__main__":
    print(argparser(["test.txt", "-f", "test.ws", ]))