class ConversationMemory:
    def __init__(self, max_messages=10):
        self.max_messages = max_messages
        self.messages = []

    def add_user_message(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })
        self._trim_memory()

    def add_ai_message(self, message):
        self.messages.append({
            "role": "assistant",
            "content": message
        })
        self._trim_memory()

    def get_history(self):
        history = ""

        for msg in self.messages:
            history += f"{msg['role'].capitalize()}: {msg['content']}\n"

        return history

    def clear(self):
        self.messages = []

    def _trim_memory(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]