from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInputForCreate
from hubspot.crm.contacts.exceptions import ApiException
import http.client
import json
import time
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
time.sleep(1)

# Obtenha as credenciais da API do HubSpot a partir das variáveis de ambiente
token = os.getenv('TOKEN')
auth = os.getenv('AUTH')

# Crie uma instância do cliente da API do HubSpot
api_client = HubSpot(access_token=token)

while True:
    # Consulta o Webhook
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/dc_v3u3w74/event_summaries', '', {
        'Authorization': auth,
    })
    res = conn.getresponse()

    # Verifica o código de status da resposta do Webhook
    if res.status == 200:
        # Ler os dados JSON da resposta
        data = res.read()
        json_data = json.loads(data.decode("utf-8"))
        conn.close()
    else:
        print(f"Erro: {res.status} - {res.reason}")

    # Extrai o email e o primeiro nome dos dados do Webhook
    email = json.dumps(json_data["data"][0]["event"]["body"]["data[email]"]).strip('"')
    firstname = json.dumps(json_data["data"][0]["event"]["body"]["data[merges][FNAME]"]).strip('"')

    # Tenta criar um novo contato no HubSpot
    try:
        simple_public_object_input_for_create = SimplePublicObjectInputForCreate(
            properties={"email": email, "firstname": firstname}
        )
        api_response = api_client.crm.contacts.basic_api.create(
            simple_public_object_input_for_create=simple_public_object_input_for_create
        )
        print("Contato adicionado com sucesso:", email, firstname)

    # Em caso de erro, capture e exiba exceções
    except ApiException as e:
        print("Erro ao criar o contato: %s\n" % e)
        print("Erro no email e nome: ", email, firstname)
        
    time.sleep(1)
