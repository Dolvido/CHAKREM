
from CentralSystem import CentralSystem
from ChakraAgent import ChakraAgent
from RootChakraAgent import RootChakraAgent
from SystemState import SystemState

central_system = CentralSystem()
root_chakra_function = """
The Root Chakra, also known as Muladhara, is the first chakra in the human energy system. It is located at the base of the spine and is associated with the color red. The Root Chakra represents our foundation and connection to the physical world. Its primary functions include:

1. Grounding: The Root Chakra helps us stay grounded and connected to the Earth. It provides a sense of stability and security in our lives.

2. Survival Instinct: This chakra is responsible for our basic survival needs, including food, shelter, and safety. It governs our fight-or-flight response.

3. Physical Health: The Root Chakra influences our overall physical health and vitality. When it's balanced, it supports a strong immune system and a healthy body.

4. Rootedness: It fosters a sense of belonging and connection to our family, community, and the world around us.

5. Material Abundance: The Root Chakra is associated with our ability to manifest material abundance and prosperity in our lives.

6. Emotional Balance: It plays a role in emotional stability and helps us manage fear, anxiety, and insecurity.

7. Self-Confidence: A balanced Root Chakra contributes to a strong sense of self and self-confidence.

Balancing and aligning the Root Chakra is essential for a stable and harmonious life. Practices such as meditation, yoga, grounding exercises, and focusing on the color red can help restore balance to this chakra.
"""

root_chakra_agent = RootChakraAgent(chakra_name="Root Chakra", chakra_function=root_chakra_function)
central_system.register_agent('RootChakraAgent', root_chakra_agent)
# Create initial system state
system_state = SystemState()

# Main simulation loop
while True:
    # Get user input
    user_input = input("You: ")
    
    # Update the system state with the new user input
    system_state.update_user_input(user_input)
    
    # Send the updated system state to the agents for analysis
    responses = {}
    for agent_name, agent in central_system.agents.items():
        responses[agent_name] = agent.analyze_system_state(system_state)
    
    # Insert the current system state into the database
    system_state.insert_system_state()
    
    # Print the responses from the agents
    for agent_name, agent_response in responses.items():
        print(f"{agent_name}: {agent_response}")
