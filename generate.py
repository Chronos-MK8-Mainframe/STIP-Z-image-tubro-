import subprocess
import os
import sys
import time

#image gen function
def generate_image(prompt, output_path="outputs/generated.png"):
    # Paths to models
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Use Vulkan-enabled binary
    sd_path = os.path.join(base_path, "bin_vulkan", "sd-cli.exe")
    model_path = os.path.join(base_path, "Image-model", "z-image-turbo-Q4_1.gguf")
    llm_path = os.path.join(base_path, "LLM(text encoder)", "Qwen3-4B-Q4_K_M.gguf")
    vae_path = os.path.join(base_path, "vae", "ae.safetensors")

    # Cmd args
    args = [
        sd_path,
        "--diffusion-model", model_path,
        "--llm", llm_path,
        "--vae", vae_path,
        "-p", prompt,
        "-o", output_path,
        "--steps", "8",
        "--guidance", "1.0",
        "--clip-on-cpu",
        "--vae-on-cpu",
        "-v"  # Verbose for progress
    ]

    print(f"Generating image for: '{prompt}'")
    print("-" * 40)

    try:
        # for streaming output
        process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            encoding='utf-8',
            errors='replace'
        )

        for line in process.stdout:
            line = line.strip()
            if line:
                # Filter for progress lines if possible, or just print everything
                # sd.cpp typically prints progress on stderr, but I redirected it to stdout
                print(line)

        process.wait()

        if process.returncode == 0:
            print("-" * 40)
            print(f"Success! Image saved to: {output_path}")
        else:
            print("-" * 40)
            print(f"Error: Generation failed with exit code {process.returncode}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "A high-tech digital art illustration of a powerful AI entity" #for debug
    generate_image(prompt)
