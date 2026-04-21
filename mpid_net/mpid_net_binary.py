import torch
import torch.nn as nn
import timm

class ViT(nn.Module):
    def __init__(self, dropout=0.5, num_classes=2):
        super(ViT, self).__init__()
        
        # ViT small with patch size 32
        # img_size=512: our LArTPC images are 512x512
        # in_chans=1: single channel (grayscale ADC values)
        # num_classes=2: signal vs background
        self.vit = timm.create_model(
            "vit_small_patch32_224",
            pretrained=False,
            img_size=512,
            in_chans=1,
            num_classes=num_classes
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = self.dropout(x)
        x = self.vit(x)
        return x


if __name__ == '__main__':
    x = torch.ones([1, 1, 512, 512])
    vit = ViT()
    print(vit)
    print(vit(x))