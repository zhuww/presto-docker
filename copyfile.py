#!/usr/bin//python

import os
from subprocess import Popen, PIPE, check_call

container = "presto"



#print("docker cp ~/local/src/presto-docker/DDplan.py %s:/home/psr/software/presto/bin/"%container)
#os.system("docker cp ~/local/src/presto-docker/DDplan.py %s:/home/psr/software/presto/bin/"%container)
#print("docker cp ~/local/src/presto-docker/fastpipe %s:/home/psr/software/presto/bin/"%container)
#os.system("docker cp ~/local/src/presto-docker/fastpipe %s:/home/psr/software/presto/bin/"%container)
print("docker cp ~/local/src/presto-docker/makezap.py %s:/home/psr/software/presto/bin/"%container)
os.system("docker cp ~/local/src/presto-docker/makezap.py %s:/home/psr/software/presto/bin/"%container)
