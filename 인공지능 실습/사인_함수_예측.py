# -*- coding: utf-8 -*-
"""사인 함수 예측.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uFcOcR8QcrbKvhd8I9gcTyPIZRvdKycX
"""

import math
import torch
import matplotlib.pyplot as plt

x = torch.linspace(-math.pi, math.pi, 1000)
y = torch.sin(x)

a = torch.randn(())
b = torch.randn(())
c = torch.randn(())
d = torch.randn(())

y_random = a * x**3 + b* x**2 + c*x +d
plt.subplot(2,1,1)
plt.title("y True")
plt.plot(x,y)

plt.subplot(2,1,2)
plt.title("y prediction")
plt.plot(x,y_random)

plt.show()

learning_rate = 1e-6

for epoch in range(20):
  y_pred = a * x**3 + b* x**2 + c*x +d

  loss = (y_pred - y).pow(2).sum().item()
  if epoch % 100 == 0:
    print(f"epoch {epoch+1} loss {loss}")

  grad_y_pred = 2.0 * (y_pred - y)
  grad_a = (grad_y_pred * x**3).sum()
  grad_b = (grad_y_pred * x**2).sum()
  grad_c = (grad_y_pred * x).sum()
  grad_d = grad_y_pred.sum()

  a -= learning_rate * grad_a
  b -= learning_rate * grad_b
  c -= learning_rate * grad_c
  d -= learning_rate * grad_d

  plt.subplot(3,1,1)
  plt.title("y True")
  plt.plot(x,y)

  plt.subplot(3,1,2)
  plt.title("y prediction")
  plt.plot(x,y_pred)

  plt.subplot(3,1,3)
  plt.plot(y_random)
  plt.title("Y random")
  plt.show()



