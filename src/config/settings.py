"""
Configuration settings for the OCS AI Landing Page Builder.
"""

import os
from typing import Dict, Any


class Config:
    """Configuration class for OCS system."""
    
    # Gemini AI Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCbxm88IFLDRCC1ni6Z3UOlmij4W322Zlc")
    GEMINI_MODEL = "gemini-2.5-flash-lite"
    
    # Default paths
    DATA_DIR = "data"
    REFERENCE_DESIGNS_DIR = os.path.join(DATA_DIR, "reference_designs")
    TASTE_CONFIGS_DIR = os.path.join(DATA_DIR, "taste_configs")
    OUTPUTS_DIR = "outputs"
    
    # Agent settings
    TASTE_CRITIC_MAX_ITERATIONS = 3
    TASTE_CRITIC_MIN_SCORE = 0.7
    
    # Default taste configuration
    DEFAULT_TASTE_CONFIG = {
        "color_scheme": {
            "primary_color": "#1a1a1a",
            "secondary_color": "#ffffff",
            "accent_color": "#007acc",
            "text_color": "#333333",
            "background_color": "#ffffff",
            "success_color": "#10b981",
            "warning_color": "#f59e0b",
            "error_color": "#ef4444"
        },
        "typography": {
            "heading_font": "Inter",
            "body_font": "Inter",
            "mono_font": "Fira Code",
            "heading_weight": "600",
            "body_weight": "400",
            "font_scale": "medium",
            "line_height": "1.6"
        },
        "spacing": {
            "section_padding": "80px",
            "element_spacing": "24px",
            "container_max_width": "1200px",
            "border_radius": "8px",
            "button_padding": "12px 24px"
        },
        "style": {
            "overall_aesthetic": "modern",
            "corner_radius": "medium",
            "shadow_style": "subtle",
            "animation_level": "minimal",
            "gradient_style": "subtle"
        },
        "layout": {
            "grid_system": "12-column",
            "breakpoints": {
                "mobile": "320px",
                "tablet": "768px", 
                "desktop": "1024px",
                "wide": "1440px"
            },
            "alignment": "center"
        }
    }
    
    # Section configuration
    SECTION_CONFIG = {
        "hero": {
            "required_fields": ["headline", "cta_primary"],
            "optional_fields": ["subheadline", "cta_secondary", "background_image"]
        },
        "footer": {
            "required_fields": ["company_info"],
            "optional_fields": ["navigation_links", "social_media", "newsletter"]
        },
        "cta": {
            "required_fields": ["headline", "primary_button"],
            "optional_fields": ["subheadline", "secondary_button", "trust_indicators"]
        },
        "features": {
            "required_fields": ["heading", "features"],
            "optional_fields": ["subheading", "description"]
        }
    }
    
    # Output formats
    OUTPUT_FORMATS = {
        "html": {
            "enabled": True,
            "template_engine": "jinja2"
        },
        "css": {
            "enabled": True,
            "preprocessor": "none"  # Could be 'sass', 'less', etc.
        },
        "json": {
            "enabled": True,
            "pretty_print": True
        }
    }
    
    # Logging configuration
    LOGGING_CONFIG = {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file": "ocs.log"
    }
    
    @classmethod
    def get_gemini_config(cls) -> Dict[str, Any]:
        """Get Gemini AI configuration."""
        return {
            "api_key": cls.GEMINI_API_KEY,
            "model": cls.GEMINI_MODEL
        }
    
    @classmethod
    def get_section_config(cls, section_type: str) -> Dict[str, Any]:
        """Get configuration for a specific section type."""
        return cls.SECTION_CONFIG.get(section_type, {})
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that required configuration is present."""
        if not cls.GEMINI_API_KEY:
            print("Warning: GEMINI_API_KEY not set. AI features will not work.")
            return False
        return True


# Environment-specific configurations
class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True
    GEMINI_MODEL = "gemini-pro"  # Use standard model for development


class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False
    LOGGING_CONFIG = {
        "level": "WARNING",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file": "ocs_production.log"
    }


# Default configuration
config = DevelopmentConfig()