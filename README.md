# Kokoro TTS Generator

<div align="center">

![Kokoro TTS Generator](https://via.placeholder.com/150x150?text=KTG)

**High Quality Local Text-to-Speech Generator**

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Release](https://img.shields.io/badge/Release-v0.1.0-orange.svg)](https://github.com/WilleIshere/KokoroTTSGenerator/releases)
[![Speed](https://img.shields.io/badge/Speed-Ultra%20Fast-red.svg)]()
[![Quality](https://img.shields.io/badge/Quality-High-brightgreen.svg)]()

*Generate high-quality speech from text using the powerful Kokoro TTS pipeline with an intuitive web interface.*

[🚀 Quick Start](#quick-start) • [📦 Download](#download) • [🔧 Build](#building-from-source) • [📚 Documentation](#documentation) • [🤝 Contributing](#contributing)

</div>

---

## ✨ Features

### 🎯 **Core Functionality**
- **High-Quality TTS**: Powered by the advanced Kokoro TTS pipeline
- **Multiple Voices**: Choose from a wide variety of natural-sounding voices
- **Customizable Output**: Adjust speech speed and pitch with precision
- **Batch Processing**: Generate audio from multi-paragraph text input with natural pauses
- **Real-time Preview**: Instant audio playback within the interface

### 🖥️ **User Interface**
- **Modern Design**: Built with NiceGUI for a sleek, responsive web interface
- **Intuitive Controls**: Simple, user-friendly experience
- **Progress Indicators**: Visual feedback for pipeline loading and audio generation
- **Dark Mode**: Easy on the eyes for extended use
- **Responsive Layout**: Works across devices and screen sizes

### 💾 **File Management**
- **WAV Format**: High-quality audio output
- **Automatic Naming**: Unique identifiers for each generated file
- **Local Processing**: All data processed on your machine for privacy
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Running from Source
```bash
# Clone the repository
git clone https://github.com/WilleIshere/KokoroTTSGenerator.git
cd KokoroTTSGenerator

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .

# Run the application
python app.py
```

## 📦 Download

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python**: 3.12
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: Space for model files and audio output
- **Internet**: Required for initial model download

### Latest Release
- **Version**: 0.1.0
- **Format**: Python package

[⬇️ Download Latest Release](https://github.com/WilleIshere/KokoroTTSGenerator/releases/latest)

## 🎮 Usage

### Getting Started
1. **Load Pipeline**: Wait for the TTS pipeline to initialize
2. **Select Voice**: Choose from available voices
3. **Adjust Parameters**: Set speech speed and pitch using the sliders
4. **Enter Text**: Type or paste text
5. **Generate**: Click "Generate Audio" to create audio
6. **Enjoy**: Preview and download your generated speech

### Voice Options
The application includes a variety of high-quality voices:
- **Female Voices**: af_alloy, af_aoede, af_bella, af_jessica, af_kore, af_nicole, af_nova, af_river, af_sarah, af_sky
- **Male Voices**: am_adam, am_echo, am_eric, am_fenrir, am_liam, am_michael, am_onyx, am_puck, am_santa

### Tips & Tricks
- **Long Text**: Break long texts into paragraphs for better processing
- **Punctuation**: Use proper punctuation for natural speech rhythm
- **Speed & Pitch**: Experiment with different settings for optimal results
- **Browser Compatibility**: Works best in modern browsers

## 🏗️ Project Structure

This project has been architected with a modular design for maintainability and extensibility:

```
KokoroTTSGenerator/
├── 🚀 app.py                    # Main entry point
├── 📁 src/                      # Source code
│   ├── gui.py                   # Web interface implementation
│   └── tts.py                   # TTS pipeline implementation
├── 📁 final_audio/              # Output directory for generated audio
├── 📁 temp/                     # Temporary working directory
└── 📄 pyproject.toml            # Dependencies and project configuration
```

### Architecture Highlights
- **Modern Web Interface**: Built with NiceGUI for a responsive experience
- **Efficient Pipeline**: Fast, high-quality audio generation
- **Clean Separation**: UI and TTS logic kept separate for maintainability
- **Python-powered**: Leverages the best Python libraries for TTS

## 🔧 Building from Source

### Prerequisites
```bash
# Ensure you have Python 3.12 installed
python --version

# Clone the repository
git clone https://github.com/WilleIshere/KokoroTTSGenerator.git
cd KokoroTTSGenerator
```

### Development Setup
```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .

# For development tools
pip install -e ".[dev]"
```

### Running the Application
```bash
python app.py
```

## 📚 Documentation

- **Project Structure**: Simple, modular design for easy maintenance
- **Kokoro TTS**: Leverages the powerful Kokoro TTS pipeline
- **NiceGUI**: Built with a modern web interface framework

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/KokoroTTSGenerator.git
cd KokoroTTSGenerator

# Install development dependencies
pip install -e ".[dev]"
```

### Ways to Contribute
- 🐛 **Bug Reports**: Found an issue? Please open an issue
- 💡 **Feature Requests**: Have an idea? We'd love to hear it
- 🔧 **Code Contributions**: Submit a pull request
- 📚 **Documentation**: Help improve our docs

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for changes
- Ensure cross-platform compatibility

## 🛠️ Technologies

- **Frontend**: NiceGUI (Python web interface framework)
- **TTS Engine**: Kokoro TTS pipeline
- **Audio**: soundfile, numpy
- **Dependencies**: kokoro, nicegui, torch, soundfile

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Kokoro TTS**: Amazing TTS pipeline that powers this application
- **NiceGUI**: Beautiful modern web interface framework
- **Python Community**: For the incredible ecosystem of libraries

## 📞 Support

### Getting Help
- 📖 **Documentation**: Check our comprehensive docs
- 🐛 **Issues**: Report bugs or request features on GitHub
- 💬 **Discussions**: Community Q&A and general discussion

### Common Issues
- **First Run Slow**: Initial pipeline loading downloads models and may take a few minutes
- **Memory Usage**: TTS models require significant RAM; 8GB recommended for optimal performance

## 🔄 Version History

### v0.1.0 (Latest)
- ✨ Initial release with core functionality
- 🎯 Multiple voice options
- 🎛️ Speed and pitch controls
- 🎮 Web-based user interface
- 🔊 High-quality audio output

---

<div align="center">

**Made with ❤️ by WilleIshere**

[⭐ Star this repo](https://github.com/WilleIshere/KokoroTTSGenerator) • [🍴 Fork it](https://github.com/WilleIshere/KokoroTTSGenerator/fork) • [📝 Report Issues](https://github.com/WilleIshere/KokoroTTSGenerator/issues)

</div>
