# Dockerfile
# Simple Jupyter Notebook with Tensorflow GPU support

# we build on top of the basic NVIDIA image
FROM nvidia/cuda:10.0-base

# some documentation
LABEL maintainer="Sebastien LEGRAND"

# expose the following port
EXPOSE 8888

# entry point for this image
ENTRYPOINT [ "jupyter", "notebook" ]

# arguments
ARG CONDA_DIR="/opt/conda"
ARG NB_USER="jovyan"
ARG NB_UID=1000
ARG NB_GID=100

# install some basic packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends wget bzip2 locales tzdata && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen && \
    ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

# set the environment
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    TZ=America/New_York \
    NB_USER=${NB_USER} \
    NB_UID=${NB_UID} \
    NB_GID=${NB_GID} \
    SHELL=/bin/bash \
    CONDA_DIR=${CONDA_DIR} \
    PATH=${CONDA_DIR}/bin:$PATH

# miniconda installation
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /opt/miniconda.sh && \
    /bin/bash /opt/miniconda.sh -b -p ${CONDA_DIR} && \
    rm -f /opt/miniconda.sh

# install the conda libraries
RUN conda install -qyk python=3.6 pip && \
    conda install -qyk numpy pandas matplotlib seaborn bokeh && \
    conda install -qyk tensorflow-gpu keras && \
    conda install -qyk jupyter && \
    conda clean -y --quiet --all

# copy the Jupyter configuration file
COPY jupyter_notebook_config.py /etc/jupyter/

# create the user
RUN useradd -m -s /bin/bash -N -u ${NB_UID} -g ${NB_GID} ${NB_USER}
USER ${NB_USER}
WORKDIR /home/${NB_USER}
