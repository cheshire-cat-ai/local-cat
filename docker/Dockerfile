from ghcr.io/cheshire-cat-ai/core:1.7.1

### ENVIRONMENT VARIABLES ###
ENV PYTHONUNBUFFERED=1
ENV WATCHFILES_FORCE_POLLING=true

### SYSTEM SETUP ###
RUN apt-get -y update && apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

### INSTALL PYTHON DEPENDENCIES (Core) ###
WORKDIR /app

RUN pip install -U pip
RUN pip install --no-cache-dir --upgrade -v "fastembed==0.3.6"
RUN pip install --no-cache-dir --upgrade -v "typing-extensions>=4.9.0"
RUN pip install --no-cache-dir --upgrade -v "qdrant_client==1.11.0"
RUN pip install --no-cache-dir --upgrade -v "typing-extensions>=4.9.0"
RUN pip install --no-cache-dir --upgrade -v "protobuf==4.25.5"
RUN pip install --no-cache-dir --upgrade -v "pydantic>=2.4.2"
RUN pip install --no-cache-dir --upgrade -v "huggingface-hub>=0.20.3"
RUN pip install --no-cache-dir --upgrade -v "unstructured>=0.12.6"
RUN pip install --no-cache-dir -v "petals @ git+https://github.com/bigscience-workshop/petals"
RUN pip install --no-cache-dir -v "hivemind @ git+https://github.com/learning-at-home/hivemind.git@213bff98a62accb91f254e2afdccbf1d69ebdea9"
 
#fix for https://github.com/tensorflow/models/issues/11192
RUN pip install --upgrade protobuf

### FINISH ###
CMD python3 -m cat.main