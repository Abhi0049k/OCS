"""
Quick test for React component generation.
"""

from src.ocs import OCS
import json

def test_react_output():
    """Test React component generation."""
    
    print("🚀 Testing React Component Generation")
    print("=" * 50)
    
    ocs = OCS()
    
    prompt = "Create a modern landing page for a tech startup selling AI tools"
    print(f"Prompt: {prompt}")
    
    result = ocs.process_user_prompt(prompt)
    
    if "react_components" in result:
        print("\n✅ React Components Generated:")
        components = result["react_components"]
        
        for name in components.keys():
            print(f"  📄 {name}")
        
        print(f"\n📋 Sample Hero Component Preview:")
        hero_component = components.get("HeroSection", "")
        print(hero_component[:300] + "..." if len(hero_component) > 300 else hero_component)
        
        print(f"\n🎨 Theme Configuration:")
        styles = result.get("component_styles", {})
        if "theme_config" in styles:
            theme_preview = styles["theme_config"][:200] + "..."
            print(theme_preview)
    
    else:
        print("❌ No React components found in output")

if __name__ == "__main__":
    test_react_output()