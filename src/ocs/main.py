"""
OCS (Orchestration Control System) - Main Entry Point

This module manages the overall flow of the AI landing page builder.
It handles user input prompts and delivers the final output.
"""

from typing import Dict, Any, Optional
import logging

# Import all agents
from ..agents.layout import LayoutAgent
from ..agents.taste import TasteAgent, TasteCritic
from ..agents.landing_page import LandingPageAgent


class OCS:
    """
    Main orchestrator for the AI Landing Page Builder system.
    
    Coordinates between Layout Agent, Taste Agent, Taste Critic, 
    and Landing Page Agent to create high-quality landing pages.
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Initialize all agents
        self.layout_agent = LayoutAgent()
        self.taste_agent = TasteAgent()
        self.taste_critic = TasteCritic()
        self.landing_page_agent = LandingPageAgent()
        
        self.logger.info("OCS system initialized with all agents")
    
    def process_user_prompt(self, user_prompt: str) -> Dict[str, Any]:
        """
        Main entry point for processing user prompts.
        
        Args:
            user_prompt (str): The user's description of the desired landing page
            
        Returns:
            Dict[str, Any]: The final landing page output
        """
        self.logger.info("Starting OCS processing for user prompt")
        
        try:
            # refine the prompt

            
            # Step 1: Get layout structure from Layout Agent
            self.logger.info("Step 1: Analyzing layout structure...")
            layout_structure = self.layout_agent.analyze_prompt(user_prompt)
            
            # Step 2: Get taste configuration from Taste Agent
            self.logger.info("Step 2: Creating taste configuration...")
            taste_config = self.taste_agent.create_taste_config(user_prompt)
            
            # Step 3: Validate taste configuration with Taste Critic
            self.logger.info("Step 3: Validating taste configuration...")
            critique = self.taste_critic.critique_with_feedback(taste_config, user_prompt)
            
            # Step 4: Improve taste config if needed (up to 3 iterations)
            iteration_count = 0
            max_iterations = 3
            
            while not critique["acceptable"] and iteration_count < max_iterations:
                self.logger.info(f"Step 4: Improving taste config (iteration {iteration_count + 1})...")
                
                # Create improved config based on critique
                improved_context = {
                    "previous_critique": critique,
                    "improvement_suggestions": critique["suggestions"]
                }
                
                taste_config = self.taste_agent.create_taste_config(user_prompt, improved_context)
                critique = self.taste_critic.critique_with_feedback(taste_config, user_prompt)
                iteration_count += 1
            
            # Step 5: Generate final landing page
            self.logger.info("Step 5: Creating final landing page...")
            landing_page = self.landing_page_agent.create_landing_page(layout_structure, taste_config)
            
            # Add processing metadata
            landing_page["processing_info"] = {
                "user_prompt": user_prompt,
                "iterations_used": iteration_count,
                "taste_quality_score": critique["quality_score"],
                "final_acceptable": critique["acceptable"],
                "processing_status": "success"
            }
            
            self.logger.info("OCS processing completed successfully")
            return landing_page
            
        except Exception as e:
            self.logger.error(f"OCS processing failed: {e}")
            return {
                "status": "error",
                "message": f"Processing failed: {str(e)}",
                "user_prompt": user_prompt,
                "processing_info": {
                    "processing_status": "failed",
                    "error": str(e)
                }
            }
