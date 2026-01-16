import os
import requests
from tqdm import tqdm

def download_file(url, destination):
    """Downloads a file with a progress bar."""
    if os.path.exists(destination):
        print(f"File already exists: {destination}")
        return

    print(f"Downloading: {url}")
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    os.makedirs(os.path.dirname(destination), exist_ok=True)

    with open(destination, 'wb') as file, tqdm(
            total=total_size, unit='iB', unit_scale=True, desc=os.path.basename(destination)
    ) as progress_bar:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    
    print(f"Successfully downloaded to: {destination}")

def main():
    # Base directory of the script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Models to download
    models = [
        {
            "url": "https://huggingface.co/vantagewithai/Z-Image-Turbo-GGUF/resolve/main/z-image-turbo-Q4_1.gguf",
            "path": os.path.join(base_dir, "Image-model", "z-image-turbo-Q4_1.gguf")
        },
        {
            "url": "https://huggingface.co/Qwen/Qwen3-4B-GGUF/resolve/main/Qwen3-4B-Q4_K_M.gguf",
            "path": os.path.join(base_dir, "LLM(text encoder)", "Qwen3-4B-Q4_K_M.gguf")
        }
    ]

    print("Checking models...")
    for model in models:
        download_file(model["url"], model["path"])
    
    print("\nAll models ready!")

if __name__ == "__main__":
    main()
