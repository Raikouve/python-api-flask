from flask import Flask, request, jsonify

app = Flask(__name__)

# (GET) Rota com header params e query params
@app.route("/get-user/<user_id>")
def get_user(user_id):
  # Dados que serão retornados na requisição
  user_data = {
    "user_id": user_id,
    "name": "John Doe",
    "email": "john.doe@gmail.com"
  }
  
  # Checa se no query params tem o parâmetro 'extra' e salva na variável
  extra = request.args.get("extra")

  # Se tiver parâmetro 'extra', adiciona nos dados de retorno da requisição
  if extra:
    user_data["extra"] = extra
  
  # Retorna os dados no formato JSON
  return jsonify(user_data), 200

# (POST) Rota POST
@app.route("/create-user", methods=["POST"])
def create_user():
  # Checa se o método da requisição é POST
  if request.method == "POST":
    # Se sim, salva o corpo da requisição na variável 'data'
    data = request.get_json()

    # Envia JSON com o data para o usuário
    return jsonify(data), 201

if __name__ == "__main__":
  app.run(debug=True)