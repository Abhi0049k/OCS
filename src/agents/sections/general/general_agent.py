"""
General Section Agent

Handles creation of any new or custom section types not covered
by specialized agents.
"""

from typing import Dict, Any, List
import logging


class GeneralAgent:
    """
    Agent for handling custom and general section types.
    
    This agent can create any type of section that doesn't have
    a specialized agent, making the system flexible and extensible.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Common section templates
        self.section_templates = {
            "features": self._create_features_section,
            "testimonials": self._create_testimonials_section,
            "pricing": self._create_pricing_section,
            "about": self._create_about_section,
            "team": self._create_team_section,
            "contact": self._create_contact_section,
            "faq": self._create_faq_section,
            "portfolio": self._create_portfolio_section,
            "services": self._create_services_section,
            "stats": self._create_stats_section
        }
    
    def create_section(self, section_type: str, taste_config: Dict[str, Any], 
                      context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a section of the specified type.
        
        Args:
            section_type (str): Type of section to create
            taste_config (Dict[str, Any]): UI taste configuration
            context (Dict[str, Any]): Additional context and requirements
            
        Returns:
            Dict[str, Any]: Section content and styling
        """
        self.logger.info(f"General Agent creating {section_type} section")
        
        # Check if we have a template for this section type
        if section_type in self.section_templates:
            return self.section_templates[section_type](taste_config, context)
        else:
            return self._create_custom_section(section_type, taste_config, context)
    
    def _create_features_section(self, taste_config: Dict[str, Any], 
                                context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a features section."""
        return {
            "type": "features",
            "heading": "Powerful Features",
            "subheading": "Everything you need to succeed",
            "features": [
                {
                    "icon": "⚡",
                    "title": "Lightning Fast",
                    "description": "Experience blazing fast performance with our optimized infrastructure."
                },
                {
                    "icon": "🔒",
                    "title": "Secure & Reliable",
                    "description": "Enterprise-grade security with 99.9% uptime guarantee."
                },
                {
                    "icon": "📊",
                    "title": "Analytics & Insights",
                    "description": "Detailed analytics to help you make data-driven decisions."
                },
                {
                    "icon": "🤝",
                    "title": "24/7 Support",
                    "description": "Round-the-clock support from our dedicated team."
                }
            ],
            "layout": "grid",
            "columns": 2
        }
    
    def _create_testimonials_section(self, taste_config: Dict[str, Any], 
                                   context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a testimonials section."""
        return {
            "type": "testimonials",
            "heading": "What Our Customers Say",
            "testimonials": [
                {
                    "quote": "This product completely transformed how we handle our workflows.",
                    "author": "Sarah Johnson",
                    "position": "CEO, TechCorp",
                    "avatar": "https://via.placeholder.com/64"
                },
                {
                    "quote": "Incredible results in just the first month of using this platform.",
                    "author": "Mike Chen",
                    "position": "CTO, InnovateLabs", 
                    "avatar": "https://via.placeholder.com/64"
                }
            ],
            "layout": "carousel"
        }
    
    def _create_pricing_section(self, taste_config: Dict[str, Any], 
                               context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a pricing section."""
        return {
            "type": "pricing",
            "heading": "Choose Your Plan",
            "subheading": "Flexible pricing for teams of all sizes",
            "plans": [
                {
                    "name": "Starter",
                    "price": "$9",
                    "period": "month",
                    "features": ["Up to 5 users", "Basic features", "Email support"],
                    "cta": "Start Free Trial"
                },
                {
                    "name": "Professional", 
                    "price": "$29",
                    "period": "month",
                    "features": ["Up to 25 users", "Advanced features", "Priority support"],
                    "cta": "Get Started",
                    "highlighted": True
                },
                {
                    "name": "Enterprise",
                    "price": "Custom",
                    "period": "",
                    "features": ["Unlimited users", "Custom integrations", "Dedicated support"],
                    "cta": "Contact Sales"
                }
            ],
            "layout": "cards"
        }
    
    def _create_about_section(self, taste_config: Dict[str, Any], 
                             context: Dict[str, Any]) -> Dict[str, Any]:
        """Create an about section."""
        return {
            "type": "about",
            "heading": "About Our Company",
            "description": "We're on a mission to empower businesses with cutting-edge AI technology that drives real results.",
            "image": "https://via.placeholder.com/600x400",
            "stats": [
                {"number": "10K+", "label": "Happy Customers"},
                {"number": "99.9%", "label": "Uptime"},
                {"number": "24/7", "label": "Support"}
            ],
            "layout": "split"
        }
    
    def _create_team_section(self, taste_config: Dict[str, Any], 
                            context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a team section."""
        return {
            "type": "team",
            "heading": "Meet Our Team",
            "members": [
                {
                    "name": "Alex Smith",
                    "position": "CEO & Founder",
                    "bio": "Visionary leader with 15+ years in AI and technology.",
                    "image": "https://via.placeholder.com/200",
                    "social": {"linkedin": "#", "twitter": "#"}
                }
            ],
            "layout": "grid"
        }
    
    def _create_contact_section(self, taste_config: Dict[str, Any], 
                               context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a contact section."""
        return {
            "type": "contact",
            "heading": "Get In Touch",
            "description": "Have questions? We'd love to hear from you.",
            "form_fields": ["name", "email", "company", "message"],
            "contact_info": {
                "email": "hello@company.com",
                "phone": "+1 (555) 123-4567"
            },
            "layout": "form_with_info"
        }
    
    def _create_faq_section(self, taste_config: Dict[str, Any], 
                           context: Dict[str, Any]) -> Dict[str, Any]:
        """Create an FAQ section."""
        return {
            "type": "faq",
            "heading": "Frequently Asked Questions",
            "questions": [
                {
                    "question": "How does the free trial work?",
                    "answer": "Start with a 14-day free trial with full access to all features."
                },
                {
                    "question": "Can I cancel anytime?",
                    "answer": "Yes, you can cancel your subscription at any time with no penalties."
                }
            ],
            "layout": "accordion"
        }
    
    def _create_portfolio_section(self, taste_config: Dict[str, Any], 
                                 context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a portfolio section."""
        return {
            "type": "portfolio",
            "heading": "Our Work",
            "projects": [
                {
                    "title": "Project Alpha",
                    "description": "Revolutionary AI solution for enterprise clients.",
                    "image": "https://via.placeholder.com/400x300",
                    "link": "#"
                }
            ],
            "layout": "masonry"
        }
    
    def _create_services_section(self, taste_config: Dict[str, Any], 
                                context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a services section."""
        return {
            "type": "services",
            "heading": "Our Services",
            "services": [
                {
                    "title": "AI Consulting",
                    "description": "Expert guidance on AI implementation.",
                    "icon": "🤖"
                },
                {
                    "title": "Custom Development",
                    "description": "Tailored AI solutions for your business.",
                    "icon": "⚙️"
                }
            ],
            "layout": "cards"
        }
    
    def _create_stats_section(self, taste_config: Dict[str, Any], 
                             context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a statistics section."""
        return {
            "type": "stats",
            "heading": "By the Numbers",
            "stats": [
                {"number": "1M+", "label": "Users Worldwide"},
                {"number": "99.9%", "label": "Uptime"},
                {"number": "150+", "label": "Countries Served"},
                {"number": "24/7", "label": "Support Available"}
            ],
            "layout": "horizontal"
        }
    
    def _create_custom_section(self, section_type: str, taste_config: Dict[str, Any], 
                              context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a custom section type using AI."""
        # TODO: Implement Gemini model integration for custom section creation
        
        return {
            "type": section_type,
            "heading": f"Custom {section_type.title()} Section",
            "description": f"This is a dynamically generated {section_type} section.",
            "content": "Custom content will be generated here based on AI analysis.",
            "layout": "default"
        }


def main():
    """Test the General Agent."""
    agent = GeneralAgent()
    
    test_taste = {
        "color_scheme": {
            "primary_color": "#1a1a1a"
        }
    }
    
    # Test different section types
    features = agent.create_section("features", test_taste, {})
    print("Features Section:")
    print(f"Heading: {features['heading']}")
    print(f"Features count: {len(features['features'])}")
    
    pricing = agent.create_section("pricing", test_taste, {})
    print("\nPricing Section:")
    print(f"Heading: {pricing['heading']}")
    print(f"Plans count: {len(pricing['plans'])}")


if __name__ == "__main__":
    main()