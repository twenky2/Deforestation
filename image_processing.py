import ee

def perform_image_segmentation(image):
    # Implement your segmentation logic here
    # This is a placeholder implementation
    ndvi = image.normalizedDifference(['B5', 'B4'])
    return ndvi.gt(0.2)