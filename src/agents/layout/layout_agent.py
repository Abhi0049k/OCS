"""
Layout Agent

Decides the sections and their order for landing pages.
Provides descriptions for each section (e.g., hero section, footer).
"""

from src.utils.gemini_client import gemini_client
from typing import List, Dict, Any
import logging


class LayoutAgent:
    """
    Agent responsible for determining the structure and layout of landing pages.
    
    This agent analyzes user prompts and decides what sections should be included
    and in what order they should appear.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.gemini_client = gemini_client
        
        # Common section types
        self.section_types = {
            "hero": "Hero section - main headline and call-to-action",
            "features": "Features section - highlighting key product features",
            "about": "About section - company or product information", 
            "testimonials": "Testimonials section - customer reviews and feedback",
            "pricing": "Pricing section - product pricing plans",
            "cta": "Call-to-action section - encouraging user action",
            "footer": "Footer section - contact info and links",
            "nav": "Navigation section - site navigation menu",
            "general": "General content section - customizable content block"
        }
    
    def analyze_prompt(self, user_prompt: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Analyze user prompt and determine optimal layout structure.
        
        Args:
            user_prompt (str): User's description of desired landing page
            context (Dict[str, Any], optional): Additional context
            
        Returns:
            Dict[str, Any]: Layout structure with sections and descriptions
        """
        self.logger.info("Layout Agent analyzing user prompt")
        
        # TODO: Implement Gemini model integration for layout analysis
        
        # For now, return a default structure
        layout_structure = self.gemini_client.analyze_prompt_for_layout(user_prompt)
         
        if layout_structure and "sections" in layout_structure:
            self.logger.info("Successfully generated layout with Gemini")
            layout_structure["total_sections"] = len(layout_structure["sections"])
            layout_structure["user_prompt"] = user_prompt
            return layout_structure

        # Fallback to default structure if Gemini fails
        self.logger.warning("Failed to get layout from Gemini, using default structure")

        layout_structure = {
            "sections": [
                {
                    "type": "nav",
                    "position": 1,
                    "description": self.section_types["nav"],
                    "required": True
                },
                {
                    "type": "hero", 
                    "position": 2,
                    "description": self.section_types["hero"],
                    "required": True
                },
                {
                    "type": "features",
                    "position": 3, 
                    "description": self.section_types["features"],
                    "required": False
                },
                {
                    "type": "cta",
                    "position": 4,
                    "description": self.section_types["cta"],
                    "required": True
                },
                {
                    "type": "footer",
                    "position": 5,
                    "description": self.section_types["footer"],
                    "required": True
                }
            ],
            "total_sections": 5,
            "user_prompt": user_prompt
        }
        
        return layout_structure
    
    def get_section_description(self, section_type: str) -> str:
        """Get description for a specific section type."""
        return self.section_types.get(section_type, "Custom section")