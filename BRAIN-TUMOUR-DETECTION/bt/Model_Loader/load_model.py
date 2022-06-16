from Log_Writer.logger import App_Logger
import torchvision , torch
import torch.nn as nn
import dill as dill

def load(PATH):
    try:
        logger = App_Logger()

        # # Load Model
        device = torch.device('cpu')
        # model = torchvision.models.efficientnet_b0(pretrained=False).to(device)
        # model.classifier[1] = nn.Sequential(
        #     nn.Linear(in_features=1280, out_features=4096, bias=True),
        #     nn.Dropout(p=0.3, inplace=False),
        #     nn.BatchNorm1d(4096),
        #     nn.ReLU(),
        #     nn.Dropout(p=0.3, inplace=False),
        #     nn.Linear(in_features=4096, out_features=2048, bias=True),
        #     nn.BatchNorm1d(2048),
        #     nn.ReLU(),
        #     nn.Linear(in_features=2048, out_features=4, bias=True)
        # ).to(device)
        # # # if we load model from its original checkpoints and then load best model weights
        # model.load_state_dict(torch.load(PATH, map_location=device))
        # model.eval()

        #if we use saved model directly
        model=torch.load(PATH, pickle_module=dill, encoding='utf-8' ,map_location=torch.device('cpu'))
        model.eval()

        logger.log("Model Loaded Successfully")
        return model
    except Exception as e:
        logger = App_Logger()
        logger.log("ERROR : Model Loading Unsuccessful\n")
        return print(e)