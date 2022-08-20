import json

from sentence_similarity import SentenceSimilarity


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


cmc_data = load_json(
    "/Users/robertoyamanaka/Documents/EthHack/eth-mexico/data/cmc_data.json"
)


def get_coin_similarities(ticker, cmc_data):
    try:
        base_sentence = cmc_data[ticker]["description"]
    except:
        return "No description found for this coin"
    sentence = SentenceSimilarity(base_sentence=base_sentence)
    similarities = []
    for key in cmc_data:
        similarity = sentence.get_similarities(
            sentences=[cmc_data[key]["description"]]
        )[0]
        similarities.append({key: similarity})
    return similarities
