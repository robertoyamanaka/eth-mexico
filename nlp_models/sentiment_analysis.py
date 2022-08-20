# Based on
# https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment


# Tasks:
# emoji, emotion, hate, irony, offensive, sentiment
# stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary

from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax


class SentimentAnalysis:
    def __init__(self):
        self.task = "sentiment"
        self.MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.config = AutoConfig.from_pretrained(self.MODEL)
        # PT
        self.model = AutoModelForSequenceClassification.from_pretrained(self.MODEL)
        self.model.save_pretrained(self.MODEL)
        self.tokenizer.save_pretrained(self.MODEL)

    def preprocess(self, text):
        new_text = []
        for t in text.split(" "):
            t = "@user" if t.startswith("@") and len(t) > 1 else t
            t = "http" if t.startswith("http") else t
            new_text.append(t)
        return " ".join(new_text)

    def get_sentiment(self, text):
        text = self.preprocess(text)
        encoded_input = self.tokenizer(text, return_tensors="pt")
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)[::-1]
        ranking = ranking[::-1]
        max_label = ""
        max_score = 0
        for i in range(scores.shape[0]):
            label = self.config.id2label[ranking[i]]
            score = scores[ranking[i]]
            if score > max_score:
                max_label = label
                max_score = score
        return {max_label: max_score}
