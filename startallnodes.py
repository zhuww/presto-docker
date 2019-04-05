import os
nodes = []
for i in range(1,45):
    nodes.append('g30'+str(i).rjust(2,'0'))

print nodes

for node in nodes: 
    if not node.endswith('29'):
        print node
        cmd = 'ssh %s /home/zhuww/local/src/presto3-docker/start.sh' % node
        print cmd
        os.system(cmd)
