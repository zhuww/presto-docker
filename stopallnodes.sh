#!/bin/bash
for i in {2..15}; do echo node$i;  ssh node$i ~/local/src/presto-docker/stoppipe; done
