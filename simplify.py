import torch
from torchvision import transforms
from . import model_gan

class Simplification:
    def __init__(self, device=torch.device('cpu')):
        self.device = device
        self.model = model_gan.model
        self.immean = model_gan.immean
        self.imstd = model_gan.imstd
        self.load('model_gan.pth', self.device)
        self.model.to(self.device)

    def load(self, path, map_location=torch.device('cpu')):
        self.model.load_state_dict(torch.load(path, map_location=map_location))
        print(f'Loaded sketch simplification from {path}.')

    def simplify(self, image):
        data = image.convert('L')
        w, h = data.size[0], data.size[1]
        pw = 8 - (w % 8) if w % 8 != 0 else 0
        ph = 8 - (h % 8) if h % 8 != 0 else 0

        data = ((transforms.ToTensor()(data) - self.immean) / self.imstd).unsqueeze(0)
        if pw != 0 or ph != 0:
            data = torch.nn.ReplicationPad2d((0, pw, 0, ph))(data).data
        
        data = data.to(self.device)
        pred = self.model(data)[0]

        pred = transforms.ToPILImage()(pred)
        return pred