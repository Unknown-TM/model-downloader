# LLM Model Downloader

import os
from diffusers import StableDiffusionPipeline
import torch

# ---- Configuration ----
model_name = "hogiahien/aom3"      # model identifier
save_dir = "./model/aom3"          # local folder to save the model < ./[modelname]> it will save where this file will be present
use_auth_token = True              # set to True if private repo (requires HF token)
device = "cuda" if torch.cuda.is_available() else "cpu" # to use GPU or else it will use CPU

# Create save directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

print(f"Downloading {model_name} to {save_dir}...")

# Load the model pipeline (this will download all model files)
pipe = StableDiffusionPipeline.from_pretrained(
    model_name,
    use_auth_token=use_auth_token
)

# Save model locally
pipe.save_pretrained(save_dir)

print(f"Model saved to {save_dir}!")
