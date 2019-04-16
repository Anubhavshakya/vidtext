import nltk.data
def summary(data):
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	return tokenizer.tokenize(data)

def Text(sourceData):
	return sourceData