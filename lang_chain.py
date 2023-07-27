class LangChain:
    def __init__(self, llms):
        self.llms = {llm.model_name: llm for llm in llms}

    async def process(self, prompt, model_name, user_id, session_id):
        chosen_llm = self.llms.get(model_name)
        if not chosen_llm:
            print(f"Model {model_name} not found.")
            return
        response = await chosen_llm.function(prompt)
        # Store the message and response in the database
        store_message(user_id, session_id, prompt, response)
        return response
