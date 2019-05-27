from lark import Lark
grammar = """
    ?start:expr 
    ?expr: (term) (("+" | "-") (term))*
    ?term : (factor) (("*" | "/" | "//" | "%") (factor))*
    ?factor : (base) ("^" (factor))?
    ?base : ("+" | "-") (base) | NUMBER | "(" expr ")"
    %import common.SIGNED_NUMBER -> NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

parser = Lark(grammar)


def main():    
    expression = input("\nEscreve uma expressao: ")
    while True:
        print(parser.parse(expression))    
        expression = input("\nEscreve uma expressao ou aberte enter: ")
        if expression == "":
            break 
if __name__ == '__main__':
    main()