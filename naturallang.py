def lexical_diversity(text):
  """Gets lexical diversity

  """
  return len(text) / len(set(text))

def percentage(count, total):
  """Gets percentage

  """
  return 100 * count / total

def gutenberg_stats(gutenberg):
  """Gets text stats

  """
  for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(gutenberg.words(fileid)))
    
    print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

def conditional_freq(nltk, words_list, text):
  """Gets conditional frequency of words
  
  """
  return nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in text.fileids()
    for w in text.words(fileid)
    for target in words_list
    if w.lower().startswith(target))

def cumulative_word_length(nltk, languages, text):
  """Gets cumulative lengths for text
  
  """
  return nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in text.words(lang + '-Latin1'))
