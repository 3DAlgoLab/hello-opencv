#!/usr/bin/env python3
"""
Load an image from file and display it using OpenCV.
"""

import cv2
import sys
import os

def main():
    # Check if an image path was provided
    if len(sys.argv) != 2:
        print("Usage: python load_image_show.py <image_path>")
        print("Example: python load_image_show.py example.jpg")
        return
    
    image_path = sys.argv[1]
    
    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return
    
    # Load the image
    image = cv2.imread(image_path)
    
    # Check if image was loaded successfully
    if image is None:
        print(f"Error: Could not load image from '{image_path}'.")
        print("Make sure the file is a valid image format (jpg, png, etc.).")
        return
    
    # Display the image
    cv2.imshow('Loaded Image', image)
    
    # Wait for a key press and then close the window
    print("Press any key to close the image window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print(f"Successfully loaded and displayed image: {image_path}")
    print(f"Image dimensions: {image.shape}")

if __name__ == "__main__":
    main()