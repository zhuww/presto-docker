#!/bin/bash
for i in {11..23}; do echo node$i;  ssh node$i ~/local/src/presto3-docker/start.sh; done
#for i in {16..18}; do echo node$i;  ssh node$i ~/local/src/presto-docker/start.sh; done
