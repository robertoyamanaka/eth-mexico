import json
import sys

sys.path.append("../")
from description_similarities.sentence_similarity import SentenceSimilarity


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


cmc_data_20 = load_json(
    "/Users/robertoyamanaka/Documents/EthHack/eth-mexico/data/cmc_data_20.json"
)


def get_description_similarities(symbol, cmc_data=cmc_data_20):
    try:
        base_sentence = cmc_data[symbol]["description"]
    except:
        return "No description found for this coin"
    sentence = SentenceSimilarity(base_sentence=base_sentence)
    similarities = []
    for key in cmc_data:
        similarity = list(
            sentence.get_similarities(sentences=[cmc_data[key]["description"]])
        )[0]
        similarities.append({key: similarity})
    return similarities


def get_most_similar_description(symbol):
    similarities = get_description_similarities(symbol)
    max_value = 0
    max_key = ""
    for element in similarities:
        element_key = list(element.keys())[0]
        if element_key != symbol:
            element_value = list(element.values())[0]
            if element_value > max_value:
                max_value = element_value
                max_key = element_key
    return {"similar_symbol": max_key, "percentage": max_value}
