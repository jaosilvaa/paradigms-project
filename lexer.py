import sys
import ply.lex as lex


# Caracteres JSON
# { } [ ] : , 

# Tokens
tokens = (
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
    'COLON', 'COMMA',
    'STRING', 'NUMBER',
    'TRUE', 'FALSE', 'NULL',
)


# Regex de cada um dos tokens
# Regex simples
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COLON = r':'
t_COMMA = r','
t_ignore = ' \t\n\r'

# Regex para strings
def t_STRING(t):
    r'"(\\.|[^"\\])*"'
    t.value = t.value[1:-1] # Pega a string sem as aspas
    return t

# Regex para números
def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else: 
        t.value = int(t.value)
    return t

# Regex para booleanos
def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

# Regex para null
def t_NULL(t):
    r'null'
    t.value = None
    return t

def t_error(t):
    print(f'Caractere ilegal: {t.value[0]} in line {t.lineno} in position {t.lexpos}')
    t.lexer.skip(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python lexical_analyzer.py <data.json> \nEx: "
            "python lexical_analyzer.py data.json")
        return

    json_path = sys.argv[1]

    if not json_path.endswith('.json'):
        print('Please use a json file')
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        json_content = f.read()


    # Criando o lexer
    lexer = lex.lex()

    lexer.input(json_content)

    for tok in lexer:
        if not tok:
            break
        print(tok)

if __name__ == "__main__":
    main()