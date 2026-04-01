import torch
import torchvision
import streamlit
import PIL
import sklearn
import matplotlib

print("torch:", torch.__version__)
print("torchvision:", torchvision.__version__)
print("streamlit: OK")
print("PIL: OK")
print("sklearn: OK")
print("matplotlib: OK")
print("CUDA available:", torch.cuda.is_available())