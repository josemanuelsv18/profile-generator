from .insertor import Insertor
from datetime import datetime

class AnswerInsertor(Insertor):
    def __init__(self):
        super().__init__()
    
    def insert(self, conn, profile, answer):
        answer_query = """ 
        INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
            "preguntaId",
            "respuestaId",
            "profileId_response",
            "profileId_paciente",
            CREATED_AT
        ) VALUES (
            %(preguntaId)s,
            %(respuestaId)s,
            %(profileId_response)s,
            %(profileId_paciente)s,
            %(CREATED_AT)s
        );
        """
        answer_params = {
            'preguntaId': answer.get_question_id(),
            'respuestaId': answer.get_answer_id(),
            'profileId_response': profile.get_id(),
            'profileId_paciente': profile.get_id(),
            'CREATED_AT': datetime.now()
        }

        try:
            with conn.get_cursor() as cursor:
                cursor.execute(answer_query, answer_params)
            print("Respuestas insertadas a la bd correctamente")
            return
        except Exception as e:
            print(f"Error al insertar las respuestas en la bd: {e}")
            return False