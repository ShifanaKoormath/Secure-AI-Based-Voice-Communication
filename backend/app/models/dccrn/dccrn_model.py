import torch
import torch.nn as nn
import torch.nn.functional as F


class DCCRN(nn.Module):
    """
    Simplified DCCRN model for inference.
    Based on official DCCRN architecture (no training logic).
    """

    def __init__(self):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Conv2d(2, 16, kernel_size=(5, 2), stride=(2, 1), padding=(2, 1)),
            nn.BatchNorm2d(16),
            nn.PReLU(),

            nn.Conv2d(16, 32, kernel_size=(5, 2), stride=(2, 1), padding=(2, 1)),
            nn.BatchNorm2d(32),
            nn.PReLU(),
        )

        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(32, 16, kernel_size=(5, 2), stride=(2, 1), padding=(2, 1)),
            nn.BatchNorm2d(16),
            nn.PReLU(),

            nn.ConvTranspose2d(16, 2, kernel_size=(5, 2), stride=(2, 1), padding=(2, 1)),
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
