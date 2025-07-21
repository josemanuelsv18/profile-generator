from pydantic import BaseModel
from datetime import datetime

class Answer(BaseModel):
    question_id: int
    answer_id: int
    profile_id_response: str
    profile_id_patient: str
    created_at: datetime

    def __init__(
            self,
            question_id: int,
            answer_id: int,
            profile_id_response: str,
            profile_id_patient: str,
            created_at: datetime
            ):
        self.question_id = question_id
        self.answer_id = answer_id
        self.profile_id_response = profile_id_response
        self.profile_id_patient = profile_id_patient
        self.created_at = created_at

    # Getters and Setters
    def get_question_id(self):
        return self.question_id
    def set_question_id(self, question_id: int):
        self.question_id = question_id
    def get_answer_id(self):
        return self.answer_id
    def set_answer_id(self, answer_id: int):
        self.answer_id = answer_id
    def get_profile_id_response(self):
        return self.profile_id_response
    def set_profile_id_response(self, profile_id_response: str):
        self.profile_id_response = profile_id_response
    def get_profile_id_patient(self):
        return self.profile_id_patient
    def set_profile_id_patient(self, profile_id_patient: str):
        self.profile_id_patient = profile_id_patient
    def get_created_at(self):
        return self.created_at
    def set_created_at(self, created_at: datetime):
        self.created_at = created_at
     