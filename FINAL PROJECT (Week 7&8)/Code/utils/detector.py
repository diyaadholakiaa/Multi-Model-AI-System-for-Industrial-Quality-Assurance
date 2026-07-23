from ultralytics import YOLO

# Load your trained model only once
model = YOLO("best.pt")


def detect(image_path):
    """
    Runs YOLO detection on an image.
    """
    results = model(image_path)
    return results