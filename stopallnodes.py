import os
nodes = []
for i in range(1,45):
    nodes.append('g30'+str(i).rjust(2,'0'))

print nodes

for node in nodes: 
    if not node.endswith('29'):
        print node
        cmd = "ssh %s docker ps  | grep 'presto' | gawk '{ print $1 }' | xargs -n 1 echo " % node
        os.system(cmd)
        cmd = "ssh %s docker ps | grep 'presto' | gawk '{ print $1 }' | xargs -n 1 ssh %s /home/zhuww/local/src/presto3-docker/rmcontainer.sh" %( node, node)
        print cmd
        os.system(cmd)
