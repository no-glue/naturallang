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
