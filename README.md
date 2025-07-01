<div align="center">

<img src="https://via.placeholder.com/200x200?text=KokoroTTS" alt="Project Logo" width="200"/>

# 🎙️ Kokoro TTS Generator

<p>
  <img src="https://img.shields.io/badge/python-3.12-blue.svg" alt="Python 3.12" height="20"/>
  <img src="https://img.shields.io/badge/Kokoro-0.9.4+-purple.svg" alt="Kokoro TTS" height="20"/>
  <img src="https://img.shields.io/badge/NiceGUI-2.20.0+-green.svg" alt="NiceGUI" height="20"/>
  <img src="https://img.shields.io/badge/Quality-High-brightgreen.svg" alt="High Quality" height="20"/>
  <img src="https://img.shields.io/badge/Speed-Ultra%20Fast-red.svg" alt="Ultra Fast" height="20"/>
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License" height="20"/>
</p>

A modern, elegant, and lightning-fast text-to-speech generator with a clean web interface.  
Convert text to high-quality, natural-sounding speech with customizable voices locally on your machine in seconds.

<img src="https://via.placeholder.com/800x450?text=Kokoro+TTS+Generator+Demo" alt="Demo" width="800"/>

*High-quality, ultra-fast TTS generation with a beautiful user interface*

</div>

<div align="center">

## ✨ Features

</div>

<div align="center">

⚡ **Lightning-Fast Processing** - Generate audio in seconds, not minutes
🔊 **Studio-Quality Output** - Crystal clear, high-fidelity voice generation
🌐 **Modern Web Interface** - Clean, responsive design built with NiceGUI
🎤 **Multiple Voice Options** - Choose from a wide variety of natural-sounding voices
🎛️ **Fine-tuning Controls** - Adjust speed and pitch for perfect output
📝 **Multi-paragraph Support** - Natural pauses and intonation across paragraphs
🔒 **Privacy-focused** - All processing happens locally, no data sent to external servers
💾 **Easy Export** - Preview and download high-quality WAV files

</div>

<div align="center">

## 📸 Screenshots

<img src="https://via.placeholder.com/400x225?text=Main+Interface" alt="Interface" width="400"/>
<img src="https://via.placeholder.com/400x225?text=Audio+Generation" alt="Generation" width="400"/>

</div>

<div align="center">

## 🚀 Quick Start

</div>

### Prerequisites

- Python 3.12
- pip
- uv

### Installation

```bash
# Clone the repository
git clone https://github.com/WilleIshere/KokoroTTSGenerator.git
cd KokoroTTSGenerator

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

### Running the Application

```bash
python app.py
```

The web interface will automatically open in your default browser, ready for instant, high-quality audio generation with minimal latency.

<div align="center">

## 🎯 How to Use

</div>

1. **Enter Text** - Type or paste the text you want to convert into the text area
2. **Select Voice** - Choose your preferred voice from the dropdown menu
3. **Adjust Parameters** - Fine-tune speed and pitch using the sliders
4. **Generate** - Click "Generate Audio" and wait for processing to complete
5. **Preview & Download** - Listen to the high-quality generated audio immediately and download the WAV file

<div align="center">

## 🧩 Project Structure

</div>

```
KokoroTTSGenerator/
├── app.py                # Application entry point
├── src/
│   ├── gui.py            # NiceGUI interface implementation
│   └── tts.py            # TTS pipeline functionality
├── final_audio/          # Output directory for generated audio
├── temp/                 # Temporary processing directory
└── pyproject.toml        # Dependencies and project configuration
```

<div align="center">

## ⚡ Performance

</div>

Kokoro TTS Generator delivers exceptional performance:

- **Generation Speed**: Converts text to speech in mere seconds
- **High-Quality Output**: Studio-grade audio clarity with natural inflections
- **Resource Efficient**: Optimized to run smoothly even on modest hardware
- **Responsive Interface**: No lag between input and audio generation

<div align="center">

## 🛠️ Development

</div>

### Setting Up Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"
```

<div align="center">

### Tech Stack

</div>

<div align="center">

**[Kokoro TTS](https://github.com/zzmp/Kokoro)** - High-quality, ultra-fast text-to-speech engine
**[NiceGUI](https://nicegui.io/)** - Python UI framework for building web interfaces
**[SoundFile](https://pysoundfile.readthedocs.io/)** - Audio processing library
**[PyTorch](https://pytorch.org/)** - Deep learning framework powering the TTS models

</div>

<div align="center">

## 📋 Roadmap

</div>

<div align="center">

- [ ] Add batch processing support for even faster workflow
- [ ] Implement additional voice customization options for higher quality
- [ ] Create export options for different audio formats
- [ ] Add language support beyond English
- [ ] Develop advanced audio post-processing options for studio-quality output

</div>

<div align="center">

## 🤝 Contributing

</div>

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

<div align="center">

## 📄 License

</div>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<div align="center">

## 👤 Author

**WilleIshere** - [GitHub Profile](https://github.com/WilleIshere)

## 🙏 Acknowledgements

**[Kokoro TTS](https://github.com/zzmp/Kokoro)** - Core high-performance text-to-speech technology
**[NiceGUI](https://nicegui.io/)** - Elegant web interface framework
All open-source contributors who make projects like this possible

</div>
