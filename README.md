# local-cat

A ready to use 100% local setup for Cat + Ollama + Embedder + Qdrant

> [!WARNING]
>
> 1. You need a GPU and tech expertise to run this
> 2. The setup is english language only

## Double command setup

1. clone the repo: `git clone https://github.com/cheshire-cat-ai/local-cat.git`
2. cd `cd local-cat`
3. Build the cat: `docker-compose up`
4. Pull the desired model from ollama library: `docker exec ollama_cat ollama pull <model_name:tags>`

---

### Steps

1. double command setup ✅
   1. create the docker compose
   2. setup core image and volumes
      1. volumes: static, public, plugins, metadata.json
      2. connect to Qdrant container
   3. embedder CPU based, bg-small-en-v1.5
   4. ollama GPU based
2. one command setup
   1. self-download the LLM (somehow)

## Use Ollama with MacOS GPU Acceleration

Ollama normally handles running the model with GPU acceleration. In order to use GPU acceleration on Mac OS it is recommended to run Ollama alongside Docker Desktop. More info [here](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image).
This mean that to use local-cat you have to install the classic (and recommended) menu bar app version of Ollama and run a multi-container docker application that run only the cat-code and qdrant containers.
To do this use the file `docker-compose-macos.yml` for creating your docker app. Before running the `docker-compose up` command, edit the file located in `cat/data/metadata.json`, find the URL `http://ollama:11434` and replace it with the following one `http://host.docker.internal:11434`. This will allow docker's containers to send requests to your local ollama service while enjoying the GPU acceleration.
