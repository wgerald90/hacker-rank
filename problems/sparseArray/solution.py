#!/usr/bin/python3.7
import sys
from typing import List

sys.path.append("../../lib")

import debug.debug as debug
from commandline.commandline import CommandLine as CL

def sparse_array(strings: List[str], queries:List[str]) -> List[int]:
    count = [0] * len(queries)
    debug.print_simple_to_console(__name__, count)
    for index,item in enumerate(queries):
        count[index] += strings.count(item)

    return count
    


if __name__ == '__main__':
    cl_args = {
        "-s": "strings space seperated and wrapped in quotes",
        "-q": "strings space seperated and wrapped in quotes",
        "-d": ("if flag is given debug messages will print to the console",),
        }

    args = CL(**cl_args).arguments
    debug.set_debug(args.d)

    debug.print_simple_to_console(__name__, f'strings: {args.s}\tqueries: {args.q}')
    strings = args.s.split()
    queries = args.q.split()

    query_count = sparse_array(strings, queries)
    [print(i) for i in query_count]
