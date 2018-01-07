#!/bin/bash
for i in {2..15}; do  ssh node$i ~/local/src/presto-docker/stoppipe; done
