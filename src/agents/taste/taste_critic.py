"""
Taste Critic Agent

Judges taste configurations created by the Taste Agent.
Can loop back to Taste Agent up to 3 times for improvements.
"""

from typing import Dict, Any, List, Tuple
import logging


class TasteCritic:
    """
    Agent responsible for critiquing and validating taste configurations.
    
    Evaluates taste configs against good design principles and reference designs.
    Can request improvements from Taste Agent if quality is insufficient.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.max_iterations = 3
        
        # Design principles for evaluation
        self.design_principles = {
            "contrast": "Ensure sufficient color contrast for accessibility",
            "consistency": "Maintain consistent styling throughout", 
            "hierarchy": "Clear visual hierarchy with proper typography",
            "whitespace": "Appropriate use of whitespace and spacing",
            "readability": "Text must be easily readable",
            "modern_appeal": "Design should feel contemporary and fresh"
        }
    
    def evaluate_config(self, taste_config: Dict[str, Any], user_prompt: str) -> Tuple[bool, List[str], float]:
        """
        Evaluate a taste configuration for quality and appropriateness.
        
        Args:
            taste_config (Dict[str, Any]): Configuration to evaluate
            user_prompt (str): Original user prompt for context
            
        Returns:
            Tuple[bool, List[str], float]: (is_acceptable, issues_found, quality_score)
        """
        self.logger.info("Taste Critic evaluating configuration")
        
        issues = []
        quality_score = 0.0
        
        # TODO: Implement sophisticated AI-based evaluation
        # For now, use basic rule-based evaluation
        
        # Check color contrast
        if self._check_contrast(taste_config.get("color_scheme", {})):
            quality_score += 0.2
        else:
            issues.append("Insufficient color contrast detected")
        
        # Check typography consistency
        if self._check_typography(taste_config.get("typography", {})):
            quality_score += 0.2
        else:
            issues.append("Typography lacks consistency")
        
        # Check spacing appropriateness
        if self._check_spacing(taste_config.get("spacing", {})):
            quality_score += 0.2
        else:
            issues.append("Spacing values need adjustment")
        
        # Check style coherence
        if self._check_style_coherence(taste_config.get("style", {})):
            quality_score += 0.2
        else:
            issues.append("Style elements lack coherence")
        
        # Check prompt alignment
        if self._check_prompt_alignment(taste_config, user_prompt):
            quality_score += 0.2
        else:
            issues.append("Configuration doesn't align well with user prompt")
        
        # Configuration is acceptable if score > 0.7 and no critical issues
        is_acceptable = quality_score >= 0.7 and len(issues) < 2
        
        return is_acceptable, issues, quality_score
    
    def critique_with_feedback(self, taste_config: Dict[str, Any], user_prompt: str) -> Dict[str, Any]:
        """
        Provide detailed critique with improvement suggestions.
        
        Args:
            taste_config (Dict[str, Any]): Configuration to critique
            user_prompt (str): Original user prompt
            
        Returns:
            Dict[str, Any]: Detailed critique with suggestions
        """
        is_acceptable, issues, score = self.evaluate_config(taste_config, user_prompt)
        
        critique = {
            "acceptable": is_acceptable,
            "quality_score": score,
            "issues": issues,
            "suggestions": self._generate_suggestions(issues, user_prompt),
            "overall_feedback": self._generate_overall_feedback(score, issues)
        }
        
        return critique
    
    def _check_contrast(self, color_scheme: Dict[str, str]) -> bool:
        """Check if color scheme has sufficient contrast."""
        # Simplified contrast check - in real implementation, use proper color contrast algorithms
        return True  # Placeholder
    
    def _check_typography(self, typography: Dict[str, str]) -> bool:
        """Check typography consistency."""
        # Check if fonts and weights are appropriately chosen
        return typography.get("heading_font") and typography.get("body_font")
    
    def _check_spacing(self, spacing: Dict[str, str]) -> bool:
        """Check spacing appropriateness."""
        # Verify spacing values are reasonable
        return spacing.get("section_padding") and spacing.get("element_spacing")
    
    def _check_style_coherence(self, style: Dict[str, str]) -> bool:
        """Check if style elements work well together."""
        return style.get("overall_aesthetic") and style.get("corner_radius")
    
    def _check_prompt_alignment(self, config: Dict[str, Any], prompt: str) -> bool:
        """Check if configuration aligns with user prompt."""
        # Simple keyword matching - will be enhanced with AI
        prompt_lower = prompt.lower()
        
        if "modern" in prompt_lower and config.get("style", {}).get("overall_aesthetic") == "modern":
            return True
        
        return True  # Placeholder for now
    
    def _generate_suggestions(self, issues: List[str], prompt: str) -> List[str]:
        """Generate improvement suggestions based on issues."""
        suggestions = []
        
        for issue in issues:
            if "contrast" in issue:
                suggestions.append("Increase color contrast between text and background")
            elif "typography" in issue:
                suggestions.append("Choose more consistent font pairings")
            elif "spacing" in issue:
                suggestions.append("Adjust spacing for better visual rhythm")
            elif "coherence" in issue:
                suggestions.append("Ensure all style elements complement each other")
            elif "prompt" in issue:
                suggestions.append("Better align design choices with user requirements")
        
        return suggestions
    
    def _generate_overall_feedback(self, score: float, issues: List[str]) -> str:
        """Generate overall feedback message."""
        if score >= 0.8:
            return "Excellent taste configuration with minor room for improvement"
        elif score >= 0.6:
            return "Good configuration but needs some refinements"
        else:
            return "Configuration needs significant improvements"


def main():
    """Test the Taste Critic."""
    critic = TasteCritic()
    
    # Mock taste config for testing
    test_config = {
        "color_scheme": {
            "primary_color": "#1a1a1a",
            "secondary_color": "#ffffff",
            "accent_color": "#007acc"
        },
        "typography": {
            "heading_font": "Inter",
            "body_font": "Inter"
        },
        "spacing": {
            "section_padding": "large",
            "element_spacing": "medium"
        },
        "style": {
            "overall_aesthetic": "modern",
            "corner_radius": "small"
        }
    }
    
    test_prompt = "Create a modern tech startup landing page"
    
    critique = critic.critique_with_feedback(test_config, test_prompt)
    print("Critique Result:")
    print(f"Acceptable: {critique['acceptable']}")
    print(f"Score: {critique['quality_score']}")
    print(f"Issues: {critique['issues']}")
    print(f"Suggestions: {critique['suggestions']}")


if __name__ == "__main__":
    main()