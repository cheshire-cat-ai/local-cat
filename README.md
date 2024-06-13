# local-cat 😸🏠

**local-cat** provides a completely local setup for CheshireCat. Local-cat leverages Ollama + Qdrant to run your preferred LLM, Embedder and VectorDB locally.

> [!WARNING]
>
> - **Technical Expertise Required:** Setting up and running local-cat requires some technical know-how.
> - **Hardware Requirements:** Performance may be slow without a recent GPU or NPU.

## Setup Instructions

1. **Clone the Repository:** `git clone https://github.com/cheshire-cat-ai/local-cat.git`
2. **Navigate to the Directory:** `cd local-cat`
3. **Start local-cat:** `docker-compose up -d`
4. **Pull Your Desired Model:** `docker exec ollama_cat ollama pull <model_name:tag>`
   - Replace `<model_name:tag>` with the specific model you want to use.
5. **Configure LLM Settings:**
   - Access the admin dashboard and open the LLM settings.
      > Note: If you are running the local-cat on the same machine, you can reach the dashboard at https://localhost:1865/admin 
   - Select Ollama as your LLM provider.
      > Note: You could also select another provider but be aware you will have to fill in different fields.
   - Enter `http://ollama_cat:11434` as the Base URL or `http://host.docker.internal:11434` if your local ollama service is running directly on your host machine or not in the same docker compose.
   - Input in the Model field the exact `model_name:tag` pulled earlier in Ollama. E.g. `mistral:instruct`
     > Note: You could list the downloaded models using `docker exec ollama_cat ollama list`
   - Confirm by hitting save and wait for the changes to apply.
6. **Configure Embedder Settings:**
   - Access the admin dashboard and open the Embedder settings.
   - Select the local Qdrant FastEmbed as your Embedder provider.
     > Note: You could also select another provider but be aware you will have to fill in different fields.
   - Choose an embedder suitable for your needs, like `BAAI/bge-large-en-v1.5-quantized` for English or `intfloat/multilingual-e5-large` for multilingual capabilities.
   - Save your settings and allow some time for saving changes and for any necessary downloads.
7. **Your Setup is Complete!**
   - You can now install additional plugins or start interacting with local-cat.


## Use Ollama with MacOS GPU Acceleration

Ollama normally handles running the model with GPU acceleration. In order to use GPU acceleration on Mac OS it is recommended to run Ollama directly on the host machine rather than inside Docker. More info [here](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image).
> Note: This is recommended until GPU acceleration is supported by Docker Desktop on MacOS.

To use local-cat with GPU acceleration on Mac:
- Install the menu bar app version of Ollama, which is the current recommended setup for MacOS users.
- Use the `docker-compose-macos.yml` to start local-cat, running only cheshire_cat_core and cheshire_cat_vector_memory containers.
- Configure the Ollama Base URL in the cat's LLM settings to `http://host.docker.internal:11434`. 
> Note: This configuration allows Docker containers to communicate with your locally running Ollama service and leverage MacOS GPU acceleration.
