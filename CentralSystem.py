class CentralSystem:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):
        """Registers an agent with the central system."""
        self.agents[name] = agent

    def send_message(self, recipient_name, message):
        """Sends a message to a specific agent and gets a response."""
        if recipient_name in self.agents:
            response = self.agents[recipient_name].agent_executor.run(message)
            return response
        else:
            raise ValueError(f"No agent registered with the name: {recipient_name}")

    def broadcast_message(self, message):
        """Broadcasts a message to all registered agents and collects their responses."""
        responses = {}
        for name, agent in self.agents.items():
            responses[name] = agent.agent_executor.run(message)
        return responses

    def create_and_register_tool(self, agent_name, tool_code, tool_name):
        """Creates a new tool from Python code and registers it with the specified agent."""
        # Execute the Python code to define the new tool function
        exec(tool_code, globals())

        # Get the new tool function from the global namespace
        new_tool_func = globals()[tool_name]

        # Register the new tool with the specified agent
        self.agents[agent_name].create_tool(new_tool_func, tool_name)
