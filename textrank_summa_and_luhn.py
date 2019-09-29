from summa.summarizer import summarize
from nltk.tokenize import sent_tokenize
import sys 

filename = sys.argv[1]

text = open(filename)
text = text.read() 
summary_2 = summarize(text, ratio=0.5)
    # print(summary_2)

summary_2 = sent_tokenize(summary_2)
# print(summary_2)
from sumy.parsers.plaintext import PlaintextParser
#for tokenization
from sumy.nlp.tokenizers import Tokenizer

# filename = "bio-cleaned" 
parser = PlaintextParser.from_file(filename, Tokenizer("english"))

from sumy.summarizers.luhn import LuhnSummarizer
summarizer_1 = LuhnSummarizer()
summary_struct_1 =summarizer_1(parser.document,100)
summary_1 = [ i.__unicode__() for i in summary_struct_1] 
# for sentence in summary_1:
#  print(sentence)
# print(type(summary_1))
# print(type(summary_2))
summary = summary_1 + summary_2 
# print (summary_1)
# print ()
# print ()
# print ()
# print ()
# print ()
# print ()
# print (summary_2)

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

# print (match_function("'Historically it was the Italian Physicist Galileo who recognised the fact that all bodies, irrespective of their masses, are accelerated towards the earth with a constant acceleration.',", "['Historically it was the Italian Physicist Galileo who recognised the fact that all bodies, irrespective of their masses, are accelerated towards the earth with a constant acceleration.'"))


results = []
for i in summary_1:
    for j in summary_2:
        if match_function(i,j):
            results.append (i)

# result_array = {}

# for i in summary:
#     if i in result_array:
#         result_array[i] += 1
#     else:
#         result_array[i] = 0

# sorted (result_array,key = result_array.get)
# print (result_array)
    
# for i in results:
#     print (i)

# f= open("selected_lines.txt","w+")