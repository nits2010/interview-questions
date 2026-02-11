"""Service layer for managing surveys, questions, options and ratings."""

from typing import Dict

from entities.options import Options
from entities.questions import Questions
from entities.survey import Survey
from entities.survey_response import SurveyResponse


class RatingService:
    
    def __init__ (self):
        # Maps survey_id -> Survey instance
        self.surveys : Dict[str, Survey] = {}
    
    # ---- admin operations ----
    def create_survey(self, title: str) -> str:
        """Create a new survey and return its id."""
        survey: Survey = Survey(title)
        self.surveys[survey.id] = survey
        return survey.id

    def add_questions(self, survey_id: str, question_content: str) -> str:
        """Add a question to a survey and return the question id."""
        if survey_id not in self.surveys:
            raise ValueError(f"Survey id = {survey_id} does not exist in the system")
        
        quesiton = Questions(question_content)
        survey: Survey  = self.surveys[survey_id]
        survey.add_question(question=quesiton)
        return quesiton.id
        
    def add_option(
        self, survey_id: str, question_id: str, content: str, score: float
    ) -> str:
        """Add an option to a question in a survey and return the option id."""
        if survey_id not in self.surveys:
            raise ValueError(f"Survey id = {survey_id} does not exist in the system")

        survey: Survey  = self.surveys[survey_id]
        if question_id not in survey.question:
            raise ValueError(
                f"question_id = {question_id} does not exist in the questions"
            )

        questions: Questions = survey.question[question_id]
        return questions.add_option(content, score)
        
    # delete questions ... 
    
    def share_survey(self, survey_id: str, user_id: str) -> None:
        """Allow a user to take a given survey."""
        if survey_id not in self.surveys:
            raise ValueError(f"Survey id = {survey_id} does not exist in the system")

        survey: Survey = self.surveys[survey_id]
        survey.share_with_users(user_id)
        
    
    
    def submit_survey(self, survey_id: str, answers:Dict[str,str], user_id: str) -> None:
        """Submit answers for a survey for a given user."""
        if survey_id not in self.surveys:
            raise ValueError(f"Survey id = {survey_id} does not exist in the system")
        survey: Survey = self.surveys[survey_id]
        
        # lock (could be used if multiple threads submit concurrently)
        if user_id in survey.response:
            raise ValueError(f"Multiple submission not allowed")

        total_score = 0.0
        for question_id, option_id in answers.items():
            questions = survey.question[question_id]
            option = questions.options[option_id]
            
            total_score += option.score
            
            survey.question_score_sum[question_id] += option.score
            survey.question_response_count[question_id] +=1 
            
        
        rating = total_score / len(answers)
        
        survey.survey_rating += rating  # aggregate survey rating
        survey.survey_count +=1 
        
        survey.response[user_id] = SurveyResponse(user_id, answers, rating)
    
    
    def get_survey_rating(self, survey_id: str) -> float:
        """Return the average rating for a survey."""
        survey: Survey = self.surveys[survey_id]
       
        if survey.survey_count == 0:
           return 0.0

        return survey.survey_rating / survey.survey_count

    def get_question_average_rating(self, survey_id: str, question_id: str) -> float:
        """Return the average rating for a single question."""
        survey: Survey = self.surveys[survey_id]
        count = survey.question_response_count[question_id]
        if count == 0:
            return 0.0
        return survey.question_score_sum[question_id] / count 
    

        
        #punit.mukherjee@razorpay.com
        
