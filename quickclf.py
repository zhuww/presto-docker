import numpy as np
import os
import cPickle, glob, ubc_AI
from ubc_AI.data import pfdreader
AI_PATH = '/'.join(ubc_AI.__file__.split('/')[:-1])
classifier = cPickle.load(open(AI_PATH+'/trained_AI/clfl2_PALFA.pkl','rb'))
#classifier = cPickle.load(open(AI_PATH+'/trained_AI/clfl2_BD.pkl','rb'))
pfdfile = glob.glob('*.pfd') 
spdfile = glob.glob('*.spd')
pfd_scores = np.array(classifier.report_score([pfdreader(f) for f in pfdfile]))
spd_scores = np.array(classifier.report_score([pfdreader(f) for f in spdfile]))
AI_scores = np.hstack((pfd_scores, spd_scores))
allfile = np.hstack((pfdfile, spdfile))

argindex = np.argsort(AI_scores)[::-1]
pfdindex = np.argsort(pfd_scores)[::-1]

text = '\n'.join(['%s %s' % (allfile[i], AI_scores[i]) for i in argindex])
fout = open('clfresult.txt', 'w')
fout.write(text)
fout.close()
for f in [pfdfile[i] for i in pfdindex if pfd_scores[i] > 0.1]:
    os.system('show_pfd %s' % f)
