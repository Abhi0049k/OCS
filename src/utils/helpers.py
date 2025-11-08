"""
Utility functions for the OCS AI Landing Page Builder.
"""

import json
import logging
import os
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path


def setup_logging(config: Dict[str, Any] = None) -> logging.Logger:
    """
    Set up logging for the application.
    
    Args:
        config (Dict[str, Any], optional): Logging configuration
        
    Returns:
        logging.Logger: Configured logger instance
    """
    if config is None:
        config = {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "file": "ocs.log"
        }
    
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, config["level"]),
        format=config["format"],
        handlers=[
            logging.FileHandler(log_dir / config["file"]),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)


def save_json(data: Dict[str, Any], filepath: str, pretty_print: bool = True) -> bool:
    """
    Save data to JSON file.
    
    Args:
        data (Dict[str, Any]): Data to save
        filepath (str): File path to save to
        pretty_print (bool): Whether to format JSON nicely
        
    Returns:
        bool: Success status
    """
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            if pretty_print:
                json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                json.dump(data, f, ensure_ascii=False)
        return True
    except Exception as e:
        logging.error(f"Failed to save JSON to {filepath}: {e}")
        return False


def load_json(filepath: str) -> Optional[Dict[str, Any]]:
    """
    Load data from JSON file.
    
    Args:
        filepath (str): File path to load from
        
    Returns:
        Optional[Dict[str, Any]]: Loaded data or None if failed
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load JSON from {filepath}: {e}")
        return None


def save_html(content: str, filepath: str) -> bool:
    """
    Save HTML content to file.
    
    Args:
        content (str): HTML content
        filepath (str): File path to save to
        
    Returns:
        bool: Success status
    """
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        logging.error(f"Failed to save HTML to {filepath}: {e}")
        return False


def save_jsx(content: str, filepath: str) -> bool:
    """
    Save JSX content to file.
    
    Args:
        content (str): JSX content
        filepath (str): File path to save to
        
    Returns:
        bool: Success status
    """
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        logging.error(f"Failed to save JSX to {filepath}: {e}")
        return False


def save_css(content: str, filepath: str) -> bool:
    """
    Save CSS content to file.
    
    Args:
        content (str): CSS content
        filepath (str): File path to save to
        
    Returns:
        bool: Success status
    """
    try:
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        logging.error(f"Failed to save CSS to {filepath}: {e}")
        return False


def generate_timestamp() -> str:
    """
    Generate timestamp string for file naming.
    
    Returns:
        str: Timestamp in format YYYYMMDD_HHMMSS
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing/replacing invalid characters.
    
    Args:
        filename (str): Original filename
        
    Returns:
        str: Sanitized filename
    """
    # Replace spaces and special characters
    sanitized = "".join(c if c.isalnum() or c in "._-" else "_" for c in filename)
    
    # Remove consecutive underscores
    while "__" in sanitized:
        sanitized = sanitized.replace("__", "_")
    
    # Remove leading/trailing underscores
    return sanitized.strip("_")


def create_project_structure(base_path: str) -> bool:
    """
    Create project directory structure.
    
    Args:
        base_path (str): Base path for project
        
    Returns:
        bool: Success status
    """
    directories = [
        "data/reference_designs",
        "data/taste_configs",
        "outputs",
        "logs"
    ]
    
    try:
        base_path = Path(base_path)
        
        for directory in directories:
            (base_path / directory).mkdir(parents=True, exist_ok=True)
        
        return True
    except Exception as e:
        logging.error(f"Failed to create project structure: {e}")
        return False


def validate_taste_config(config: Dict[str, Any]) -> List[str]:
    """
    Validate taste configuration structure.
    
    Args:
        config (Dict[str, Any]): Taste configuration to validate
        
    Returns:
        List[str]: List of validation errors
    """
    errors = []
    required_sections = ["color_scheme", "typography", "spacing", "style"]
    
    for section in required_sections:
        if section not in config:
            errors.append(f"Missing required section: {section}")
    
    # Validate color scheme
    if "color_scheme" in config:
        required_colors = ["primary_color", "secondary_color", "accent_color"]
        for color in required_colors:
            if color not in config["color_scheme"]:
                errors.append(f"Missing required color: {color}")
    
    # Validate typography
    if "typography" in config:
        required_fonts = ["heading_font", "body_font"]
        for font in required_fonts:
            if font not in config["typography"]:
                errors.append(f"Missing required font: {font}")
    
    return errors


def merge_configurations(base_config: Dict[str, Any], 
                        override_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two configuration dictionaries.
    
    Args:
        base_config (Dict[str, Any]): Base configuration
        override_config (Dict[str, Any]): Override configuration
        
    Returns:
        Dict[str, Any]: Merged configuration
    """
    merged = base_config.copy()
    
    for key, value in override_config.items():
        if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
            merged[key] = merge_configurations(merged[key], value)
        else:
            merged[key] = value
    
    return merged


