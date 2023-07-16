class LangChain:
    def __init__(self, llms):
        self.llms = {llm.model_name: llm for llm in llms}

    async def process(self, prompt, model_name):
        # At the start of the process method
        print(f"LLM names at start of process method: {self.llms.keys()}")
        chosen_llm = self.llms.get(model_name)
        if not chosen_llm:
            print(f"Model {model_name} not found.")
            return
        print(f"Sending prompt \"{prompt}\" to {model_name}")
        response = await chosen_llm.function(prompt)
        print(f"{model_name}: {response}")
