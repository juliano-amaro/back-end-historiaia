from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS
from google import genai
import json
import os

load_dotenv()

app = Flask(__name__)

CORS(app)

API_KEY = os.getenv('GENAI_APIKEY')

client = genai.Client(api_key=API_KEY)

def criar_historia(protagonista, vilao, secundario, titulo):
    prompt = f"""
        Crie uma historia com o seguinte titulo {titulo}, contendo um personagem principal que vai ser o {protagonista}, e contendo um amigo ou parceiro ou personagem secundario que vai ser {secundario}, e vai ter uma pessoa para atrapalhar a vida dos dois que vai ser {vilao}.
        A história deve ser legal, sem conteudos sexuais, e também um bom climax, tendo cenas ineditas, e também tendo bastante drama.
        Não pode ter cenas de violencia, e não pode ter palavrões, e não pode ter cenas de sexo.
        Apresente a historia no formato HTML com codificação UTF-8, sem head, sem body, sem a estrutura basica do html, apenas com o titulo em um h2, separando os paragrafos com a tag p do HTML. NÃO COLOQUE NADA A MAIS ALÉM DO H2 E P.
        NÃO DEIXE AS TRÊS ASPAS DO COMEÇO E NO FIM TAMBÉM QUERO QUE TIRE A SIGLA HTML NO COMEÇO DO CONTEUDO.

    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text

@app.route('/historia', methods=['POST'])
def criacao_historia():

    dados = request.get_json()
    print(dados)

    elemento = dados.get('elementos', [])
    
    response = criar_historia(elemento[0], elemento[1], elemento[2], elemento[3])

    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
