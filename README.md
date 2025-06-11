# Photo Condenser

A modern Python application for finding and managing similar or duplicate images in your photo collection. The tool uses Machine Learning to compare images and provides an intuitive interface for reviewing and organizing your photos.

**Select the photo you want to keep with arrow keys**

## Features

- 🖼️ Supports multiple image formats (JPG, PNG, WebP, etc.)
- 🔍 Advanced image comparison using Machine Learning
- 🎯 Smart caching for improved performance
- 📊 Image metadata display
- 🖱️ Intuitive navigation with address bar

## Installation

### Using pipx
```bash
pipx install photo_condenser
```

## Usage

### Command Line
```bash
# Launch the application
photo_condenser

# Or run directly
python -m photo_condenser
```

### Basic Workflow
1. Launch the application
2. Use the address bar to navigate to your photo directory
3. The application will present you with pairs of similar images
4. Use the arrow keys to select the image you want to keep or Space to skip

All not-selected images are moved to a `trash` folder.

## Development

### Setting up the development environment
```bash
# Clone the repository
git clone https://github.com/mova/photo_condenser.git
cd photo_condenser

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e .[dev]
```


## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

