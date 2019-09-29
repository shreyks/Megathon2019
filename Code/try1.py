import pke
import os

def two (text):
	extractor = pke.unsupervised.TopicRank()
	f = open ("input.txt", "w")
	f.write (text)
	f.close ()
	extractor.load_document(input='input.txt', language='en')
	extractor.candidate_selection()
	extractor.candidate_weighting()
	keyphrases = extractor.get_n_best(n=10)
	return keyphrases
def three (text):
	extractor = pke.unsupervised.SingleRank()
	f = open ("input.txt", "w")
	f.write (text)
	f.close ()
	extractor.load_document(input='input.txt', language='en')
	extractor.candidate_selection()
	extractor.candidate_weighting()
	keyphrases = extractor.get_n_best(n=10)
	return keyphrases
def five (text):
	extractor = pke.unsupervised.YAKE()
	f = open ("input.txt", "w")
	f.write (text)
	f.close ()
	extractor.load_document(input='input.txt', language='en')
	extractor.candidate_selection()
	extractor.candidate_weighting()
	keyphrases = extractor.get_n_best(n=10)
	return keyphrases
def six (text):
	extractor = pke.unsupervised.TextRank()
	f = open ("input.txt", "w")
	f.write (text)
	f.close ()
	extractor.load_document(input='input.txt', language='en')
	extractor.candidate_selection()
	extractor.candidate_weighting()
	keyphrases = extractor.get_n_best(n=10)
	return keyphrases
def seven (text):
	extractor = pke.unsupervised.TextRank()
	f = open ("input.txt", "w")
	f.write (text)
	f.close ()
	extractor.load_document(input='input.txt', language='en')
	extractor.candidate_selection()
	extractor.candidate_weighting()
	keyphrases = extractor.get_n_best(n=10)
	return keyphrases
def eight (text):
	extractor = pke.unsupervised.TopicalPageRank()
	f = open ("input.txt", "w")
	f.write (text)
	f.close ()
	extractor.load_document(input='input.txt', language='en')
	extractor.candidate_selection()
	extractor.candidate_weighting()
	keyphrases = extractor.get_n_best(n=10)
	return keyphrases
def eight (text):
	pos = {'NOUN', 'PROPN', 'ADJ'}
	grammar = "NP: {<ADJ>*<NOUN|PROPN>+}"
	extractor = pke.unsupervised.PositionRank()
	f = open ("input.txt", "w")
	f.write (text)
	f.close ()
	extractor.load_document(input='path/to/input', language='en', normalization=None)
	extractor.candidate_selection(grammar=grammar, maximum_word_number=3)
	extractor.candidate_weighting(window=10, pos=pos)
	keyphrases = extractor.get_n_best(n=10)
	return keyphrases
def nine (text):
	extractor = pke.unsupervised.MultipartiteRank()
	f = open ("input.txt", "w")
	f.write (text)
	f.close ()
	extractor.load_document(input='input.txt', language='en')
	extractor.candidate_selection()
	extractor.candidate_weighting()
	keyphrases = extractor.get_n_best(n=10)
	return keyphrases

# print (two ("s"))


# print (two ("The gravitational force is a conservative force, and therefore a potential energy function can be defined."))

