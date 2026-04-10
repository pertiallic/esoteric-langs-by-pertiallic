import argparse
def argparser(arguments:list[str]) -> dict:
    file_parser = argparse.ArgumentParser(add_help= False)
    file_parser.add_argument("-f", "--file")
    output_parser = argparse.ArgumentParser(add_help= False)
    output_parser.add_argument("-o", "--output")
    output_parser.add_argument("-d", "--dontask", action= "store_true")
    parser = argparse.ArgumentParser(description= "test desc", epilog= "test epilog")
    subpersers = parser.add_subparsers()
    parser_run = subpersers.add_parser("run", parents= [file_parser])
    parser_format = subpersers.add_parser("format", parents= [file_parser, output_parser])
    parser_visualize = subpersers.add_parser("visualize", parents= [file_parser, output_parser])
    args:dict = vars(parser.parse_args(arguments))
    return args