# 🎨 Iro's Paint App

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*A simple, beautiful painting application built with Pygame*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure)

</div>

---

## ✨ Features

- **🖌️ Multiple Brush Sizes** - Choose from 4 different brush sizes (5px, 10px, 15px, 20px)
- **🎨 Color Palette** - Select from a variety of colors to bring your artwork to life
- **💾 Save Your Art** - Export your masterpiece as a PNG file
- **🧹 Clear Canvas** - Start fresh with a single click
- **🔊 Sound Effects** - Satisfying audio feedback for your interactions
- **👁️ Live Preview** - See your brush size and color as you move the cursor

---

## 📦 Installation

### Prerequisites

Make sure you have Python 3.x installed on your system.

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd paint-app
   ```

2. **Install dependencies**
   ```bash
   pip install pygame
   ```

3. **Verify your project structure**
   ```
   paint-app/
   ├── main.py
   ├── assets/
   │   └── sounds/
   │       └── select_sound.ogg
   ├── ui/
   │   └── canvas.py
   └── tools/
       └── brush.py
   ```

---

## 🚀 Usage

Run the application:

```bash
python main.py
```

### Controls

| Action | How To |
|--------|--------|
| **Paint** | Click and drag on the canvas (below the menu bar) |
| **Change Brush Size** | Click on the brush size buttons in the menu |
| **Change Color** | Click on any color in the palette |
| **Save Painting** | Click the SAVE button |
| **Clear Canvas** | Click the CLEAR button |
| **Exit** | Close the window or press ESC |

---

## 📁 Project Structure

```
paint-app/
│
├── main.py                 # Main application entry point
├── assets/
│   └── sounds/
│       └── select_sound.ogg  # UI interaction sound
├── ui/
│   └── canvas.py          # Canvas and menu rendering
└── tools/
    └── brush.py           # Brush class and painting logic
```

### Key Components

- **`main.py`** - Game loop, event handling, and core application logic
- **`Brush`** - Manages brush properties (color, size) and painting data
- **`draw_menu()`** - Renders the top menu bar with controls
- **`draw_painting()`** - Displays all painted strokes on the canvas

---

## 🎨 Screenshots

*Add your screenshots here to showcase your paint app!*

---

## 🛠️ Technical Details

- **Window Size:** 800x600 pixels
- **Canvas Area:** 800x530 pixels (menu bar: 70px)
- **Frame Rate:** 120 FPS
- **Export Format:** PNG

---

## 🔮 Future Enhancements

- [ ] Add eraser tool
- [ ] Implement undo/redo functionality
- [ ] Add more brush shapes (square, spray, etc.)
- [ ] Color picker with RGB sliders
- [ ] Layer support
- [ ] Load existing images for editing

---

## 📝 License

This project is licensed under the MIT License - feel free to use and modify as you wish!

---

## 💖 Acknowledgments

Built with [Pygame](https://www.pygame.org/) - the amazing Python game development library.

---

<div align="center">

**Happy Painting! 🎨✨**

Made with ❤️ and Python

</div>