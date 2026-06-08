# AI 2 – Aura Lab CLI Assistant

AI 2 is a Python command‑line assistant that combines AI‑style prompt generation, math tools, Google & Workspace launchers, a festivals calendar, and full local history logging – all in one simple terminal app.

It is designed for quick daily use: generate prompts for image models, solve math, open Google apps fast, check today’s date/time and festivals (India + world), and keep a personal activity log on your own machine.[web:206][web:209]

---

## Features

- **Prompt + Image Helper**
  - Turn a short idea into a long, detailed prompt.
  - Open **Perchance Stable Diffusion** and **StableDiffusionWeb** directly from the app to generate images.
  - Save all prompt ideas and generated prompts to `prompts_history.txt`.

- **Math Tools**
  - Simple calculator using safe math evaluation.
  - Extra tools:
    - Quadratic equation solver.
    - Area & perimeter helper (rectangle, circle, triangle).
  - Quick **math formula sheet** (basic to class 12 style).
  - Basic **physics formula sheet** (motion, force, energy, electricity).

- **Date / Time / Festivals**
  - Shows:
    - Current day, date, month, year.
    - Time in **24‑hour** and **12‑hour (AM/PM)** formats.
  - India‑focused festivals list for **2026** (month‑wise) plus selected world fixed‑date festivals.
  - Notes for movable festivals (Ramadan, Eid, Diwali, Easter, etc.) whose dates change every year.

- **Google & Workspace Launchers**
  - Fast open for main Google services:
    - Google Search, Gmail, Maps, YouTube, Drive, Calendar, Docs, Sheets, Slides, Photos, Forms, Sites, and more.[web:113][web:198]
  - Google Workspace (India) links:
    - Workspace Gmail, Drive, Meet, Calendar, Chat, Docs, Sheets, Slides, Vids, Keep, Sites, Forms, Tasks, NotebookLM, AppSheet, Workspace Marketplace.

- **Wikipedia Tools**
  - Open Wikipedia home.
  - Direct search: type a topic, it opens the matching Wikipedia page in your browser.

- **Aura Lab / Social Links**
  - Central menu for your personal links:
    - Aura Lab: **Cares & Laughs 1 & 2** (CodePen)
    - Instagram, Facebook, GitHub
    - Aura Lab Discord server
    - Care Lab Studio YouTube channel
    - Note about the Sekai app (search from your app store)

- **History Logging**
  - All app activity is logged with timestamps into:
    - `C:\Users\HP\AI 2 History\AI 2 history.txt`
  - Logs:
    - Main menu choices
    - Prompt ideas and generation
    - Math expressions and results/errors
    - Google/Wiki/links opened
  - The same folder is intended as a place to store your own **screenshots** from any device, so everything is collected together.

---

## Folder Structure

Example layout:

```text
AI-2/
├─ AI 2.py                # main Python script (CLI app)
├─ prompts_history.txt    # auto‑created prompt history
├─ README.md              # this file
└─ (created at runtime)
   C:\Users\HP\AI 2 History\
       AI 2 history.txt   # main activity log with timestamps
       (your screenshots) # you can manually drop images here
```

> Note: `C:\Users\HP\AI 2 History` is created automatically when you run the app on Windows. You can change the base path in the code if needed.

---

## Requirements

- **Python 3.8+** (any recent 3.x should work)
- Standard library only (no external packages):
  - `webbrowser`, `datetime`, `os`, `math`, `urllib.parse`.[web:198][web:199]

No extra installations are required – just Python.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

2. **Make sure Python is installed**

On Windows:

```bash
python --version
```

If `python` doesn’t work, try:

```bash
py --version
```

3. (Optional) Create and activate a virtual environment if you want an isolated setup.

---

## Usage

From the project folder, run:

```bash
python "AI 2.py"
```

or on some Windows setups:

```bash
py "AI 2.py"
```

You’ll see a menu similar to:

```text
AI 2: Prompts + Math + Google + Wiki + Festivals
1. Prompt + Image Helper
2. Math Solver (Calculator)
3. Extra Math Tools
4. Math Formulas
5. Physics Formulas
6. Date / Time / Festivals (India + World)
7. Wikipedia Home
8. Wikipedia Search
9. Google Products
10. Aura Lab / Social Links
11. Credits
12. Exit
```

### Common flows

- **Generate an AI image prompt**
  1. Choose `1` (Prompt + Image Helper).
  2. Type a short idea (e.g. `cyberpunk city at night`).
  3. Copy the generated long prompt.
  4. Optionally choose to open Perchance or StableDiffusionWeb and paste the prompt.

- **Quick math**
  1. Choose `2` (Math Solver).
  2. Type expressions like `2+3*4`, `(5**2 + 3)/4`, or `sqrt(16) + sin(0.5)`.
  3. Type `back` to return.

- **Check today’s date/time and festivals**
  1. Choose `6`.
  2. See current day/date/time in both 24h and 12h formats.
  3. See all India + world fixed‑date festivals for today (if any) and a note about movable festivals.

- **Open Google/Workspace apps**
  1. Choose `9` (Google Products).
  2. Select a category (Main Google Apps, Workspace, AI & Labs, etc.).
  3. Pick the specific service to open in your default browser.

- **Open Aura Lab links**
  1. Choose `10`.
  2. Pick the CodePen, social, Discord, or YouTube link you want.
  3. Browser opens directly to that link.

---

## Configuration

Some things you might want to change:

- **History folder**

In `AI 2.py`:

```python
HISTORY_DIR = r"C:\Users\HP\AI 2 History"
```

Change this to another path if your Windows username is different or you want a different drive/folder.

- **Author / branding**

In the `show_credits()` function you can change:

```python
print("Created by: Kavyant (Aura Lab / Care Lab Studio)")
```

to your preferred name or brand.

- **Festivals list**

The India 2026 and world fixed‑date festivals are defined at the top in:

```python
INDIA_FESTIVALS_2026 = { ... }
WORLD_FESTIVALS_FIXED = { ... }
```

You can edit, add, or remove entries as needed.

---

## Roadmap / Ideas

Possible future improvements:

- Add configuration file instead of hard‑coded paths.
- More years for Indian and world festivals.
- Export history as JSON/CSV.
- Package as an installable Python package or Windows executable (.exe).

---

## Credits

- **Author:** Kavyant – Aura Lab / Care Lab Studio  
- **Assistant:** Perplexity AI (planning & code suggestions)

Aura Lab / Care Lab links:

- Cares & Laughs 2 (CodePen): https://codepen.io/Kavyant-Kumar/pen/dPOXwmY  
- Cares & Laughs 1 (CodePen): https://codepen.io/Kavyant-Kumar/pen/dPGJPKj  
- Instagram: https://www.instagram.com/kavyanthub/  
- Facebook: https://www.facebook.com/profile.php?id=61586003535719  
- GitHub: https://github.com/Kiik913  
- Aura Lab Discord server (channel link)  
- YouTube: https://www.youtube.com/@CareLabStudio  
- Many cool projects and ideas also live in the **Sekai** app.

---

## License

Choose a license you prefer (MIT is common for small tools).[web:206]

Example MIT section:

```text
This project is licensed under the MIT License – see the LICENSE file for details.
```

(If you want AI-23-V.10.1.0 here is the link:- https://github.com/Kiik913/AI-23-V.10.1.0-)
