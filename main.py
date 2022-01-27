from flask import *
import base64

# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

app = Flask(__name__)


@app.route("/")
def root():
    text = request.args.get('user')
    if text:
        return process_text(base64.b64decode(text))

    return {
        "status": 400,
        "readable_status": "Couldn't process request as request does not contain enough parameters or parameters are "
                           "invalid."
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
        "readable_status": "Request succeeded.",
        "nouns": [token.lemma_ for token in doc if token.pos_ == "NOUN"],
        "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]
    }


if __name__ == '__main__':
    app.run()
