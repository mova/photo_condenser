# Photo Deduplicator

A Python application that helps you find and remove duplicate or similar images from your photo collection. The tool uses computer vision to compare images and presents you with similar pairs, allowing you to keep the best one.

## Features

- Scans a directory for images (supports JPG, PNG, BMP, TIFF, GIF)
- Uses histogram comparison to find visually similar images
- Simple GUI interface for reviewing and selecting which images to keep
- Moves deleted images to a "trash" folder instead of permanent deletion
- Shows image filenames and sizes for easy comparison

## Requirements

- Python 3.7+
- OpenCV
- Pillow
- NumPy

## Installation

1. Clone this repository or download the files
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python photo_deduplicator.py
```

2. Click "Select Image Folder" and choose the folder containing your images
3. The application will scan for similar images
4. For each pair of similar images:
   - The left and right arrow keys let you choose which image to keep
   - The other image will be moved to a "trash" folder
   - The next similar pair will be shown automatically

## How It Works

The application uses OpenCV to:
1. Load and resize images to a common size
2. Convert images to grayscale
3. Calculate color histograms
4. Compare histograms to determine similarity

Images with a similarity score above a certain threshold are considered potential duplicates.

## Notes

- The application creates a "trash" folder in your selected directory
- No files are permanently deleted - they're just moved to the trash folder
- The similarity threshold can be adjusted in the code (look for `if score < 0.2`)
- Processing time depends on the number and size of images

## License

MIT
