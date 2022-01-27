from flask import *

# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

app = Flask(__name__)


@app.route("/")
def root():
    text = request.args.get('user')
    if text:
        return process_text(text)

    return {
        "status": 400
    }


def process_text(text):
    # Load English tokenizer, tagger, parser and NER
    nlp = spacy.load("en_core_web_trf")

    doc = nlp(text)

    # Analyze syntax
    # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

    # Find named entities, phrases and concepts
    # for entity in doc.ents:
    #     print(entity.text, entity.label_)

    return {
        "status": 200,
        "nouns": [token.lemma_ for token in doc if token.pos_ == "NOUN"],
        "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]
    }

if __name__ == '__main__':
    app.run()