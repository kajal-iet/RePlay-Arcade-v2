from google.adk import Agent


def create_game_guide_agent(context: str):
    agent = Agent(
        model="gemini-1.5-pro",
        system_instruction=f"""
You are GameGuide, an expert AI mentor for this game.

You have access to the full game code and documentation below.
Answer clearly and practically.
Suggest code changes but never execute or modify production code.

GAME CONTEXT:
{context}
"""
    )
    return agent
