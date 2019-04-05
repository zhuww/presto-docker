# Copyright (C) 2016 by Ewan Barr
# Licensed under the Academic Free License version 3.0
# This program comes with ABSOLUTELY NO WARRANTY.
# You are free to modify and redistribute this code as long
# as you do not remove the above attribution and reasonably
# inform receipients that you have modified the original work.

FROM ubuntu:xenial-20160923.1

#MAINTAINER Ewan Barr "ebarr@mpifr-bonn.mpg.de"
MAINTAINER Weiwei Zhu "zhuww@nao.cas.cn" 
#adopted from Ewan Barr's repo

# Suppress debconf warnings
ENV DEBIAN_FRONTEND noninteractive

# Switch account to root and adding user accounts and password
USER root
RUN echo "root:root" | chpasswd && \
    mkdir -p /root/.ssh 

# Create psr user which will be used to run commands with reduced privileges.
RUN adduser --disabled-password --gecos 'unprivileged user' psr && \
    echo "psr:psr" | chpasswd && \
    mkdir -p /home/psr/.ssh && \
    chown -R psr:psr /home/psr/.ssh

# Create space for ssh daemon and update the system
#RUN echo 'deb http://us.archive.ubuntu.com/ubuntu trusty main multiverse' >> /etc/apt/sources.list && \
RUN echo 'deb mirror://mirrors.ubuntu.com/mirrors.txt trusty main multiverse' >> /etc/apt/sources.list && \
    mkdir /var/run/sshd && \
    apt-get -y check && \
    apt-get -y update && \
    apt-get install -y apt-utils apt-transport-https software-properties-common python-software-properties && \
    apt-get -y update --fix-missing && \
    apt-get -y upgrade 

# Install dependencies
RUN apt-get -y update --fix-missing
RUN apt-get --no-install-recommends -y install \
    build-essential \
    autoconf \
    autotools-dev \
    automake \
    pkg-config \
    csh \
    gcc \
    gfortran \
    wget \
    git \
    libcfitsio-dev \
    pgplot5 \
    swig2.0 \    
    python \
    python-dev \
    python-pip \
    python-tk  \
    libfftw3-3 \
    libfftw3-bin \
    libfftw3-dev \
    libfftw3-single3 \
    libx11-dev \
    libpng12-dev \
    libpng3 \
    libpnglite-dev \   
    libglib2.0-0 \
    libglib2.0-dev \
    libblas-dev \
    libgtk3.0-cil-dev \
    gir1.2-gtk-3.0 \
    python-gobject \
    openssh-server \
    libgomp1 \
    openmpi-bin \
    openmpi-common \
    openmpi-doc \
    libpomp-dev \
    libopenmpi-dev \
    libiomp-dev \
    libiomp-doc \
    libiomp5 \
    libiomp5-dbg \
    docker.io \
    xorg \
    openbox \
    imagemagick \
    vim \
    latex2html \
    && rm -rf /var/lib/apt/lists/* 

#RUN apt-get install -y parallel

RUN apt-get -y clean

# Install python packages
ENV PIP_FIND_LINKS https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U 
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple setuptools -U
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -Iv scipy==0.19.1
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy==1.13.3
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib==2.1.0
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple astropy==2.0.8 
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyfits 
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple fitsio
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pywavelets

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -Iv scikit-learn==0.12.1
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -Iv theano==0.8.1
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pika
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple redis
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple rq

#COPY sshd_config /etc/ssh/sshd_config
USER psr

# Define home, psrhome, OSTYPE and create the directory
ENV HOME /home/psr
ENV PSRHOME $HOME/software
ENV OSTYPE linux
RUN mkdir -p $PSRHOME

# PGPLOT
ENV PGPLOT_DIR /usr/lib/pgplot5
ENV PGPLOT_FONT /usr/lib/pgplot5/grfont.dat
ENV PGPLOT_INCLUDES /usr/include
ENV PGPLOT_BACKGROUND white
ENV PGPLOT_FOREGROUND black
ENV PGPLOT_DEV /xs
WORKDIR $PSRHOME

# Pull all repos
RUN wget http://www.atnf.csiro.au/people/pulsar/psrcat/downloads/psrcat_pkg.tar.gz  
RUN tar -xvf psrcat_pkg.tar.gz -C $PSRHOME 
RUN git clone git://git.code.sf.net/p/tempo/tempo
RUN git clone https://github.com/scottransom/pyslalib.git 

RUN git clone https://github.com/scottransom/presto.git 


# Psrcat
ENV PSRCAT_FILE $PSRHOME/psrcat_tar/psrcat.db
ENV PATH $PATH:$PSRHOME/psrcat_tar
WORKDIR $PSRHOME/psrcat_tar
RUN /bin/bash makeit && \
    rm -f ../psrcat_pkg.tar.gz

#PICS AI 
WORKDIR $PSRHOME
RUN git clone https://github.com/zhuww/ubc_AI.git
ENV PICS $PSRHOME/ubc_AI/
ENV PYTHONPATH $PSRHOME
RUN echo "alias pfdviewer='python $PICS/pfdviewer.py'" >> ~/.bashrc && \
   echo "alias quickclf='python $PICS/batchclf.py'" >> ~/.bashrc

# Tempo
ENV TEMPO $PSRHOME/tempo
ENV PATH $PATH:$PSRHOME/tempo/bin
WORKDIR $TEMPO
RUN ls -lrt 
RUN ./prepare && \
    ./configure --prefix=$PSRHOME/tempo && \
    make && \
    make install 
    #&& \
    #rm -rf .git
    #mv obsys.dat obsys.dat_ORIGINAL && \
    #wget https://raw.githubusercontent.com/mserylak/pulsar_docker/master/tempo/obsys.dat && \

# pyslalib
ENV PYSLALIB $PSRHOME/pyslalib
ENV PYTHONPATH $PYTHONPATH:$PYSLALIB/install
WORKDIR $PYSLALIB
RUN python setup.py install --record list.txt --prefix=$PYSLALIB/install && \
    python setup.py clean --all 
    #rm -rf .git

#RUN pip uninstall scipy
#RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scipy==0.19.1

# Presto
ENV PRESTO $PSRHOME/presto
#ENV PRESTO /home/psr/software/presto
ENV PATH $PATH:$PRESTO/bin
ENV LD_LIBRARY_PATH $PRESTO/lib
ENV PYTHONPATH $PYTHONPATH:$PRESTO/lib/python

#WORKDIR $PRESTO/src
WORKDIR /home/psr/software/presto/src
#RUN rm -rf ../.git
RUN  echo $PRESTO 
RUN  echo `pwd` 
RUN  ls  | echo
RUN  make makewisdom
RUN  make prep
RUN  make 
RUN  make mpi
WORKDIR $PRESTO/python/ppgplot_src
#RUN mv _ppgplot.c _ppgplot.c_ORIGINAL && \
    #wget https://raw.githubusercontent.com/mserylak/pulsar_docker/master/ppgplot/_ppgplot.c
WORKDIR $PRESTO/python
RUN make && \
    echo "export PYTHONPATH=$PYTHONPATH:$PRESTO/lib/python:$PSRHOME" >> ~/.bashrc

RUN env | awk '{print "export ",$0}' >> $HOME/.profile
WORKDIR $HOME
USER root
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
ENV DISPLAY :0
#RUN apt-get install -y eog 
