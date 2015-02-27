#!/usr/bin/env python
import argparse # optparse is deprecated
from itertools import islice # slicing for iterators
from collections import Counter

function_words = ["you", "i", "to", "the", "a", "and", "that", "it", "of", "me", "what", "is", "in", "this", "know", "i'm", "for", "no", "have", "my", "don't", "just", "not", "do", "be", "on", "your", "was", "we", "it's", "with", "so", "but", "all", "well", "are", "he", "oh", "about", "right"]

C_function = Counter(function_words)
for item in C_function.keys():
	C_function[item] = 10

def har_mean(p, r, a):
    den = (a * p + (1 - a) * r)
    if den == 0: return 0.0
    return p * r / den

def simple_meteor(h, ref, alpha, delta):

    m_function = float(sum((Counter(h) & Counter(ref) & C_function).viewvalues()))
    m_content = float(sum((Counter(h) & Counter(ref)).viewvalues())) - m_function

    p = ((delta * m_content) + ((1 - delta) * m_function)) / len(h)
    r = ((delta * m_content) + ((1 - delta) * m_function)) / len(ref)

    return har_mean(p, r, alpha)
 
def main():
    parser = argparse.ArgumentParser(description='Evaluate translation hypotheses.')
    # PEP8: use ' and not " for strings
    parser.add_argument('-i', '--input', default='data/train-test.hyp1-hyp2-ref',
            help='input file (default data/train-test.hyp1-hyp2-ref)')
    parser.add_argument('-n', '--num_sentences', default=None, type=int,
            help='Number of hypothesis pairs to evaluate')
    parser.add_argument('-a', '--alpha', default=0.5, type=float, help='precision/recall weight parameter')
    parser.add_argument('-d', '--delta', default=0.5, type=float, help='content/function word weight parameter')
    # note that if x == [1, 2, 3], then x[:None] == x[:] == x (copy); no need for sys.maxint
    opts = parser.parse_args()
 
    # we create a generator and avoid loading all sentences into a list
    def sentences():
        with open(opts.input) as f:
            for pair in f:
                yield [sentence.strip().split() for sentence in pair.lower().split(' ||| ')]
 
    # note: the -n option does not work in the original code
    for h1, h2, ref in islice(sentences(), opts.num_sentences):
        h1_val = simple_meteor(h1, ref, opts.alpha, opts.delta)
        h2_val = simple_meteor(h2, ref, opts.alpha, opts.delta)

        if h1_val != 0 and h2_val != 0:
		if (h1_val / h2_val) > 1.0002:
			print -1
		elif (h1_val / h2_val) <= 1.0002 and (h1_val / h2_val) >= 0.9998:
			print 0
		else:
			print 1
	elif h2_val == 0:
		print -1
	else:
		print 1
 
# convention to allow import of this file as a module
if __name__ == '__main__':
    main()
