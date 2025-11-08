"""
Taste Agent

Creates configuration files for UI taste and styling preferences.
Analyzes user prompts to determine appropriate design aesthetics.
"""

from typing import Dict, Any
import json
import logging


class TasteAgent:
    """
    Agent responsible for creating UI taste and styling configuration.
    
    Analyzes user prompts to determine color schemes, typography,
    spacing, and overall design aesthetic preferences.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Default taste categories
        self.taste_categories = {
            "color_scheme": {
                "primary_color": "#000000",
                "secondary_color": "#ffffff", 
                "accent_color": "#0066cc",
                "text_color": "#333333",
                "background_color": "#ffffff"
            },
            "typography": {
                "heading_font": "Inter",
                "body_font": "Inter",
                "heading_weight": "bold",
                "body_weight": "normal",
                "font_scale": "medium"
            },
            "spacing": {
                "section_padding": "large",
                "element_spacing": "medium",
                "container_max_width": "1200px"
            },
            "style": {
                "overall_aesthetic": "modern",
                "corner_radius": "medium", 
                "shadow_style": "subtle",
                "animation_level": "minimal"
            },
            "layout": {
                "grid_system": "12-column",
                "breakpoints": "responsive",
                "alignment": "center"
            }
        }
    
    def create_taste_config(self, user_prompt: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Create taste configuration based on user prompt.
        
        Args:
            user_prompt (str): User's description of desired design
            context (Dict[str, Any], optional): Additional context
            
        Returns:
            Dict[str, Any]: Comprehensive taste configuration
        """
        self.logger.info("Taste Agent creating configuration from prompt")
        
        # Analyze prompt for design preferences  
        prompt_lower = user_prompt.lower()
        
        # Determine color scheme based on keywords
        color_scheme = self._analyze_colors(prompt_lower)
        
        # Determine typography
        typography = self._analyze_typography(prompt_lower)
        
        # Determine spacing and style
        spacing = self._analyze_spacing(prompt_lower)
        style = self._analyze_style(prompt_lower)
        
        taste_config = {
            "color_scheme": color_scheme,
            "typography": typography,
            "spacing": spacing,
            "style": style,
            "metadata": {
                "created_from_prompt": user_prompt,
                "agent": "TasteAgent",
                "context": context or {}
            }
        }
        
        return taste_config
    
    def _analyze_colors(self, prompt: str) -> Dict[str, str]:
        """Analyze prompt for color preferences."""
        
        # Tech/startup themes
        if any(word in prompt for word in ["tech", "startup", "ai", "software", "app"]):
            return {
                "primary_color": "#1a1a1a",
                "secondary_color": "#ffffff", 
                "accent_color": "#007acc",
                "text_color": "#333333",
                "background_color": "#ffffff"
            }
        
        # Modern/minimal themes
        elif any(word in prompt for word in ["modern", "minimal", "clean", "simple"]):
            return {
                "primary_color": "#000000",
                "secondary_color": "#ffffff",
                "accent_color": "#0070f3",
                "text_color": "#1a1a1a",
                "background_color": "#fafafa"
            }
        
        # Creative/vibrant themes
        elif any(word in prompt for word in ["creative", "vibrant", "colorful", "agency", "design"]):
            return {
                "primary_color": "#6366f1",
                "secondary_color": "#ffffff",
                "accent_color": "#f59e0b",
                "text_color": "#374151",
                "background_color": "#ffffff"
            }
        
        # Luxury/elegant themes
        elif any(word in prompt for word in ["luxury", "elegant", "premium", "high-end"]):
            return {
                "primary_color": "#1f2937",
                "secondary_color": "#f9fafb",
                "accent_color": "#d97706",
                "text_color": "#374151",
                "background_color": "#ffffff"
            }
        
        # Default modern scheme
        else:
            return {
                "primary_color": "#1a1a1a",
                "secondary_color": "#ffffff",
                "accent_color": "#007acc",
                "text_color": "#333333",
                "background_color": "#ffffff"
            }
    
    def _analyze_typography(self, prompt: str) -> Dict[str, str]:
        """Analyze prompt for typography preferences."""
        
        # Professional/corporate
        if any(word in prompt for word in ["professional", "corporate", "business", "consulting"]):
            return {
                "heading_font": "Georgia",
                "body_font": "Arial",
                "heading_weight": "600",
                "body_weight": "400",
                "font_scale": "medium"
            }
        
        # Modern/tech
        elif any(word in prompt for word in ["modern", "tech", "startup", "ai", "software"]):
            return {
                "heading_font": "Inter",
                "body_font": "Inter",
                "heading_weight": "700",
                "body_weight": "400",
                "font_scale": "medium"
            }
        
        # Creative
        elif any(word in prompt for word in ["creative", "agency", "design", "art"]):
            return {
                "heading_font": "Poppins",
                "body_font": "Open Sans",
                "heading_weight": "600",
                "body_weight": "400",
                "font_scale": "large"
            }
        
        # Default
        else:
            return {
                "heading_font": "Inter",
                "body_font": "Inter", 
                "heading_weight": "600",
                "body_weight": "400",
                "font_scale": "medium"
            }
    
    def _analyze_spacing(self, prompt: str) -> Dict[str, str]:
        """Analyze prompt for spacing preferences."""
        
        # Minimal/clean = tight spacing
        if any(word in prompt for word in ["minimal", "clean", "compact"]):
            return {
                "section_padding": "60px",
                "element_spacing": "16px",
                "container_max_width": "1100px",
                "border_radius": "4px"
            }
        
        # Luxury/premium = generous spacing
        elif any(word in prompt for word in ["luxury", "premium", "elegant"]):
            return {
                "section_padding": "100px",
                "element_spacing": "32px",
                "container_max_width": "1300px",
                "border_radius": "8px"
            }
        
        # Default balanced spacing
        else:
            return {
                "section_padding": "80px",
                "element_spacing": "24px",
                "container_max_width": "1200px",
                "border_radius": "6px"
            }
    
    def _analyze_style(self, prompt: str) -> Dict[str, str]:
        """Analyze prompt for overall style preferences."""
        
        # Determine aesthetic
        if any(word in prompt for word in ["minimal", "clean", "simple"]):
            aesthetic = "minimalist"
        elif any(word in prompt for word in ["modern", "contemporary"]):
            aesthetic = "modern"
        elif any(word in prompt for word in ["creative", "vibrant"]):
            aesthetic = "creative"
        elif any(word in prompt for word in ["luxury", "elegant", "premium"]):
            aesthetic = "luxury"
        elif any(word in prompt for word in ["corporate", "professional", "business"]):
            aesthetic = "corporate"
        else:
            aesthetic = "modern"
        
        return {
            "overall_aesthetic": aesthetic,
            "corner_radius": "medium",
            "shadow_style": "subtle",
            "animation_level": "minimal"
        }
    
    def save_config(self, config: Dict[str, Any], filepath: str) -> bool:
        """Save taste configuration to file."""
        try:
            with open(filepath, 'w') as f:
                json.dump(config, f, indent=2)
            self.logger.info(f"Taste configuration saved to {filepath}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to save config: {e}")
            return False
    
    def load_config(self, filepath: str) -> Dict[str, Any]:
        """Load taste configuration from file."""
        try:
            with open(filepath, 'r') as f:
                config = json.load(f)
            self.logger.info(f"Taste configuration loaded from {filepath}")
            return config
        except Exception as e:
            self.logger.error(f"Failed to load config: {e}")
            return {}


def main():
    """Test the Taste Agent."""
    agent = TasteAgent()
    test_prompt = "Create a modern, sleek design for a tech startup selling AI tools"
    
    config = agent.create_taste_config(test_prompt)
    print("Taste Configuration:")
    print(json.dumps(config, indent=2))


if __name__ == "__main__":
    main()