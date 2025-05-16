# @title import
import pymorphy2
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from matplotlib import pyplot as plt

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('punkt_tab')
# @title Functions
def summarization(text, sent_count, lang):
  sentences = sent_tokenize(text, language=lang)
  stop_words = set(stopwords.words(lang))
  words = word_tokenize(text)
  words = [word.lower() for word in words if word.isalpha()]
  words = [word for word in words if word not in stop_words]
  morph = pymorphy2.MorphAnalyzer()
  words = [morph.parse(word)[0].normal_form for word in words]
  freq_dist = FreqDist(words)
  sentence_scores = {}

  for i, sentence in enumerate(sentences):
    sentence_words = word_tokenize(sentence.lower())
    morph = pymorphy2.MorphAnalyzer()
    sentence_words = [morph.parse(word)[0].normal_form for word in sentence_words]
    sentence_score = sum([freq_dist[word] for word in sentence_words if word in freq_dist])

    sentence_scores[i] = sentence_score
  sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
  selected_sentences = sorted_scores[:sent_count]
  selected_sentences = sorted(selected_sentences)

  # Формируем суммаризацию
  summary = ' '.join([sentences[i] for i, _ in selected_sentences])
  return summary