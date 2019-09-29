
from pytextrank import parse_doc, normalize_key_phrases, json_iter, pretty_print, render_ranks, text_rank
import sys
import ast
import os

def one (text):

	path_stage0 = "tempfile.json"
	path_stage1 = "o1.json"
	path_stage2 = "o2.json"

	f = open ("tempfile.json", "w")
	f.write ("{\"id\":\"777\", \"text\":\"" + text + "\"}")
	f.close()

	with open(path_stage1, 'w') as f:
	    for graf in parse_doc(json_iter(path_stage0)):
	        f.write("%s\n" % pretty_print(graf._asdict()))

	graph, ranks = text_rank(path_stage1)
	render_ranks(graph, ranks)

	outputs = []
	with open(path_stage2, 'w') as f:
	    for rl in normalize_key_phrases(path_stage1, ranks):
	        ans = "%s\n" % pretty_print(rl._asdict())
	        output = ast.literal_eval(ans)
	        outputs.append ((output["text"], output["rank"]))

	os.remove("tempfile.json")

	return outputs

# text = "The earliest recorded model for planetary motions proposed by Ptolemy about 2000 years ago was a ‘geocentric’ model in which all celestial objects, stars, the sun and the planets, all revolved around the earth."
# print (one("The earliest recorded model for planetary motions proposed by Ptolemy about 2000 years ago was a ‘geocentric’ model in which all celestial objects, stars, the sun and the planets, all revolved around the earth."))