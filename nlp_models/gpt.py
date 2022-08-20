import openai


def set_openai_key(key):
    openai.api_key = key


class Example:
    def __init__(self, inp, out):
        self.input = inp
        self.output = out

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def format(self):
        return f"input: {self.input}\noutput: {self.output}\n"
