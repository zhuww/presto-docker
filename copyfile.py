#!/usr/bin//python

import os
from subprocess import Popen, PIPE, check_call

container = "10.134.1.60:5000/admin/presto"



print("docker cp ~/local/src/presto3-docker/DDplan.py %s:/home/psr/software/presto/bin/"%container)
os.system("docker cp ~/local/src/presto3-docker/DDplan.py %s:/home/psr/software/presto/bin/"%container)
print("docker cp ~/local/src/presto3-docker/fastpipe %s:/home/psr/software/presto/bin/"%container)
os.system("docker cp ~/local/src/presto3-docker/fastpipe %s:/home/psr/software/presto/bin/"%container)
print("docker cp ~/local/src/presto3-docker/sifting.py %s:/home/psr/software/presto/lib/python/"%container)
os.system("docker cp ~/local/src/presto3-docker/sifting.py %s:/home/psr/software/presto/lib/python/"%container)
print("docker cp ~/local/src/presto3-docker/rrattrap.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
os.system("docker cp ~/local/src/presto3-docker/rrattrap.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
print("docker cp ~/local/src/presto3-docker/rrattrap_config.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
os.system("docker cp ~/local/src/presto3-docker/rrattrap_config.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
print("docker cp ~/local/src/presto3-docker/bary_and_topo.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
os.system("docker cp ~/local/src/presto3-docker/bary_and_topo.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
print("docker cp ~/local/src/presto3-docker/psrfits.py %s:/home/psr/software/presto/lib/python/"%container)
os.system("docker cp ~/local/src/presto3-docker/psrfits.py %s:/home/psr/software/presto/lib/python/"%container)
print("docker cp -r ~/local/src/presto3-docker/singlepulse/* %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
os.system("docker cp -r ~/local/src/presto3-docker/singlepulse/* %s:/home/psr/software/presto/lib/python/singlepulse/"%container)

print("docker cp ~/local/src/presto3-docker/filterbankfile.py %s:/home/psr/software/presto/lib/python/"%container)
os.system("docker cp ~/local/src/presto3-docker/filterbankfile.py %s:/home/psr/software/presto/lib/python/"%container)
#print("docker cp ~/local/src/presto3-docker/sigproc_fb.c %s:/home/psr/software/presto/lib/python/"%container)
#os.system("docker cp ~/local/src/presto3-docker/sigproc_fb.c %s:/home/psr/software/presto/lib/python/"%container)
print("docker cp ~/local/src/presto3-docker/makezap.py %s:/home/psr/software/presto/bin/"%container)
os.system("docker cp ~/local/src/presto3-docker/makezap.py %s:/home/psr/software/presto/bin/"%container)
print("docker cp ~/local/src/presto3-docker/stopall %s:/usr/local/bin/"%container)
os.system("docker cp ~/local/src/presto3-docker/stopall %s:/usr/local/bin/"%container)
print("docker commit %s"%container)
os.system("docker commit %s"%container)


