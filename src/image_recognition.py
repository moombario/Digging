from google.cloud import vision

client = vision.ImageAnnotatorClient()

def analyze_image(image_url):
    response = client.label_detection(image={'source': {'image_uri': image_url}})
    for label in response.label_annotations:
        if "book" in label.description.lower():
            return True
    return False