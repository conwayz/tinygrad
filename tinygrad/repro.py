from tinygrad.tensor import Tensor
a = Tensor([1.1, 2.2])
b = Tensor([3.3, 4.4])
c = a.dot(b)
val = c.numpy()
print(c.dtype, val) # 11