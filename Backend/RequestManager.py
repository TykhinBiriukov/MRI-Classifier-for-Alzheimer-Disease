import sys
import json
import ast

# Imports for model
import torch
from PIL import Image
from torchvision import transforms
#


# This is temporary file instead of the model
route = ast.literal_eval(sys.argv[1])
name = ast.literal_eval(sys.argv[2])

if route == "greet":
    message = f"Hello, {name}!"

elif route == "goodbye":
    message = f"Goodbye, {name}!"

else:
    message = "Invalid route!"

print(message)

sys.stdout.flush()



def call_model(image) -> str: # get image location
    loaded_model = torch.load("model_file1.pt")
    loaded_model.eval()

    transform = transforms.Compose([
        transforms.Resize((380, 380)),
        transforms.CenterCrop(380),
        transforms.ToTensor(),
        # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) -- we probably don't need normalization
    ])
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = loaded_model(input_tensor)
        predicted_class = output.argmax(dim=1).item()

    result_map = {0: "ClassA", 1: "ClassB", 2: "ClassC", 3: "ClassD"} # define classes for used dataset
    result_class = result_map[predicted_class]
    print("Predicted class:", result_class)
    
    return result_class