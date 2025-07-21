class Answer():
    def __init__(
            self,
            question_id,
            answer_id,
            profile_id_response,
            profile_id_patient,
            created_at
            ):
        self.question_id = question_id
        self.answer_id = answer_id
        self.profile_id_response = profile_id_response
        self.profile_id_patient = profile_id_patient
        self.created_at = created_at

    # Getters and Setters
    def get_question_id(self):
        return self.question_id
    def set_question_id(self, question_id):
        self.question_id = question_id
    def get_answer_id(self):
        return self.answer_id
    def set_answer_id(self, answer_id):
        self.answer_id = answer_id
    def get_profile_id_response(self):
        return self.profile_id_response
    def set_profile_id_response(self, profile_id_response):
        self.profile_id_response = profile_id_response
    def get_profile_id_patient(self):
        return self.profile_id_patient
    def set_profile_id_patient(self, profile_id_patient):
        self.profile_id_patient = profile_id_patient
    def get_created_at(self):
        return self.created_at
    def set_created_at(self, created_at):
        self.created_at = created_at
     