class LLM:
    def __init__(self, function, name, model_name, capabilities):
        self.function = function
        self.name = name
        self.model_name = model_name
        self.capabilities = capabilities

    def __repr__(self):
        return f"LLM(name={self.name}, model_name={self.model_name})"