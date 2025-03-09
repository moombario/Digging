import os
from google.cloud import vision

# Ensure your JSON file path is correctly set
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

# Initialize Vision API client
client = vision.ImageAnnotatorClient()

# Test Image URL (Change this to any book cover image URL for testing)
test_image_url = "https://example.com/sample_book_cover.jpg"

def test_vision_api(image_url):
    image = vision.Image()
    image.source.image_uri = image_url

    # Perform label detection
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print("\n✅ **Vision API Test Results:**")
    if labels:
        for label in labels:
            print(f" - {label.description} (Confidence: {label.score:.2f})")
    else:
        print("❌ No labels detected -- Check image URL or credentials.")

# Run the test
if __name__ == "__main__":
    test_vision_api(test_image_url)