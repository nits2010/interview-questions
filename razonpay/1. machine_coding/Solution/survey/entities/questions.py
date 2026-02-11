"""
    A question within in a survey

"""


from typing import Dict
from interface.question_id_generator import QuestionIdGenerator
from entities.options import Options


class Questions:
    MAX_OPTION = 10  # get from config

    def __init__(self, content: str) -> None:
        # store id as a string to keep consistency with Survey ids
        self.id: str = QuestionIdGenerator().generate_id()
        self.content: str = content
        self.rating: float = -1
        self.options: Dict[str, Options] = {}
          
    def add_option(self, option_content: str, score: float) -> str:
        if len(self.options) == self.MAX_OPTION:
            raise ValueError("You can have max 10 options within a question")
         
        option = Options(option_content, score)
        self.options[option.id] = option
        return option.id
        
    def remove_option(self, option_id: str) -> str:
        if option_id not in self.options:
            return f"Option does not exists in {self.id}"

        del self.options[option_id]
    
    
        
        
    