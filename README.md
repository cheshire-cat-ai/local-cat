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
