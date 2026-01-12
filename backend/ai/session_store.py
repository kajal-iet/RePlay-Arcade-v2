from collections import defaultdict

class SessionStore:
    def __init__(self):
        self.sessions = defaultdict(list)

    def add(self, session_id, role, text):
        self.sessions[session_id].append({"role": role, "text": text})

    def get(self, session_id):
        return self.sessions[session_id]

store = SessionStore()
