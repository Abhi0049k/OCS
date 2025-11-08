"""
Gemini AI integration utilities.
"""

import google.generativeai as genai
import json
import logging
from typing import Dict, Any, Optional, List
from ..config import config


class GeminiClient:
    """Client for interacting with Gemini AI."""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.model = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the Gemini client."""
        try:
            if not config.GEMINI_API_KEY:
                self.logger.warning("Gemini API key not configured. AI features will be disabled.")
                return
            
            genai.configure(api_key=config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel(config.GEMINI_MODEL)
            self.logger.info("Gemini client initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Gemini client: {e}")
    
    def generate_content(self, prompt: str, max_tokens: int = 1000) -> Optional[str]:
        """
        Generate content using Gemini AI.
        
        Args:
            prompt (str): The prompt to send to Gemini
            max_tokens (int): Maximum tokens to generate
            
        Returns:
            Optional[str]: Generated content or None if failed
        """
        if not self.model:
            self.logger.error("Gemini client not initialized")
            return None
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            self.logger.error(f"Failed to generate content: {e}")
            return None
    
    def analyze_prompt_for_layout(self, user_prompt: str) -> Optional[Dict[str, Any]]:
        """
        Analyze user prompt to determine optimal layout structure.
        
        Args:
            user_prompt (str): User's description of desired landing page
            
        Returns:
            Optional[Dict[str, Any]]: Layout analysis or None if failed
        """
        prompt = f"""
        Analyze this user prompt for a landing page and determine the optimal layout structure:
        
        User Prompt: "{user_prompt}"
        
        Based on the prompt, suggest:
        1. What sections should be included (hero, features, testimonials, pricing, about, cta, footer, etc.)
        2. The order of these sections
        3. Whether each section is required or optional
        4. Brief description of what each section should contain
        
        Return the response as a JSON object with this structure:
        {{
            "sections": [
                {{
                    "type": "section_type",
                    "position": 1,
                    "description": "what this section should contain",
                    "required": true/false
                }}
            ],
            "reasoning": "explanation of why this layout was chosen"
        }}
        """
        
        response = self.generate_content(prompt)
        if response:
            try:
                # Extract JSON from response
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                json_str = response[json_start:json_end]
                return json.loads(json_str)
            except Exception as e:
                self.logger.error(f"Failed to parse layout analysis response: {e}")
        
        return None
    
    def analyze_prompt_for_taste(self, user_prompt: str) -> Optional[Dict[str, Any]]:
        """
        Analyze user prompt to determine UI taste preferences.
        
        Args:
            user_prompt (str): User's description of desired design
            
        Returns:
            Optional[Dict[str, Any]]: Taste analysis or None if failed
        """
        prompt = f"""
        Analyze this user prompt for UI taste and design preferences:
        
        User Prompt: "{user_prompt}"
        
        Based on the prompt, determine:
        1. Color scheme (primary, secondary, accent colors)
        2. Typography preferences (modern, classic, etc.)
        3. Overall aesthetic (modern, minimalist, corporate, creative, etc.)
        4. Spacing and layout preferences
        5. Animation and interaction preferences
        
        Return the response as a JSON object with this structure:
        {{
            "color_scheme": {{
                "primary_color": "#hex",
                "secondary_color": "#hex",
                "accent_color": "#hex",
                "text_color": "#hex",
                "background_color": "#hex"
            }},
            "typography": {{
                "heading_font": "font_name",
                "body_font": "font_name",
                "heading_weight": "weight",
                "body_weight": "weight",
                "font_scale": "small/medium/large"
            }},
            "spacing": {{
                "section_padding": "small/medium/large",
                "element_spacing": "tight/medium/loose",
                "container_max_width": "1200px"
            }},
            "style": {{
                "overall_aesthetic": "modern/classic/minimalist/etc",
                "corner_radius": "none/small/medium/large",
                "shadow_style": "none/subtle/prominent",
                "animation_level": "none/minimal/moderate/heavy"
            }},
            "reasoning": "explanation of design choices"
        }}
        """
        
        response = self.generate_content(prompt)
        if response:
            try:
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                json_str = response[json_start:json_end]
                return json.loads(json_str)
            except Exception as e:
                self.logger.error(f"Failed to parse taste analysis response: {e}")
        
        return None
    
    def critique_taste_config(self, taste_config: Dict[str, Any], user_prompt: str) -> Optional[Dict[str, Any]]:
        """
        Critique a taste configuration for quality and appropriateness.
        
        Args:
            taste_config (Dict[str, Any]): Configuration to critique
            user_prompt (str): Original user prompt
            
        Returns:
            Optional[Dict[str, Any]]: Critique analysis or None if failed
        """
        prompt = f"""
        Critique this UI taste configuration based on the user's requirements:
        
        User Prompt: "{user_prompt}"
        
        Taste Configuration:
        {json.dumps(taste_config, indent=2)}
        
        Evaluate the configuration for:
        1. Color harmony and accessibility (contrast ratios)
        2. Typography consistency and readability
        3. Appropriateness for the user's requirements
        4. Overall design coherence
        5. Modern design standards compliance
        
        Provide a quality score from 0.0 to 1.0 and specific improvement suggestions.
        
        Return the response as a JSON object:
        {{
            "quality_score": 0.85,
            "acceptable": true/false,
            "issues": [
                "list of specific issues found"
            ],
            "suggestions": [
                "list of specific improvement suggestions"
            ],
            "overall_feedback": "summary of the critique"
        }}
        """
        
        response = self.generate_content(prompt)
        if response:
            try:
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                json_str = response[json_start:json_end]
                return json.loads(json_str)
            except Exception as e:
                self.logger.error(f"Failed to parse critique response: {e}")
        
        return None
    
    def generate_section_content(self, section_type: str, taste_config: Dict[str, Any], 
                                context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Generate content for a specific section type.
        
        Args:
            section_type (str): Type of section to generate
            taste_config (Dict[str, Any]): UI taste configuration
            context (Dict[str, Any]): Additional context
            
        Returns:
            Optional[Dict[str, Any]]: Generated section content or None if failed
        """
        prompt = f"""
        Generate content for a {section_type} section of a landing page.
        
        Taste Configuration:
        {json.dumps(taste_config, indent=2)}
        
        Context:
        {json.dumps(context, indent=2)}
        
        Generate appropriate content including:
        1. Headlines and text content
        2. Call-to-action buttons (if applicable)
        3. Styling specifications that match the taste configuration
        4. Layout structure
        
        Return as JSON object with structure appropriate for {section_type} section.
        """
        
        response = self.generate_content(prompt)
        if response:
            try:
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                json_str = response[json_start:json_end]
                return json.loads(json_str)
            except Exception as e:
                self.logger.error(f"Failed to parse section content response: {e}")
        
        return None


# Global Gemini client instance
gemini_client = GeminiClient()