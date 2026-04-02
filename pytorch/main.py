import torch
from torch import nn
# from torch.utils.data import DataLoader
# from torchvision import datasets
# from torchvision.transforms import ToTensor
# import matplotlib.pyplot as plt
from datetime import datetime

from data_loader import train_dataloader, test_dataloader
from model import NeuralNetwork
from train import train
from test import test
import os

# x = torch.rand(5, 3)
# print(x)


# Display image and label.
for X, y in test_dataloader:
    # img = X[0].squeeze()  # first image in batch
    # plt.imshow(img, cmap="gray")
    # plt.title(f"Label: {y[0].item()}")
    # plt.show()
    print(f"Shape of X [N, C, H, W]: {X.shape}")
    print(f"Shape of y: {y.shape} {y.dtype}")
    break

device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
print(f"Using {device} device")

model = NeuralNetwork().to(device)
print(model)

if os.path.exists("checkpoints/latest_model.pth"):
    model.load_state_dict(torch.load("checkpoints/latest_model.pth", map_location=device))
    print("Loaded latest checkpoint")
else:
    print("No checkpoint found, starting fresh")


loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)


epochs = 5
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer, device)
    test(test_dataloader, model, loss_fn, device)
print("Done!")


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_path = f"checkpoints/model_{timestamp}.pth"
torch.save(model.state_dict(), model_path)
torch.save(model.state_dict(), "checkpoints/latest_model.pth")
print(f"Saved model to {model_path}")