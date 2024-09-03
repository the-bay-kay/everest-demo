FROM nodered/node-red:2.2.3
RUN npm install node-red-dashboard
RUN npm install node-red-contrib-ui-actions
RUN npm install node-red-node-ui-table
RUN npm install node-red-contrib-ui-level

RUN arch=$(uname -m) && \
    if [ "$arch" = "x86_64" ]; then \
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"; \
    elif [ "$arch" = "aarch64" ]; then \
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh"; \
    else \
    echo "Unsupported architecture: $arch"; \
    exit 1; \
    fi && \
    wget $MINICONDA_URL -O miniconda.sh && \
    bash miniconda.sh -b -u -p /usr/src/node-red && \
    rm -f miniconda.sh

RUN conda --version

# The method below attempts to run this via PIP... Since I have been
# Unable to get the `USER root` command to correctly give 
#USER root
#RUN apk update && \
#    apk add --virtual python-dev 
# python3-pip python3-numpy python3-pandas python3-control
# RUN pip install control numpy

#RUN apk add --update --no-cache py3-pip-20.3.4-r1 

#RUN python3 -m ensurepip
# RUN pip3 install --no-cache --upgrade pip setuptools control numpy
#RUN ln -sf /usr/bin/pip3 /usr/bin/pip

#USER node-red

# COPY --chown=node-red:root config /config

LABEL org.opencontainers.image.source=https://github.com/everest/everest-demo
