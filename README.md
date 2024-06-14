# local-cat 😸🏠

**local-cat** provides a completely local setup for CheshireCat. Local-cat leverages Local runners + Qdrant to run your preferred LLM, Embedder and VectorDB locally.

> [!WARNING]
>
> - **Technical Expertise Required:** Setting up and running local-cat requires some technical know-how.
> - **Hardware Requirements:** Performance may be slow without a recent GPU or NPU.

## Ollama Setup

> [!IMPORTANT]
> Ollama can be instable with **latest models** or **non-common use** models(like qwen, deepseek)!!
> If you encount inference problems, downgrade ollama image or [open an issue to Ollama](https://github.com/ollama/ollama/issues)

### Setup Instructions

1. **Clone the Repository:** `git clone https://github.com/cheshire-cat-ai/local-cat.git`
2. **Navigate to the Directory:** `cd local-cat`
3. **Start local-cat:** `docker-compose up -d`
4. **Pull Your Desired Model:** `docker exec ollama_cat ollama pull <model_name:tag>`
   - Replace `<model_name:tag>` with the specific model you want to use.
5. **Your Setup is Complete!**
   - You can now install additional plugins or start interacting with local-cat.

### Use Ollama with MacOS GPU Acceleration

Ollama normally handles running the model with GPU acceleration. In order to use GPU acceleration on Mac OS it is recommended to run Ollama directly on the host machine rather than inside Docker. More info [here](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image).
> [!NOTE]
> This is recommended until GPU acceleration is supported by Docker Desktop on MacOS.

To use local-cat with GPU acceleration on Mac:

1. Install the menu bar app version of Ollama, which is the current recommended setup for MacOS users.
2. Start using the following command `docker compose -f docker-compose-macos.yml up`
3. Configure the Ollama Base URL in the cat's LLM settings to `http://host.docker.internal:11434`.

> Note: This configuration allows Docker containers to communicate with your locally running Ollama service and leverage MacOS GPU acceleration.

### Use Ollama with AMD

To use local-cat with [AMD graphics that supports ROCm](https://rocm.docs.amd.com/en/docs-5.7.0/release/gpu_os_support.html#linux-supported-gpus), use the following command:

```bash
docker compose -f docker-compose-amd.yml up
```
