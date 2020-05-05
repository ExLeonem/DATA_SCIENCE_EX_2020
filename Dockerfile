FROM jupyter/scipy-notebook

RUN conda install -y pytorch-cpu torchvision-cpu -c pytorch
RUN conda install -y tensorflow
RUN conda install -c conda-forge keras
RUN conda install -y opencv
RUN conda install -c conda-forge pypdf2
RUN conda install -c conda-forge spacy

RUN python -m spacy download de
RUN python -m spacy download en
RUN python -m spacy download en_core_web_sm

## Alternative setup with tensorflow 2.0 and tensorflow-probability to work with statistical distributions in DL
# FROM jupyter/scipy-notebook
# RUN conda install tensorflow=2.0 python=3.7
# RUN conda install -y pytorch-cpu torchvision-cpu -c pytorch
# # RUN conda install -c anaconda tensorflow
# # tensorflow-propability newly added
# RUN conda install -c conda-forge tensorflow-probability 
# RUN conda install -c conda-forge keras
# RUN conda install -y opencv
# RUN conda install -c conda-forge pypdf2
# RUN conda install -c conda-forge spacy

# RUN python -m spacy download de
# RUN python -m spacy download en
# RUN python -m spacy download en_core_web_sm

# # RUN pip install --upgrade tensorflow