# models/Profile.py
from User import User
from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr


# Profile model that extends User
class Profile(User, BaseModel):
    nombre: str
    user_role: str
    def __init__(
            self,
            nombre: str,
            user_role: str,
            id: int,
            aud: str,
            role: str,
            email: EmailStr,
            encrypted_password: str,
            created_at: datetime,
            instance_id: int = '00000000-0000-0000-0000-000000000000',
            is_super_admin: bool = False,
            is_active: bool = True,
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
    def set_nombre(self, nombre: str):
        self.nombre = nombre
    def get_user_role(self):
        return self.user_role
    def set_user_role(self, user_role: str):
        self.user_role = user_role
