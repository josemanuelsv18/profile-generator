# models/Profile.py
from .User import User

# Profile model that extends User
class Profile(User):
    def __init__(
            self,
            nombre,
            user_role,
            id,
            aud,
            role,
            email,
            encrypted_password,
            created_at,
            instance_id,
            is_super_admin,
            is_active,
            ):
        super().__init__(
                    id,
                    aud,
                    role,
                    email,
                    encrypted_password,
                    created_at,
                    instance_id,
                    is_super_admin,
                    is_active
                        )
        self.nombre = nombre
        self.user_role = user_role
    
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_user_role(self):
        return self.user_role
    def set_user_role(self, user_role):
        self.user_role = user_role
