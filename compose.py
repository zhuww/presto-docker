#!/usr/bin//python

import os
from subprocess import Popen, PIPE, check_call

#start up presto service
check_call(["docker-compose","up","-d"])
p = Popen(["docker","ps","-aq"],stdout=PIPE,stderr=PIPE)
p.wait()

#copy public keys into root and psr user directories
container = "presto3"
#print("docker cp ~/.ssh/id_rsa.pub %s:/root/.ssh/authorized_keys"%container)
#os.system("docker cp ~/.ssh/id_rsa.pub %s:/root/.ssh/authorized_keys"%container)
#print("docker cp ~/.ssh/id_rsa.pub %s:/home/psr/.ssh/authorized_keys"%container)
#os.system("docker cp ~/.ssh/id_rsa.pub %s:/home/psr/.ssh/authorized_keys"%container)

print("docker cp ./prestoall  %s:/home/psr/software/presto/bin/"%container)
os.system("docker cp ./prestoall  %s:/home/psr/software/presto/bin/"%container)
print("docker cp ./DDplan.py %s:/home/psr/software/presto/bin/"%container)
os.system("docker cp ./DDplan.py %s:/home/psr/software/presto/bin/"%container)
print("docker cp ./rrattrap.py %s:/home/psr/software/presto/bin/"%container)
os.system("docker cp ./rrattrap.py %s:/home/psr/software/presto/bin/"%container)
print("docker cp ./threadit.py %s:/home/psr/software/presto/lib/python/"%container)
os.system("docker cp ./threadit.py %s:/home/psr/software/presto/lib/python/"%container)
print("docker cp ./psrfits.py %s:/home/psr/software/presto/lib/python/"%container)
os.system("docker cp ./psrfits.py %s:/home/psr/software/presto/lib/python/"%container)
print("docker cp ./bary_and_topo.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
os.system("docker cp ./bary_and_topo.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
print("docker cp ./rrattrap_config.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
os.system("docker cp ./rrattrap_config.py %s:/home/psr/software/presto/lib/python/singlepulse/"%container)
print("docker cp ./obsys.dat %s:/home/psr/software/tempo/"%container)
os.system("docker cp ./obsys.dat %s:/home/psr/software/tempo/"%container)
#print("docker cp ./misc_utils.c %s:/home/psr/software/presto/src"%container)
#os.system("docker cp ./misc_utils.c %s:/home/psr/software/presto/src/"%container)
