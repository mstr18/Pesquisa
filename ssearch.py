from flask import Flask,  request, jsonify, render_template

app = Flask(__name__)

def page(result):
    # Aqui você pode usar o resultado para gerar a página desejada
    return f'<h1>Página para o resultado: {result} </h1>'
 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']
    # Execute a função de pesquisa aqui para obter todos os resultados
    all_results = ['Result 1', 'Result 2', 'Result 3']
    # Filtrar os resultados com base na entrada do usuário
    results = [result for result in all_results if result.lower().startswith(search_term.lower())]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)