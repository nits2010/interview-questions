from collections import defaultdict
from typing import Dict, Set
import uuid
import threading



from interface.sruvey_id_generator import SurveyIdGenerator
from entities.survey_response import SurveyResponse
from entities.questions import Questions
class Survey:
    MAX_QUESTION  = 100 # get from config
    
    def __init__(self, survey_title: str) -> None:
        self.id: str = SurveyIdGenerator().generate_id()
        self.survey_title: str = survey_title 
            
        self.question : Dict[str, Questions]= {}
        self.response : Dict[str, SurveyResponse] = {}
        self.shared_users : Set[str] = set()
        
        # ratings
        self.survey_rating = 0.0
        self.survey_count = 0
        
        self.question_score_sum = defaultdict(float)
        self.question_response_count = defaultdict(int)
        
        self.lock = threading.Lock()
    
    def add_question(self, question: Questions) -> None:
        if len(self.question) == self.MAX_QUESTION:
            raise ValueError("Max question limit exceeded")

        self.question[question.id] = question
    
    def remove_question(self, question_id: str) -> None:
        if question_id not in self.question:
            raise ValueError(f"Question id {question_id} does not exisits in survey id ={self.id}")
        del self.question[question_id]
    
    def share_with_users(self, user_id: str) -> None:
        self.shared_users.add(user_id)
    
    def is_user_allowed(self, user_id: str) -> bool:
        return user_id in self.shared_users

            
    