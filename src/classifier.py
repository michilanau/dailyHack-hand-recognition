import torchvision
import torch
import torchvision.transforms as transforms
import PIL.Image as Image

classes = [
    'palm',
    'l',
    'fist',
    'fist_moved',
    'thumb',
    'index',
    'ok',
    'palm_moved',
    'c',
    'down'
]

model = torch.load('./best_model.pth')

image_transforms = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

def classify(model, image_transforms, image_path, classes):
    model = model.eval()
    image = Image.open(image_path)
    image = image_transforms(image).float()
    image = image.unsqueeze(0)

    output = model(image)
    _, predicted = torch.max(output.data, 1)

    return classes[predicted.item()]

def classifyImage(image_path):
    return classify(model, image_transforms, image_path, classes)

# Tests

#print(classify(model, image_transforms, "image_tests/frame_00_01_0002.png", classes)) # palm
#print(classify(model, image_transforms, "image_tests/frame_00_08_0010.png", classes)) # palm_moved
#print(classify(model, image_transforms, "image_tests/frame_01_07_0092.png", classes)) # ok
#print(classify(model, image_transforms, "image_tests/frame_00_02_0020.png", classes)) # l

#text = ""
#text += translation[classify(model, image_transforms, "image_tests/frame_00_02_0020.png", classes) + "+" + classify(model, image_transforms, "image_tests/frame_01_07_0092.png", classes)]
#text += translation[classify(model, image_transforms, "image_tests/frame_00_01_0002.png", classes)]
#text += translation[classify(model, image_transforms, "image_tests/frame_00_02_0020.png", classes) + "+" + classify(model, image_transforms, "image_tests/frame_01_07_0092.png", classes)]
#print(text)
###