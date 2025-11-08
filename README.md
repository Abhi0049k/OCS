# OCS - AI Landing Page Builder 🚀

OCS (Orchestration Control System) is an advanced AI-powered system that creates unique, high-quality landing pages. Unlike other AI builders that produce identical, obviously AI-generated UIs, OCS leverages sophisticated agent architecture to create distinctive, professionally-crafted landing pages.

## ✨ Features

- **Multi-Agent Architecture**: Specialized agents for layout, design taste, section creation, and quality control
- **Intelligent Design System**: AI-powered taste configuration with built-in design critic
- **Gemini AI Integration**: Leverages Google's Gemini AI for intelligent content and design generation
- **Quality Assurance**: Built-in critic agent ensures design quality with iterative improvements
- **Modular Section Agents**: Specialized agents for hero, footer, CTA, and general sections
- **Unique Output**: Generates distinctive designs that don't look obviously AI-made

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                            OCS                              │
│                  (Main Orchestrator)                       │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────┐│
│  │   Layout    │  │    Taste     │  │   Landing Page      ││
│  │   Agent     │  │   Agent      │  │      Agent          ││
│  └─────────────┘  └──────────────┘  └─────────────────────┘│
│                    │              │                        │
│                    │   Taste      │                        │
│                    │   Critic     │                        │
│                    └──────────────┘                        │
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │              Section Agents                             ││
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐      ││
│  │  │  Hero   │ │ Footer  │ │   CTA   │ │ General │      ││
│  │  │ Agent   │ │ Agent   │ │ Agent   │ │ Agent   │      ││
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘      ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Gemini AI API Key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Abhi0049k/OCS.git
cd OCS
```

2. Install dependencies:
```bash
pip install -e .
```

3. Set up your Gemini AI API key:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

### Usage

```python
from src.ocs import OCS

# Initialize the system
ocs = OCS()

# Generate a landing page
result = ocs.process_user_prompt(
    "Create a modern landing page for a tech startup selling AI tools"
)

print(result)
```

## 📁 Project Structure

```
OCS/
├── src/
│   ├── ocs/                    # Main orchestrator
│   ├── agents/                 # Agent implementations
│   │   ├── layout/            # Layout determination
│   │   ├── taste/             # Design taste & critic
│   │   ├── landing_page/      # Page orchestration
│   │   └── sections/          # Section-specific agents
│   │       ├── hero/
│   │       ├── footer/
│   │       ├── cta/
│   │       └── general/
│   ├── config/                # Configuration
│   └── utils/                 # Utilities
├── data/                      # Reference designs & configs
├── outputs/                   # Generated landing pages
├── tests/                     # Test suite
└── README.md
```

## 🤖 Agent Details

### Layout Agent
- Analyzes user prompts to determine optimal section structure
- Decides section types, order, and requirements
- Provides contextual descriptions for each section

### Taste Agent
- Creates comprehensive UI taste configurations
- Analyzes user preferences for colors, typography, spacing
- Generates cohesive design systems

### Taste Critic
- Quality assurance for design configurations
- Can iterate up to 3 times for improvements
- Validates against design principles and user requirements

### Landing Page Agent
- Orchestrates the complete page creation process
- Coordinates between section agents
- Generates final HTML/CSS output

### Section Agents
- **Hero Agent**: Specialized in compelling hero sections
- **Footer Agent**: Creates appropriate footer content
- **CTA Agent**: Optimizes call-to-action sections
- **General Agent**: Handles any custom section types

## 🛠️ Development

### Setting up Development Environment

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Run tests:
```bash
pytest
```

3. Code formatting:
```bash
black src/
```

4. Type checking:
```bash
mypy src/
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

- Create an issue for bugs or feature requests
- Join our discussions for questions and ideas
- Check the documentation for detailed guides

## 🔮 Roadmap

- [ ] Vector database integration for design references
- [ ] Advanced prompt engineering
- [ ] Custom section type creation
- [ ] Export to various frameworks (React, Vue, etc.)
- [ ] Live preview capabilities
- [ ] Design system generation

---

Built with ❤️ by the OCS Team
