from flask import Flask, render_template, request
from compiler_logic import tarjuma_karo, code_chalao

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    code_input = ""
    output_result = ""
    
    if request.method == 'POST':
        code_input = request.form.get('code_area') # User ka Urdu code
        
        # Step 1: Tarjuma (Urdu -> Python)
        py_code = tarjuma_karo(code_input)
        
        # Step 2: Run (Execute)
        output_result = code_chalao(py_code)

    return render_template('index.html', code=code_input, result=output_result)

if __name__ == '__main__':
    app.run(debug=True)