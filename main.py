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
token = os.getenv('TOKEN')
auth = os.getenv('AUTH')

# Inicializa o cliente da API do HubSpot
api_client = HubSpot(access_token=token)

while True:
    # Conectar-se ao webhook
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/dc_v3u3w74/event_summaries', headers={'Authorization': auth})
    res = conn.getresponse()

    # Verifica o código de status da resposta do webhook
    if res.status == 200:
        # Ler os dados JSON da resposta
        data = res.read()
        json_data = json.loads(data.decode("utf-8"))
        conn.close()
    else:
        print(f"Erro: {res.status} - {res.reason}")

    # Extrair o email e primeiro nome dos dados JSON
    event_data = json_data.get("data", [])[0].get("event", {}).get("body", {})
    email = event_data.get("data[email]", "").strip('"')
    firstname = event_data.get("data[merges][FNAME]", "").strip('"')

    # Tente realizar o cadastro de contato no HubSpot
    try:
        contact_properties = {"email": email, "firstname": firstname}
        simple_public_object_input_for_create = SimplePublicObjectInputForCreate(properties=contact_properties)
        api_response = api_client.crm.contacts.basic_api.create(
            simple_public_object_input_for_create=simple_public_object_input_for_create
        )
        print("Adicionado com sucesso:", email, firstname)

    # Lidar com exceções
    except ApiException as e:
        print("Exception when creating contact:", e)
        print("Erro no email e nome:", email, firstname)

    # Aguardar por um segundo antes da próxima iteração
    time.sleep(1)
