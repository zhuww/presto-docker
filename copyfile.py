#!/usr/bin//python

import os
from subprocess import Popen, PIPE, check_call

container = "presto"



#print("docker cp ~/local/src/presto-docker/DDplan.py %s:/home/psr/software/presto/bin/"%container)
#os.system("docker cp ~/local/src/presto-docker/DDplan.py %s:/home/psr/software/presto/bin/"%container)
#print("docker cp ~/local/src/presto-docker/fastpipe %s:/home/psr/software/presto/bin/"%container)
#os.system("docker cp ~/local/src/presto-docker/fastpipe %s:/home/psr/software/presto/bin/"%container)
print("docker cp ~/local/src/presto-docker/sifting.py %s:/home/psr/software/presto/lib/python/"%container)
os.system("docker cp ~/local/src/presto-docker/sifting.py %s:/home/psr/software/presto/lib/python/"%container)
#print("docker cp ~/local/src/presto-docker/makezap.py %s:/home/psr/software/presto/bin/"%container)
#os.system("docker cp ~/local/src/presto-docker/makezap.py %s:/home/psr/software/presto/bin/"%container)
#print("docker cp ~/local/src/presto-docker/stopall %s:/usr/local/bin/"%container)
#os.system("docker cp ~/local/src/presto-docker/stopall %s:/usr/local/bin/"%container)
print("docker commit %s"%container)
os.system("docker commit %s"%container)


