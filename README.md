# Kokoro TTS Generator

<div align="center">

![Kokoro TTS Generator](https://via.placeholder.com/150x150?text=KTG)

**High Quality Local Text-to-Speech Generator**

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-blueviolet.svg)](https://github.com/astral-sh/uv)
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

### Option 1: Using Compiled Versions (Recommended)
1. Download the appropriate release for your platform from the [Releases page](https://github.com/WilleIshere/KokoroTTSGenerator/releases/latest)
2. Extract the downloaded archive (if applicable)
3. Run the application:
   - **Windows**: Double-click the `.exe` file
   - **macOS**: Open the `.app` application or run the executable
   - **Linux**: Make the AppImage executable (`chmod +x KokoroTTSGenerator.AppImage`) and run it
4. Wait for the TTS pipeline to initialize on first run (may take a few minutes)

### Option 2: Running from Source
```bash
# Clone the repository
git clone https://github.com/WilleIshere/KokoroTTSGenerator.git
cd KokoroTTSGenerator

# Create virtual environment and install dependencies with UV
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync

# Run the application
python app.py
```

## 📦 Download

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 2GB+ free space for model files and audio output
- **Internet**: Required for initial model download
- **No Python installation needed** for compiled versions

### Latest Release
- **Version**: 0.1.0
- **Formats**:
  - **Windows**: Standalone executable (.exe) - no installation required
  - **macOS**: Native application bundle (.app) / executable
  - **Linux**: AppImage (.AppImage) - runs anywhere
  - **Source**: Python package (requires Python 3.12 & UV)
- **Size**: ~300MB (includes all dependencies and runtime)

[⬇️ Download Latest Release](https://github.com/WilleIshere/KokoroTTSGenerator/releases/latest)

> **Note**: For the compiled versions, no Python installation or additional dependencies are required. Everything is bundled in the executable.

## 🎮 Usage

### Getting Started
1. **First Launch**: Wait for the TTS pipeline to initialize (first run only)
2. **Select Voice**: Choose from available voices in the dropdown
3. **Adjust Parameters**: Set speech speed and pitch using the sliders
4. **Enter Text**: Type or paste text into the text area
5. **Generate**: Click "Generate Audio" to create speech
6. **Enjoy**: Preview the audio directly in the app and download the WAV file

### Voice Options
The application includes a variety of high-quality voices:
- **Female Voices**: af_alloy, af_aoede, af_bella, af_jessica, af_kore, af_nicole, af_nova, af_river, af_sarah, af_sky
- **Male Voices**: am_adam, am_echo, am_eric, am_fenrir, am_liam, am_michael, am_onyx, am_puck, am_santa

> All voices are included in the compiled versions - no additional downloads required.

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
├── 📄 pyproject.toml            # Dependencies and project configuration
└── 📄 uv.lock                   # UV dependencies lockfile
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
# Create virtual environment and install dependencies with UV
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync

# For development tools
uv pip install -e ".[dev]"
```

### Running the Application
```bash
uv run app.py
```

## 📚 Documentation

- **Project Structure**: Simple, modular design for easy maintenance
- **Kokoro TTS**: Leverages the powerful Kokoro TTS pipeline
- **NiceGUI**: Built with a modern web interface framework
- **Compiled Versions**: Standalone executables for all platforms

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/KokoroTTSGenerator.git
cd KokoroTTSGenerator

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
uv pip install -e ".[dev]"
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
- **TTS Engine**: Kokoro TTS pipeline (v0.9.4+)
- **Audio**: soundfile, numpy
- **Package Management**: UV (Fast, reliable Python package manager)
- **Dependencies**: kokoro, nicegui, torch, soundfile
- **Distribution**: Standalone executables for all platforms

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
- **Antivirus Warnings**: Some antivirus software may flag compiled executables; these are false positives
- **macOS Security**: On macOS, you may need to right-click and select "Open" the first time
- **Linux Permissions**: On Linux, remember to make AppImage files executable before running

## 🔄 Version History

### v0.1.0 (Latest)
- ✨ Initial release with core functionality
- 🎯 Multiple voice options
- 🎛️ Speed and pitch controls
- 🎮 Web-based user interface
- 🔊 High-quality audio output
- 📦 Compiled versions for Windows, macOS, and Linux

---

<div align="center">

**Made with ❤️ by WilleIshere**

[⭐ Star this repo](https://github.com/WilleIshere/KokoroTTSGenerator) • [🍴 Fork it](https://github.com/WilleIshere/KokoroTTSGenerator/fork) • [📝 Report Issues](https://github.com/WilleIshere/KokoroTTSGenerator/issues)

</div>
