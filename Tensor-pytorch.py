import torch
import numpy as np

ndarray = np.array([0, 1, 2])
t = torch.from_numpy(ndarray)
print(t)


# tensor([0, 1, 2])

'''
A tensor on PyTorch has three attributes:

shape: the size of the tensor
data type: the type of data stored in the tensor
device: the device in which the tensor is stored
If we print the attributes from the tensor we created, we'll have the following:

'''
print(t.shape)
print(t.dtype)
print(t.device)

'''
torch.Size([3])
torch.int64
cpu

'''