from typing import Dict


class SurveyResponse :
    
    def __init__(self, user_id: str, answers : Dict[str,str], rating:float):
        self.user_id: str = user_id
        self.answers: Dict[str,str] = answers
        self.rating: float = rating
        