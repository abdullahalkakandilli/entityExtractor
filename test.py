import requests

API_URL = "https://api-inference.huggingface.co/models/StanfordAIMI/stanford-deidentifier-base"
headers = {"Authorization": f"Bearer {'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'}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "My name is Sarah Jessica Parker but you can call me Jessica, I live in Berlin",
})

print(output)


