import json
import requests
import sys

sys.path.append("../")
from keys.private_keys import HUGGING_API_KEY

import json
import requests


class SentenceSimilarity:
    def __init__(self, base_sentence):
        self.API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
        self.headers = {"Authorization": f"Bearer {HUGGING_API_KEY}"}
        self.base_sentence = base_sentence

    def get_similarities(self, sentences):
        payload = {
            "inputs": {
                "source_sentence": self.base_sentence,
                "sentences": sentences,
            }
        }
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        return response.json()
