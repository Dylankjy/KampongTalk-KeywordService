import datetime

from flask import *
import base64
import spacy

app = Flask(__name__)


@app.route("/")
def root():
    try:
        text_base64 = request.args.get('text')

        # Decodes base64 string and removes b' header
        text_decoded = str(base64.b64decode(text_base64)).replace("b'", "")

        if text_decoded:
            return process_text(text_decoded)

    except:
        return {
            "server": "KampongTalk Keyword API",
            "status": 400,
            "readable_status": "Couldn't process request as request does not contain enough parameters or parameters "
                               "are invalid.",
            "response_timestamp": datetime.datetime.now().timestamp(),
        }


def process_text(text):
    # Load English tokenizer, tagger, parser and NER
    nlp = spacy.load("en_core_web_lg")

    doc = nlp(text)

    # Analyze syntax
    # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

    # Find named entities, phrases and concepts
    # for entity in doc.ents:
    #     print(entity.text, entity.label_)

    res = {
        "server": "KampongTalk Keyword API",
        "status": 200,
        "readable_status": "Request succeeded.",
        "nouns": [token.lemma_ for token in doc if token.pos_ == "NOUN"],
        "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"],
        "response_timestamp": datetime.datetime.now().timestamp(),
    }

    print(res)

    return res


if __name__ == '__main__':
    app.run(port=5010)
