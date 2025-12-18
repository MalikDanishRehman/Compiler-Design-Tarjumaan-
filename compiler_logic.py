import re
import sys
from io import StringIO

# --- 1. Keywords Dictionary (Lughat) ---
keywords = {
    'agar': 'if',
    'warna': 'else',
    'varna': 'else',
    'jabtak': 'while',
    'dikhao': 'print',
    'pucho': 'input',
    'sahi': 'True',
    'ghalat': 'False',
    'roko': 'break',
    'chalo': 'run'
}

# --- 2. Translation Engine ---
def tarjuma_karo(urdu_code):
    translated_code = urdu_code
    for urdu_word, py_word in keywords.items():
        # Sirf exact word match karega (taake 'sagar' ka 'agar' change na ho)
        pattern = r'\b' + urdu_word + r'\b'
        translated_code = re.sub(pattern, py_word, translated_code)
    return translated_code

# --- 3. Execution Engine ---
def code_chalao(python_code):
    # Output capture karne ka setup
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()

    try:
        exec(python_code) # Code yahan run hoga
        result = redirected_output.getvalue()
    except Exception as e:
        result = f"Ghalati (Error): {e}"
    finally:
        sys.stdout = old_stdout # System wapis normal hojaye
    
    return result