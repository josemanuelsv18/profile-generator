from generator import Generator
from models.Answer import Answer
import random
from datetime import datetime

class AnswerGenerator(Generator):
    def __init__(self):
        super().__init__()
        self.answer_ids_dict = {
            1: [2, 3, 4, 5, 6],
            2: [7, 8, 9, 10, 11],
            3: [12, 13, 14, 15, 16],
            6: [17, 18, 19, 20, 21],
            7: [22, 23, 24, 25, 26],
            8: [27, 28, 29, 30],
            9: [31, 32, 33],
            10: [34, 35, 36, 37, 38],
            11: [39, 40, 41, 42],
            12: [43, 44, 45, 46],
            13: [47, 48, 49, 50],
            14: [51, 52, 53],
            15: [54, 55, 56],
            16: [57, 58, 59, 60],
            17: [61, 62, 63, 64],
            18: [65, 66, 67],
            19: [68, 69, 70, 71],
            20: [72, 73, 74, 75]
        }
        self.answer_probability_dict = {
            1: [0.05, 0.15, 0.35, 0.30, 0.15],
            2: [0.25, 0.30, 0.25, 0.15, 0.05],
            3: [0.08, 0.25, 0.55, 0.10, 0.02],
            6: [0.15, 0.20, 0.35, 0.20, 0.10],
            7: [0.20, 0.25, 0.30, 0.15, 0.10],
            8: [0.18, 0.32, 0.35, 0.15],
            9: [0.20, 0.35, 0.45],
            10: [0.12, 0.20, 0.28, 0.25, 0.15],
            11: [0.10, 0.30, 0.40, 0.20],
            12: [0.15, 0.35, 0.35, 0.15],
            13: [0.12, 0.28, 0.40, 0.20],
            14: [0.15, 0.35, 0.50],
            15: [0.18, 0.40, 0.42],
            16: [0.08, 0.15, 0.35, 0.42],
            17: [0.12, 0.28, 0.40, 0.20],
            18: [0.10, 0.30, 0.60],
            19: [0.15, 0.30, 0.35, 0.20],
            20: [0.18, 0.32, 0.30, 0.20]
        }

    def random_answer(self, answer_ids, probabilities):
        if len(answer_ids) != len(probabilities):
            raise ValueError("Las listas de ids y probabilidades deben tener el mismo tamaño")
        if not all(0 <= p <= 1 for p in probabilities):
            raise ValueError("Las probabilidades deben estar entre 0 y 1")
        if abs(sum(probabilities) - 1.0) > 1e-9:
            raise ValueError("Las probabilidades deben sumar 1")
        answer = random.choices(answer_ids, weights=probabilities, k=1)[0]
        return answer

    
    def generate(self, user):
        answers = []
        for id_question in self.answer_ids_dict.keys():
            answer_ids = self.answer_ids_dict[id_question]
            probabilities = self.answer_probability_dict[id_question]
            answer_ids = self.random_answer(answer_ids, probabilities)
            answer_obj = Answer(id_question, answer_ids, user, user, datetime.now())
            answers.append(answer_obj)
        return answers