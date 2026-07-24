import os
import json
from openai import OpenAI
from geoplan_bench.config.prompts import KEY_STEPS_EXTRACTION_PROMPT, KEY_TOOLS_EXTRACTION_PROMPT



class CorrectnessEvaluator:
    def __init__(self, model="gpt-4o-mini"):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )
        self.model = model

    def generate_key_steps(self, question, ground_truth_tool_flow):
        """generate key steps from ground truth tool flow"""
        prompt = KEY_STEPS_EXTRACTION_PROMPT.format(
            question=question,
            ground_truth_tool_flow=ground_truth_tool_flow
        )
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        try:
            response_content = response.choices[0].message.content.strip()
            
            # try to extract JSON part
            if "```json" in response_content:
                json_start = response_content.find("```json") + 7
                json_end = response_content.find("```", json_start)
                response_content = response_content[json_start:json_end].strip()
            elif "```" in response_content:
                json_start = response_content.find("```") + 3
                json_end = response_content.find("```", json_start)
                response_content = response_content[json_start:json_end].strip()
            
            key_steps_data = json.loads(response_content)
            key_steps = key_steps_data.get("key_steps", [])
            
        except (json.JSONDecodeError, KeyError, AttributeError) as e:
            print(f"Key step parsing failed: {e}")
            print(f"LLM response content: {response.choices[0].message.content[:200]}...")
            # use gold path prefix 70% as key steps
            key_steps = ground_truth_tool_flow[:max(1, int(len(ground_truth_tool_flow) * 0.7))]
        
        return key_steps
    
    def generate_key_tools(self, question, agent_tool_flow):
        """generate key steps from agent's tool flow"""
        prompt = KEY_TOOLS_EXTRACTION_PROMPT.format(
            question=question,
            agent_tool_flow=agent_tool_flow
        )
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        try:
            response_content = response.choices[0].message.content.strip()
            
            # try to extract JSON part
            if "```json" in response_content:
                json_start = response_content.find("```json") + 7
                json_end = response_content.find("```", json_start)
                response_content = response_content[json_start:json_end].strip()
            elif "```" in response_content:
                json_start = response_content.find("```") + 3
                json_end = response_content.find("```", json_start)
                response_content = response_content[json_start:json_end].strip()
            
            key_tools_data = json.loads(response_content)
            key_tools = key_tools_data.get("key_tools", [])
            
        except (json.JSONDecodeError, KeyError, AttributeError) as e:
            print(f"Key tool parsing failed: {e}")
            print(f"LLM response content: {response.choices[0].message.content[:200]}...")
            # use gold path prefix 70% as key tools
            key_tools = agent_tool_flow[:max(1, int(len(agent_tool_flow) * 0.7))]
        
        return key_tools
    
    def compute_correctness_score(self, question, ground_truth_tool_flow, agent_tool_flow):
        """evaluate correctness of the agent's tool flow"""
        key_steps = self.generate_key_steps(question, ground_truth_tool_flow)
        key_tools = self.generate_key_tools(question, agent_tool_flow)
        key_step_recall = len(set(key_steps) & set(agent_tool_flow)) / len(key_steps)
        key_tool_precision = len(set(key_tools) & set(ground_truth_tool_flow)) / len(key_tools)
        F1_score = 2 * (key_tool_precision * key_step_recall) / (key_tool_precision + key_step_recall)
        return key_steps, key_tools, key_step_recall, key_tool_precision, F1_score
