There are three Python programs here (`-h` for usage):

 - `./decode` a simple non-reordering (monotone) phrase-based decoder
 - `./grade` computes the model score of your output

The commands are designed to work in a pipeline. For instance, this is a valid invocation:

    ./decode | ./grade


The `data/` directory contains the input set to be decoded and the models

 - `data/input` is the input text

 - `data/lm` is the ARPA-format 3-gram language model

 - `data/tm` is the phrase translation model


Order of experiments:
 - Default
 - Adjective and noun switching
 - Added in future cost (https://www.cs.jhu.edu/~jason/465/PowerPoint/lect32b-mt-decoding.pdf)
 - Took Hao's future cost
 - Fixed adj/noun switching to adjacent words, added in Spanish-special knowledge

