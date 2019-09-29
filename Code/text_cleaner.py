import re
import json
import sys
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

input_file = sys.argv[1]
# output_file = sys.argv[2]
inp = open(input_file, 'r')
# out = open(output_file, 'w+')
final_sriven = []
text = inp.readlines()
output_text = []
for line in text:
	reg = False
	x = []
	for y in x:
		if y != None:
			reg = True
	line = re.sub("\(.*\)", '', line)
	line = re.sub("Fig. [0-9]\.[0-9]{1,3}", 'SrivenShreyasAni', line)
	line = re.sub("Figure [0-9]\.[0-9]{1,3}", 'SrivenShreyasAni', line)
	line = re.sub("Table [0-9]\.[0-9]{1,3}", 'SrivenShreyasAni', line)
	line = re.sub("Equation", 'SrivenShreyasAni', line)
	line = re.sub("Eq.", 'SrivenShreyasAni', line)
	line = re.sub("Problem [0-9]\.[0-9]{1,3}", 'SrivenShreyasAni', line)
	line = re.sub("Example [0-9]\.[0-9]{1,3}", 'SrivenShreyasAni', line)
	line = re.sub("\n", '', line)
	line = re.sub("^\*", 'SrivenShreyasAni', line)
	line = re.sub("\s+", ' ', line)
	if not line or line == ' ':
		continue
	if reg is False:
		output_text.append(line)
text = ''
for line in  output_text:
	text = text + "\n" + line
sentences = sent_tokenize(text)
final_sent = [line for line in sentences if(len(word_tokenize(line)) in range(10,100))]
for line in final_sent:
	line = re.sub("^[0-9]\.[0-9]{1,3}.*\n", '', line)
	reg = False
	x = []
	x.append(re.search("We ", line))
	x.append(re.search(" we ", line))
	x.append(re.search("These", line))
	x.append(re.search("He ", line))
	x.append(re.search(" he ", line))
	x.append(re.search("She ", line))
	x.append(re.search(" she ", line))
	x.append(re.search("You ", line))
	x.append(re.search(" you ", line))
	x.append(re.search("Those", line))
	x.append(re.search("However", line))
	x.append(re.search("Now", line))
	x.append(re.search("Hence", line))
	x.append(re.search("Chapter", line))
	x.append(re.search("Since", line))
	x.append(re.search("Who ", line))
	x.append(re.search("Which", line))
	x.append(re.search("How ", line))
	x.append(re.search("Can ", line))
	x.append(re.search("Whose ", line))
	x.append(re.search("Where ", line))
	x.append(re.search("Why ", line))
	x.append(re.search("\?", line))
	x.append(re.search("If", line))
	x.append(re.search("Consider", line))
	x.append(re.search("SrivenShreyasAni", line))
	for y in x:
		if y != None:
			reg = True
	if reg is True:
		continue
	final_sriven.append (line)
# print (final_sriven)

final_sriven = " ".join(final_sriven)





















from summa.summarizer import summarize
from nltk.tokenize import sent_tokenize
import sys

text = final_sriven

filename = open ("temp.txt", "w")
filename.write (text)
filename.close ()

# filename = open ("temp.txt")

summary_2 = summarize(text, ratio=0.5)

summary_2 = sent_tokenize(summary_2)
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

parser = PlaintextParser.from_file("temp.txt", Tokenizer("english"))
# parser = 

from sumy.summarizers.luhn import LuhnSummarizer
summarizer_1 = LuhnSummarizer()
summary_struct_1 =summarizer_1(parser.document,100)
summary_1 = [ i.__unicode__() for i in summary_struct_1] 

summary = summary_1 + summary_2 

def match_function (a, b):
	wa = a.split(' ')
	wb = b.split(' ')
	count = 0
	for i in wa:
		if i in wb:
			count += 1
	if (count >= len(wa)*0.8):
		return True
	return False

results = []
for i in summary_1:
	for j in summary_2:
		if match_function(i,j):
			results.append (i)

final_ani = results

# print (final_ani)























from pytextrank import parse_doc, normalize_key_phrases, json_iter, pretty_print, render_ranks, text_rank
import sys
import ast
import pke
import os
import json
from try2 import one
from try1 import two, three, five, six, seven, eight, nine

json_bio = final_ani

final_swaraj = {}
for entry in json_bio:
	methods = []
	# methods.append (one (entry))
	# methods.append (two (entry))
	methods.append (three (entry))
	# methods.append (six (entry))
	# methods.append (seven (entry))
	# methods.append (nine (entry))
	# print (methods)
	result = {}
	for x in methods:
		for y in x:
			if y in result:
				result[y[0]] += y[1]
			else:
				result[y[0]] = y[1]

	ans_labels = sorted(result, key=result.get)
	ans_labels = ans_labels[:7]
	# print (type(ans_labels))
	# print ()
	final_swaraj [entry] = ans_labels
	# print (entry, ans_labels)
	print ()

output_final_final_finales = open ("output_final_final_finales.json", "w", encoding='utf-8')

for element, value in final_swaraj.items():
	json_data = {"text":element, "fibs":value}
	json.dump (json_data, output_final_final_finales, ensure_ascii=False)
	output_final_final_finales.write ('\n')

output_final_final_finales.close()


