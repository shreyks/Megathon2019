import re
import sys
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

input_file = sys.argv[1]
output_file = sys.argv[2]

inp = open(input_file, 'r')
out = open(output_file, 'w+')

text = inp.readlines()
output_text = []

for line in text:

	reg = False
	x = []

	# x.append(re.search("Fig. [0-9]\.[0-9]", line))
	# x.append(re.search("Figure [0-9]\.[0-9]", line))
	# x.append(re.search("Table [0-9]\.[0-9]", line))
	# x.append(re.search("Equation [0-9]\.[0-9]", line))
	# x.append(re.search("Eq.", line))
	# x.append(re.search("Problem [0-9]\.[0-9]", line))

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
	# line = re.sub("^[0-9]{1,2}\.", '', line)
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

	# x.append(re.search("^(We)\b", line))
	# x.append(re.search("\b(We|we)\b", line))
	# x.append(re.search("\b(We|we)\b", line))
	# x.append(re.search("\b(We|we)\b", line))

	for y in x:
		if y != None:
			# print("------------------------------" + line + "-------------------------------------")
			reg = True

	if reg is True:
		continue

	# out.write("BEGIN---------------------%s---------------END\n" % line)
	out.write("%s\n" % line)
