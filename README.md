# Simple Text-to-Image Pipeline (Z-Image Turbo)

This project provides a simple text-to-image pipeline using `stable-diffusion.cpp`, Z-Image Turbo, and Qwen3-4B.

## Requirements
- Python 3.x
- `vae/ae.safetensors` (Automatically downloaded or placed manually)
- `Image-model/z-image-turbo-Q4_1.gguf`
- `LLM(text encoder)/Qwen3-4B-Q4_K_M.gguf`
- Yes I used Quantasiation!

## Setup
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Download Models**:
   Run the download script to fetch the required models:
   ```bash
   python download_models.py
   ```

## Usage
Run the generation script with a prompt:

```bash
python generate.py -p "A futuristic cityscape with neon lights"
```

The output will be saved to `outputs/generated.png`.

## Configuration
- **Steps**: 8 (Optimized for Z-Image Turbo)
- **Guidance**: 1.0
- **Text Encoder**: Qwen3-4B
- **Backend**: AVX2 (CPU)

## License(of the repository)
MIT License

## License(of the models)
Apache License 2.0
(both models)

## Author
**I'MnotSHRI(Chronos-MK8-mainframe)**
