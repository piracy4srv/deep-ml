import torch

def single_neuron_model(x,y,weights,bias):
    x_tensor=torch.tensor(x,dtype=torch.float32)
    y_tensor=torch.tensor(y,dtype=torch.float32)
    w_tensor=torch.tensor(weights,dtype=torch.float32)
    b_tensor=torch.tensor(bias,dtype=torch.float32)

    linear_output=torch.matmul(x_tensor,w_tensor)+b_tensor
    predictions=torch.sigmoid(linear_output)

    mse=torch.mean((predictions - y_tensor)**2)

    rounded_preds=[round(val,4) for val in predictions.tolist()]
    rounded_mse=round(float(mse.item()),4)

    return rounded_preds, rounded_mse
