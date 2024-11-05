from ghcr.io/cheshire-cat-ai/core:1.7.1

### ENVIRONMENT VARIABLES ###
ENV PYTHONUNBUFFERED=1
ENV WATCHFILES_FORCE_POLLING=true

### SYSTEM SETUP ###
RUN apt-get -y update && apt-get install -y curl build-essential fastjar libmagic-mgc libmagic1 mime-support git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

### PREPARE BUILD WITH NECESSARY FILES AND FOLDERS ###
COPY ./pyproject.toml /app/pyproject.toml

### override default llm.py to add another LLM configuration for Petals
COPY ./cat/factory/llm.py /app/cat/factory/llm.py

### INSTALL PYTHON DEPENDENCIES (Core) ###
WORKDIR /app
RUN pip install -U pip && \
    pip install --no-cache-dir . &&\
    python3 -c "import nltk; nltk.download('punkt');nltk.download('averaged_perceptron_tagger')"

#fix for https://github.com/tensorflow/models/issues/11192
RUN pip install --upgrade protobuf

### FINISH ###
CMD python3 -m cat.main