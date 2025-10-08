# Clan MacQuarrie

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Built with MkDocs](https://img.shields.io/badge/Built%20with-MkDocs-blue)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE?logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-222222?logo=github)](https://dmccreary.github.io/clan-macquarrie/)

An educational website dedicated to Clan MacQuarrie, an ancient Highland Scottish clan that originated in the Scottish Inner Hebrides. This site provides comprehensive resources about the clan system, Scottish history, and the MacQuarrie clan's significant role in Scotland's heritage.

## 🌐 Website

Visit the live site: **[https://dmccreary.github.io/clan-macquarrie/](https://dmccreary.github.io/clan-macquarrie/)**

## 📚 About

This website focuses on education about the Scottish clan system and the history of Clan MacQuarrie. It includes:

- **Clan History**: Origins, timeline of major events, chiefs, and the Jacobite period
- **Family History Research**: Resources for genealogical research
- **Visiting Scotland**: Guides for exploring clan territories and heritage sites
- **Land and Environment**: Information about traditional clan lands
- **Identity and Symbols**: Tartans, badges, and clan symbolism
- **Education**: Learning resources about Scottish culture and history
- **Research and Archives**: Access to historical documents and archives
- **Interactive Apps**: Timeline viewers and other educational tools

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- MkDocs and Material theme

### Installation

```bash
# Clone the repository
git clone https://github.com/dmccreary/clan-macquarrie
cd clan-macquarrie

# Set up Python environment (using conda)
conda create -n mkdocs python=3
conda activate mkdocs

# Install dependencies
pip install mkdocs "mkdocs-material[imaging]"
```

### Local Development

```bash
# Build the site
mkdocs build

# Run local development server at http://localhost:8000
mkdocs serve
```

### Deployment

```bash
# Deploy to GitHub Pages
mkdocs gh-deploy
```

**Note**: `mkdocs gh-deploy` publishes to GitHub Pages but does not commit source changes. Remember to separately commit and push your changes:

```bash
git add .
git commit -m "Your commit message"
git push
```

## 🏗️ Project Structure

```
clan-macquarrie/
├── docs/                 # Documentation source files
│   ├── content/         # Main content organized in chapters
│   │   ├── 01-clan-history/
│   │   ├── 02-family-history-research/
│   │   ├── 03-visit-scotland/
│   │   └── ...
│   ├── img/             # Images, logos, and icons
│   ├── css/             # Custom styling
│   ├── js/              # JavaScript for interactive features
│   └── sims/            # Interactive applications
├── mkdocs.yml           # MkDocs configuration
└── README.md            # This file
```

## 🤝 Contributing

Contributions are welcome! This is an educational resource for the community. If you have:

- Historical information or corrections
- Family research to share
- Suggestions for improvements
- Bug reports

Please feel free to open an issue or submit a pull request.

## 👤 Author

**Dan McCreary**

- LinkedIn: [@danmccreary](https://www.linkedin.com/in/danmccreary/)
- GitHub: [@dmccreary](https://github.com/dmccreary)

## 📄 License

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes

See [LICENSE](license.txt) for full details.

## 🙏 Acknowledgments

This project stands on the shoulders of giants. We are deeply grateful to the open source community and the incredible developers who have built the tools that make this site possible:

### Core Technologies

- **[MkDocs](https://www.mkdocs.org/)** - The brilliant static site generator that powers this documentation. Created by Tom Christie and maintained by a dedicated community of contributors.

- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - The stunning theme by Martin Donath that brings modern design, powerful features, and excellent accessibility to our site.

### Interactive Visualizations

- **[p5.js](https://p5js.org/)** - The creative coding library by Lauren McCarthy and the Processing Foundation that enables engaging interactive visualizations and educational animations.

- **[Vis.js](https://visjs.org/)** - The powerful dynamic browser-based visualization library that helps us create interactive network diagrams and data visualizations.

- **[vis-timeline](https://github.com/visjs/vis-timeline)** - The flexible timeline visualization library that brings our clan history to life with interactive timelines.

### Infrastructure

- **[GitHub](https://github.com)** - For hosting our code and providing an excellent collaboration platform.

- **[GitHub Pages](https://pages.github.com/)** - For free, reliable hosting of our static site.

### The Open Source Community

To all the maintainers, contributors, and supporters of these projects: thank you for your dedication, creativity, and generosity in sharing your work with the world. Open source software powers education, preserves history, and brings communities together. This website exists because of your efforts.

---

*In the spirit of the Scottish Highlands: "Beannachd leibh" (Blessings be with you)*
