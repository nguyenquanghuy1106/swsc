from torchvision import datasets

DATA_DIR = "datasets/standardized_256"

dataset = datasets.ImageFolder(DATA_DIR)

print("Classes:", dataset.classes)
print("Số ảnh:", len(dataset))