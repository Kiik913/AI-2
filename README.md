# 🤖 AI 2 - Your Local AI Assistant

A powerful Python-based AI application with multiple features including prompts, math, video generation, chat, and history logging.

**Screenshort**
<img width="1920" height="1046" alt="Screenshot 2026-07-07 160319" src="https://github.com/user-attachments/assets/c57b4162-028b-4069-bebf-e206c476df6e" />

## ✨ Features

- **1️⃣ AI Prompts**: Get smart answers and help with tasks
- **2️⃣ Math Solver**: Solve complex math problems
- **3️⃣ AI Video**: Text-to-video generation with HunyuanVideo
- **4️⃣ Gemma 4 Chat**: Local offline AI chat with Google's Gemma 4
- **5️⃣ History Logger**: Track all your conversations and actions
- **6️⃣ Google & Wiki**: Search Google and Wikipedia integration
- **7️⃣ Festivals**: Get information about festivals and events

## 🚀 Installation

### Prerequisites

```bash
pip install -U transformers==5.5.0 torch accelerate torchvision
```

### Set Hugging Face Token

1. Create token at: https://huggingface.co/settings/tokens
2. Token type: **Read**
3. Add to your script:

```python
os.environ['HF_TOKEN'] = 'hf_your_token_here'
```

Or use command line:

```bash
set HF_TOKEN=hf_your_token_here
python AI_2.py
```

## 🔧 Usage

Run the application:

```bash
python AI_2.py
```

Choose from menu options 1-16:

---


## 📦 Dependencies

- `transformers>=5.5.0`
- `torch>=2.12.0`
- `accelerate>=1.13.0`
- `torchvision>=0.27.0`
- `huggingface_hub>=1.18.0`

## 🧠 AI Models

- **HunyuanVideo**: Text-to-video generation (Tencent)
- **Gemma 4-E4B-it**: Local multimodal AI chat (Google)
- **Gemma 4-E2B-it**: Smaller version (1GB, recommended for low disk space)

## 💻 System Requirements

- **Disk Space**: 16GB+ for Gemma 4-E4B, 2-3GB for Gemma 4-E2B
- **RAM**: 8GB+ recommended
- **GPU**: CUDA-compatible NVIDIA GPU for faster inference

## 📝 License

MIT License

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📮 Contact

- **GitHub**: Kiik913
- **Project**: AI-2

## 🎯 Quick Start

```bash
# 1. Install dependencies
pip install -U transformers==5.5.0 torch accelerate torchvision

# 2. Set HF_TOKEN
set HF_TOKEN=hf_your_token_here

# 3. Run AI 2
python AI_2.py

# 4. Choose option 15 or 16
```

---

**Made with ❤️ for Aura Lab projects**
## Credits

- **Author:** Kavyant – Aura Lab / Care Lab Studio  
- **Assistant:** Perplexity AI (planning & code suggestions)

Aura Lab / Care Lab links:

- Cares & Laughs 2 (CodePen): <https://codepen.io/Kavyant-Kumar/pen/dPOXwmY>  
- Cares & Laughs 1 (CodePen): <https://codepen.io/Kavyant-Kumar/pen/dPGJPKj>  
- Instagram: <https://www.instagram.com/kavyanthub/>  
- Facebook: <https://www.facebook.com/profile.php?id=61586003535719>  
- GitHub: <https://github.com/Kiik913>  
- Aura Lab Discord server (channel link)  
- YouTube: <https://www.youtube.com/@CareLabStudio>  
- Many cool projects and ideas also live in the **Sekai** app.  

Related project:

- **AI‑23‑V.10.1.0:** <https://github.com/Kiik913/AI-23-V.10.1.0>

---

## License

Choose a license you prefer (MIT is common for small tools).[web:296][web:301]

Example MIT section:

```text
This project is licensed under the MIT License – see the LICENSE file for details.                                                              (If you want AI-23-V.10.1.0 here is the link:- [https://github.com/Kiik913/AI-23-V.10.1.0-](https://github.com/Kiik913/AI-23-V.10.1.0-))
```
