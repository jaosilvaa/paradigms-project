import ply.lex as lex
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


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
    r'\btrue\b'
    t.value = True
    return t

def t_FALSE(t):
    r'\bfalse\b'
    t.value = False
    return t

# Regex para null
def t_NULL(t):
    r'\bnull\b'
    t.value = None
    return t

def t_error(t):
    errors.append(f'Caractere ilegal: {t.value[0]}')
    t.lexer.skip(1)


lexer = lex.lex()
errors = []

def json_analyze(text):
    lexer.input(text)
    tokens_found = []
    global errors
    errors = []
    
    for token in lexer:
        tokens_found.append(f"{token.type}: {token.value}")
    return tokens_found, errors