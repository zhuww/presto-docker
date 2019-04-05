#!/bin/bash
for i in {11..24}; do echo node$i;  ssh node$i docker ps; done
#for i in {16..18}; do echo node$i;  ssh node$i ~/local/src/presto-docker/start.sh; done
