import requests
import json

def call_ollama_model(prompt, model, stream = False):
    url = 'http://localhost:11434/api/generate'

    params = {
        'prompt': prompt,
        'model': model,
        'stream': stream
    }

    payload = json.dumps(params)

    respone = requests.post(url, data=payload,
                            headers = {'Content-Type': 'application/json'})

    if respone.status_code != 200:
        return 'Error'

    else:
        respone = respone.json()['response']
        return respone

if __name__ == '__main__':
    model = 'gemma3:1b'
    prompt = input("How Can I Hellp You? ")
    response = call_ollama_model(prompt, model)

    print(f'Result: {response}')
