import shlex
from Group import Group
from Property import *

BLOCK_WORDS = ('version', 'group')

class ParseError(Exception): pass

def split(line: str) -> list[str]:
    return shlex.split(line, True, True)

def parse(code: str, version: int|None = None) -> list[Group]:
    # by default, we will attempt to find the latest version.
    versions_list: list[int] = []
    versions_index_list: list[int] = []
    max_version: int = 0
    lines: list[str] = [x.strip() for x in code.split('\n')]
    i: int = 0

    def crash_if_EOF():
        if i >= len(lines):
            raise EOFError(code, i)

    # finding the available versions
    stk: int = 0
    while i < len(lines):
        if lines[i] == '':
            i += 1
            continue
        tokens: list[str] = split(lines[i])
        if tokens[0] == 'version':
            if stk > 0:
                raise ParseError(f'version tag inside another version tag at line {i+1}')
            v = int(tokens[1])
            if v in versions_list:
                raise ParseError(f'version {v} already defined at line {i+1}')
            versions_list.append(v)
            versions_index_list.append(i)
            if v > max_version: max_version = v
            stk += 1
        elif tokens[0] in BLOCK_WORDS:
            stk += 1
        elif tokens[0] == ';':
            stk -= 1

        if stk < 0:
            raise ParseError(f'superfluous ; at line {i+1}')
        i += 1
    
    # parsing
    if version == None: version = max_version
    i = versions_index_list[versions_list.index(version)] + 1
    stk = 1

    groups: list[Group] = []

    return groups

if __name__ == '__main__':
    print(parse("""
version 1
    balls
;
"""))