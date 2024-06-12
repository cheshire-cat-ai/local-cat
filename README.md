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
   - Enter `http://ollama_cat:11434` as the Base URL.
   - Input in the Model field the exact `model_name:tag` pulled earlier in Ollama. E.g. `mistral:instruct`
     > Note: You could list the downloaded models using `docker exec ollama_cat ollama list`
   - Confirm by hitting save and wait for the changes to apply.
   ![LLM example settings](./assets/settings_example_LLM.png?raw=true)
6. **Configure Embedder Settings:**
   - Access the admin dashboard and open the Embedder settings.
   - Select the local Qdrant FastEmbed as your Embedder provider.
     > Note: You could also select another provider but be aware you will have to fill in different fields.
   - Choose an embedder suitable for your needs, like `BAAI/bge-large-en-v1.5-quantized` for English or `intfloat/multilingual-e5-large` for multilingual capabilities.
   - Save your settings and allow some time for saving changes and for any necessary downloads.
   ![Embedder example settings](./assets/settings_example_Embedder.png?raw=true)
7. **Your Setup is Complete!**
   - You can now install additional plugins or start interacting with local-cat.

