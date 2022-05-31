# Sketch Simplification

**This repository is forked from [ramilmsh/sketch_simplification](https://github.com/ramilmsh/sketch_simplification) and modified. Please refers to [bobbens/sketch_simplification](https://github.com/bobbens/sketch_simplification) for more information about the original Sketch Simplification.**

In this repository, I convert the sketch simplification code into a package and **delete** all unused files.

## Usage

In order to use this repository as your package, you need to clone this repository and download the [`model_gan.pth`](https://mega.nz/folder/2lUn1YbY#JhTkB1vdaBMeTCSs37iTVA) to the root folder of your project.

```
your_project
  ├── sketch_simplification
  │     ├── __init__.py
  │     ├── model_gan.py
  │     └── simplify.py
  └── model_gan.pth
```

Then, you could just import `sketch_simplification` into your projects.

```py
from sketch_simplification import sketch_simplification
from PIL import Image

model = sketch_simplification(device='cuda')

image = Image.open('image.jpg')
result = model.simplify(image)
result.save('out.jpg')
```

---

This project was developed as part of Nodeflux Internship x Kampus Merdeka.
