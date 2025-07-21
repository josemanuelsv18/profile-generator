class Validator:
    @staticmethod
    def int_validator(n):
        if not isinstance(n, int):
            print("El valor debe ser de tipo entero")
            return False
        if n <= 0:
            print("El valor debe ser mayor a 0")
            return False
        if n > 1000:
            print("El numero maximo de perfiles a generar es 1000")
            return False
        return True