def extract_keywords(text: str) -> List[str]:
    """
    Extract keywords from text for analysis.
    
    Args:
        text (str): Input text
        
    Returns:
        List[str]: List of extracted keywords
    """
    # Simple keyword extraction - can be enhanced with NLP
    words = text.lower().split()
    
    # Filter out common stop words
    stop_words = {"the", "is", "are", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "a", "an"}
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    
    return keywords


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human readable format.
    
    Args:
        size_bytes (int): Size in bytes
        
    Returns:
        str: Formatted file size
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


class FileManager:
    """Helper class for managing project files."""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def save_landing_page(self, landing_page: Dict[str, Any], project_name: str) -> Dict[str, str]:
        """
        Save complete landing page to files.
        
        Args:
            landing_page (Dict[str, Any]): Landing page data
            project_name (str): Project name for file naming
            
        Returns:
            Dict[str, str]: Dictionary of saved file paths
        """
        timestamp = generate_timestamp()
        safe_name = sanitize_filename(project_name)
        output_dir = self.base_path / "outputs" / f"{safe_name}_{timestamp}"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create React component structure
        components_dir = output_dir / "components"
        components_dir.mkdir(exist_ok=True)
        
        saved_files = {}
        
        # Save JSON data
        json_path = output_dir / "landing_page.json"
        if save_json(landing_page, str(json_path)):
            saved_files["json"] = str(json_path)
        
        # Save React components
        if "react_components" in landing_page:
            react_components = landing_page["react_components"]
            
            # Save main LandingPage component
            if "LandingPage" in react_components:
                main_component_path = output_dir / "LandingPage.jsx"
                if save_jsx(react_components["LandingPage"], str(main_component_path)):
                    saved_files["main_component"] = str(main_component_path)
            
            # Save individual section components
            for component_name, component_code in react_components.items():
                if component_name != "LandingPage":
                    component_path = components_dir / f"{component_name}.jsx"
                    if save_jsx(component_code, str(component_path)):
                        saved_files[f"component_{component_name.lower()}"] = str(component_path)
        
        # Save component styles
        if "component_styles" in landing_page:
            styles = landing_page["component_styles"]
            
            # Save global CSS
            if "global_css" in styles:
                css_path = output_dir / "globals.css"
                if save_css(styles["global_css"], str(css_path)):
                    saved_files["global_css"] = str(css_path)
            
            # Save theme config
            if "theme_config" in styles:
                theme_path = output_dir / "theme.js"
                if save_jsx(styles["theme_config"], str(theme_path)):
                    saved_files["theme_config"] = str(theme_path)
        
        # Create package.json for React project
        package_json = {
            "name": safe_name.lower().replace("_", "-"),
            "version": "1.0.0",
            "description": f"AI Generated Landing Page: {project_name}",
            "main": "LandingPage.jsx",
            "scripts": {
                "dev": "next dev",
                "build": "next build",
                "start": "next start",
                "lint": "next lint"
            },
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "next": "^14.0.0"
            },
            "devDependencies": {
                "eslint": "^8.0.0",
                "eslint-config-next": "^14.0.0"
            },
            "keywords": ["landing-page", "react", "ai-generated"],
            "author": "OCS AI Landing Page Builder",
            "license": "MIT"
        }
        
        package_json_path = output_dir / "package.json"
        if save_json(package_json, str(package_json_path)):
            saved_files["package_json"] = str(package_json_path)
        
        # Create README.md
        readme_content = f"""# {project_name}

AI-generated landing page created by OCS (Orchestration Control System).

## Generated Components

- **LandingPage.jsx** - Main page component
- **components/** - Individual section components
- **globals.css** - Global styles
- **theme.js** - Theme configuration

## Quick Start

1. Install dependencies:
```bash
npm install
```

2. Run development server:
```bash
npm run dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
{safe_name}/
├── LandingPage.jsx          # Main component
├── components/              # Section components
│   ├── HeroSection.jsx
│   ├── FooterSection.jsx
│   └── ...
├── globals.css             # Global styles
├── theme.js               # Theme configuration
├── package.json           # Dependencies
└── README.md             # This file
```

## Customization

- Edit components in the `components/` directory
- Modify styles in `globals.css` or component inline styles
- Update theme configuration in `theme.js`

---
Generated by OCS AI Landing Page Builder
"""
        
        readme_path = output_dir / "README.md"
        if save_html(readme_content, str(readme_path)):
            saved_files["readme"] = str(readme_path)
        
        self.logger.info(f"React landing page saved to {output_dir}")
        return saved_files
    
    def list_projects(self) -> List[Dict[str, Any]]:
        """
        List all saved projects.
        
        Returns:
            List[Dict[str, Any]]: List of project information
        """
        projects = []
        outputs_dir = self.base_path / "outputs"
        
        if outputs_dir.exists():
            for project_dir in outputs_dir.iterdir():
                if project_dir.is_dir():
                    json_file = project_dir / "landing_page.json"
                    if json_file.exists():
                        project_data = load_json(str(json_file))
                        if project_data:
                            projects.append({
                                "name": project_dir.name,
                                "path": str(project_dir),
                                "created": datetime.fromtimestamp(project_dir.stat().st_ctime),
                                "metadata": project_data.get("metadata", {})
                            })
        
        return sorted(projects, key=lambda x: x["created"], reverse=True)