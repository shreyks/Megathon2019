from pytextrank import parse_doc, normalize_key_phrases, json_iter, pretty_print, render_ranks, text_rank
import sys
import ast
import pke
import os
import json
from try2 import one
from try1 import two, three, five, six, seven, eight, nine

text = "In some plants living in very dry habitats, the epidermis may be thicker since protection against water loss is critical."

json_bio = []

out = open ("result.txt", "a")

f1_scores = []
for entry in json_bio:
	count = 0
	methods = []
	methods.append (one (entry["text"]))
	methods.append (two (entry["text"]))
	methods.append (three (entry["text"]))
	methods.append (six (entry["text"]))
	methods.append (seven (entry["text"]))
	methods.append (nine (entry["text"]))
	result = {}
	for x in methods:
		for y in x:
			if y in result:
				result[y[0]] += y[1]
			else:
				result[y[0]] = y[1]

	ans_labels = sorted(result, key=result.get)
	print (type(ans_labels))
	print (entry["fibs"], ans_labels)
	for m in entry["fibs"]:
		if m[-1] == ' ':
			m = m[0:-1]
		if m in ans_labels:
			count += 1
	precision = count / len(ans_labels)
	recall = count / len(entry["fibs"])
	print ("precision = ", precision, "recall = ", recall)
	if precision == 0 and recall == 0:
		f1_score = 0
	else:
		f1_score = (2*precision*recall) / (precision+recall)
	f1_scores.append (f1_score)
	print ("F1 score = ", f1_score)
print (f1_scores)
print ("average = ", sum(f1_scores) / len(f1_scores))
out.write (str(sum(f1_scores) / len(f1_scores)))


# print (ans1)
# print ()
# print (ans2)
# print ()
# print (ans3)
# print ()
# print (ans5)
# print ()
# print (ans6)
# print ()
# print (ans7)
# print ()
# print (ans8)
# print ()
# print (ans9)

