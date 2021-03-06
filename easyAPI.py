from flask import Flask, abort, request, jsonify
from summa import summarizer
from textrank4zh import TextRank4Sentence
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import logging

app = Flask(__name__)

@app.route('/get_abstract', methods=['POST'])
def get_task():
    if not request.form:
        return 'Missing parameter'
    if 'language' not in request.form:
        return 'Missing language'
    if 'text' not in request.form:
        return 'Missing text'

    language = request.form.get("language")
    text = request.form.get('text')

    if language == 'english':
        abstract = summarizer.summarize(text)
        if abstract.strip() == '':
            return jsonify({'abstract': text})
        return jsonify({'abstract' : abstract})
    elif language == 'chinese':
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source='all_filters')

        if len(tr4s.get_key_sentences()) < 3:
            return jsonify({'abstract': text})
        abstract = ''
        for item in tr4s.get_key_sentences(num=3):
            abstract += item.sentence + '\n'
        return jsonify({'abstract': abstract.strip()})
    elif language == 'japanese':
        parser = PlaintextParser.from_string(text, Tokenizer(language))
        stemmer = Stemmer(language)

        summar = LsaSummarizer(stemmer)
        summar.stop_words = get_stop_words(language)

        if len(summar(parser.document, 3)) < 3:
            return jsonify({'abstract': text})
        abstract = ''
        for sentence in summar(parser.document, 3):
            abstract += str(sentence) + '\n'
        return jsonify({'abstract': abstract.strip()})

    return language + 'is not supported.'


if __name__ == "__main__":
    handler = logging.FileHandler("flask.log", encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=80)
