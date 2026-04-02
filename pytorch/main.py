import torch
from torch import nn
# from torch.utils.data import DataLoader
# from torchvision import datasets
# from torchvision.transforms import ToTensor
from datetime import datetime

from data_loader import train_dataloader, test_dataloader, training_data, test_data, categories
from model import NeuralNetwork
from train import train
from test import test
import os
from pathlib import Path


# x = torch.rand(5, 3)
# print(x)

BASE_DIR = Path(__file__).resolve().parent
CHECKPOINTS_DIR = BASE_DIR / "checkpoints"

# Inspect a batch of data. x is a batch of images, y is a batch of labels
for X, y in test_dataloader:
    print(f"Shape of X [N, C, H, W]: {X.shape}")
    print(f"Shape of y: {y.shape} {y.dtype}")
    break

device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
print(f"Using {device} device")

model = NeuralNetwork().to(device)
print(model)

if os.path.exists(CHECKPOINTS_DIR / f"latest_model.pth"):
    model.load_state_dict(torch.load(CHECKPOINTS_DIR / f"latest_model.pth", map_location=device, weights_only=True))
    print("Loaded latest checkpoint")
    Train = True
    # Do not retrain if a checkpoint is found, just test the model on the test dataset. Unindent the following lines to retrain a model from the last checkpoint in addition
else:
    Train = True
    print("No checkpoint found, starting fresh")
    # Train a model from scratch if no checkpoint is found
 
if Train:
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

    epochs = 5
    for t in range(epochs):
        print(f"Epoch {t+1}\n-------------------------------")
        train(train_dataloader, model, loss_fn, optimizer, device)
        test(test_dataloader, model, loss_fn, device)
    print("Done!")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_path = CHECKPOINTS_DIR / f"model_{timestamp}.pth"
    torch.save(model.state_dict(), model_path)
    torch.save(model.state_dict(), CHECKPOINTS_DIR / "latest_model.pth")
    print(f"Saved model to {model_path}")

model.eval()
x, y = test_data[0][0], test_data[0][1]
with torch.no_grad():
    x = x.to(device)
    pred = model(x)
    predicted, actual = categories[pred[0].argmax(0)], categories[y]
    print(f'Predicted: "{predicted}", Actual: "{actual}"')