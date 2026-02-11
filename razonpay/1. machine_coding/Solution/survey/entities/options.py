"""
    A options within a question under a survey
"""
from interface.option_id_generator import OptionIdGenerator

class Options:
    def __init__(self, content: str, score: float) -> None:
        # store id as a string to keep consistency with Survey and Questions ids
        self.id: str = OptionIdGenerator().generate_id()
        self.content: str = content
        self.score: float = score
        