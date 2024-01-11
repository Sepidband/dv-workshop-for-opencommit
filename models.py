class Step:
    def __init__(self, label, content):
        self.label = label
        self.content = content

class Codelab:
    def __init__(self, title, steps):
        self.title = title
        self.steps = steps