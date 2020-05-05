import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision as torchv
import torchvision.transforms as transforms

from sklearn.model_selection import train_test_split


class MnistConvNet(nn.Module):

    def __init__(self):
        super(MnistConvNet, self).__init__()
        pass

    def forward(self,x):
        pass



# Returns mnist dataset for training, splitted
def load_dataset():
    pass