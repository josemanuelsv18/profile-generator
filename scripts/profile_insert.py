from datetime import datetime
from insertor import Insertor

class ProfileInsert(Insertor):
    def __init__(self):
        super().__init__()
    
    def insert(self, conn, profile):
        # Query para insertar en auth.users
        user_query = """
        INSERT INTO auth.users (
            instance_id,
            id,
            aud,
            role,
            email,
            encrypted_password,
            created_at,
            is_super_admin,
            is_anonymous
        ) VALUES (
            %(instance_id)s,
            %(id)s,
            %(aud)s,
            %(role)s,
            %(email)s,
            %(encrypted_password)s,
            %(created_at)s,
            %(is_super_admin)s,
            %(is_anonymous)s
        )
        """
        
        # Query para insertar en public.profiles
        profile_query = """
        INSERT INTO public.profiles (
            id,
            nombre,
            role
        ) VALUES (
            %(id)s,
            %(nombre)s,
            %(role)s
        )
        """
        
        # Parámetros para auth.users
        user_params = {
            'instance_id': '00000000-0000-0000-0000-000000000000',
            'id': profile.get_id(),
            'aud': 'authenticated',
            'role': 'authenticated',
            'email': profile.get_email(),
            'encrypted_password': profile.get_encrypted_password(),
            'created_at': datetime.now(),
            'is_super_admin': False,
            'is_anonymous': False
        }
        # Parámetros para public.profiles
        profile_params = {
            'id': profile.get_id(),  # Mismo ID que el usuario
            'nombre': profile.get_nombre(),
            'role': 'patient'
        }
        
        try:
            with conn.get_cursor() as cursor:
                cursor.execute(user_query, user_params)
                cursor.execute(profile_query, profile_params)
            print("Usuario y perfil creados exitosamente")
            return True
        except Exception as e:
            print(f"Error al crear usuario y perfil: {e}")
            return False