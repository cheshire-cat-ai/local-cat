# local-cat
A ready to use 100% local setup for Cat + Ollama + Embedder + Qdrant

# DICLAIMERS:
1. You need a GPU and tech expertise to run this
2. The setup is english language only

### Steps:

1. double command setup
   1. create the docker compose
   2. setup core image and volumes
      1. volumes: static, public, plugins, metadata.json
      2. connect to Qdrant container
   3. embedder CPU based, bg-small-en-v1.5
   4. ollama GPU based
3. one command setup
   1. self-download the LLM (somehow)    
