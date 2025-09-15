# LLM Model Downloader

A simple Python script to download and store Stable Diffusion models locally on your machine for offline use.

## 📋 Overview

This repository contains a utility script that downloads Stable Diffusion models from Hugging Face Hub and saves them locally. By storing models locally, you can:

- Use models offline without internet connectivity
- Avoid re-downloading models every time you use them
- Improve loading times for your AI image generation projects
- Have better control over model versions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (optional, but recommended for faster processing)
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Unknown-TM/LLM-Model-Downloader.git
   cd LLM-Model-Downloader
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the download script**
   ```bash
   python download_model.py
   ```

## 📦 What Gets Downloaded

The script downloads the **AOM3 (AbyssOrangeMix3)** model by default, which is a popular anime-style Stable Diffusion model. The model includes:

- Model weights and configuration files
- Tokenizer and text encoder
- VAE (Variational Autoencoder)
- Safety checker (optional)
- All necessary components for image generation

## 📁 Directory Structure

After running the script, your directory will look like this:

```
├── download_model.py
├── requirements.txt
├── README.md
└── model/
    └── aom3/
        ├── model_index.json
        ├── scheduler/
        ├── text_encoder/
        ├── tokenizer/
        ├── unet/
        ├── vae/
        └── safety_checker/
```

## ⚙️ Configuration

You can modify the script to download different models by editing these variables in `download_model.py`:

```python
model_name = "hogiahien/aom3"  # Change this to any Hugging Face model ID
save_dir = "./model/aom3"      # Local directory to save the model
```

### Popular Stable Diffusion Models

Here are some popular models you can download:

| Model | ID | Style | Description |
|-------|----|----|-----------|
| AOM3 | `hogiahien/aom3` | Anime | High-quality anime-style images |
| Realistic Vision | `SG161222/Realistic_Vision_V5.1_noVAE` | Realistic | Photorealistic images |
| DreamShaper | `Lykon/DreamShaper` | Versatile | Good balance of styles |
| Anything V4 | `andite/anything-v4.0` | Anime | Popular anime model |

## 🔧 System Requirements

### Minimum Requirements
- **RAM**: 8GB (16GB recommended)
- **Storage**: 5-10GB free space per model
- **Python**: 3.8+

### Recommended Requirements
- **GPU**: NVIDIA GPU with 6GB+ VRAM
- **RAM**: 16GB+
- **Storage**: SSD with 20GB+ free space

## 🐛 Troubleshooting

### Common Issues

**1. Out of Memory Error**
```
RuntimeError: CUDA out of memory
```
**Solution**: The script will automatically fall back to CPU if GPU memory is insufficient.

**2. Network/Download Issues**
```
HTTPError: 401 Client Error
```
**Solution**: Some models require authentication. Set `use_auth_token=True` and ensure you're logged into Hugging Face:
```bash
huggingface-cli login
```

**3. Permission Errors**
```
PermissionError: [Errno 13] Permission denied
```
**Solution**: Run with appropriate permissions or change the save directory to a location you have write access to.

## 🔐 Authentication (For Private Models)

If you want to download private or gated models:

1. **Create a Hugging Face account** at [huggingface.co](https://huggingface.co)
2. **Generate an access token** in your HF settings
3. **Login via CLI**:
   ```bash
   huggingface-cli login
   ```
4. **Set authentication in script**:
   ```python
   use_auth_token = True
   ```

## 📊 Storage Management

Models can be large (2-7GB each). To manage storage:

- **Check model size** before downloading on the Hugging Face model page
- **Use symbolic links** if you need the same model in multiple projects
- **Clean up unused models** periodically
- **Use external storage** for model collections

## 🚀 Usage After Download

Once downloaded, you can load the model in your projects:

```python
from diffusers import StableDiffusionPipeline
import torch

# Load from local directory
pipe = StableDiffusionPipeline.from_pretrained(
    "./model/aom3",
    torch_dtype=torch.float16
)

# Generate an image
image = pipe("anime girl with blue hair").images[0]
image.save("output.png")
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co) for providing the model hub and diffusers library
- [Stability AI](https://stability.ai) for the original Stable Diffusion models
- Model creators and the open-source community

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) section
2. Create a new issue with detailed information
3. Join the discussion in [Discussions](../../discussions)

---

**⭐ If this helped you, please give it a star!**
