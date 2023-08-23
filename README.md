# Text-Recognition-with-OpenCV
This Python program performs text recognition on images using an alphabet database. It detects characters within an image, compares them with a preloaded database of English alphabet letters, and identifies the most similar character using pixel-to-pixel correlation.

This 'database.py' Python script extracts individual characters from the 'alphabet.jpg' image, creates an alphabet database, and saves them as separate image files. The script performs contour detection on an input image to identify characters, then isolates and resizes each character. The resulting images are stored in a directory, forming a simple yet effective alphabet database for further text recognition tasks.

Features:

Detects characters within an input image using contour detection and bounding rectangles.

Resizes extracted characters to a consistent dimension suitable for the database.

Saves individual character images as files in the dbase directory.

Displays the original image with bounding rectangles around detected characters for visual reference.

Utilizes the created database of English alphabet letters for character comparison.

Identifies characters within an input image using contour detection and bounding rectangles.

Compares detected characters with the alphabet database using pixel-to-pixel correlation.

Simple and fast.
