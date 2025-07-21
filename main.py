from validator import Validator
from generators import profile_generator, answer_generator
from scripts import profile_insertor, answer_insertor
from models import User, Answer
from database import connection

class Main:
    def __init__(self):
        self.valid = False
        self.profiles_num = 0
        self.profile = None
        self.answer = []
        self.validator = Validator.Validator()
        self.profile_gen =  profile_generator.ProfileGenerator()
        self.profile_insert = profile_insertor.ProfileInsertor()
        self.answer_gen = answer_generator.AnswerGenerator()
        self.answer_insert = answer_insertor.AnswerInsertor()

    def main(self):
        print('Generador de perfiles falsos, adaptado a la base datos de metodologia de investigación')
        print('Ingresa la cantidad de perfiles a generar')
        while not self.valid:
            profiles_num = input()
            profiles_num = int(profiles_num)
            self.valid = self.validator.int_validator(profiles_num)
        print(f'Generando {profiles_num} perfiles...')
        conn = connection.Connection()
        for i in range(profiles_num):
            self.profile = self.profile_gen.generate()
            self.answer = self.answer_gen.generate(self.profile)
            if conn.open_connection():
                self.profile_insert.insert(conn, self.profile)
                for answ in self.answer:
                    self.answer_insert.insert(conn, self.profile, answ)
            else:
                print("No se pudo abrir la conexion al servidor")
                break
        conn.close_connection()
        print(f"Se generaron e insertaron {i+1} perfiles en la base de datos")
        diff = profiles_num-(i+1)
        if diff > 0:
            print(f"no se pudieron crear los {profiles_num}, faltaron {diff} perfiles por crear")
                

if __name__ == "__main__":
    app = Main()
    app.main()