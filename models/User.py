class User():
    def __init__(
            self,
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
        self.id = id
        self.aud = aud
        self.role = role
        self.email = email
        self.encrypted_password = encrypted_password
        self.created_at = created_at
        self.instance_id = instance_id
        self.is_super_admin = is_super_admin
        self.is_active = is_active
    

    #getters y setters
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_aud(self):
        return self.aud
    def set_aud(self, aud):
        self.aud = aud
    def get_role(self):
        return self.role
    def set_role(self, role):
        self.role = role
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_encrypted_password(self):
        return self.encrypted_password
    def set_encrypted_password(self, encrypted_password):
        self.encrypted_password = encrypted_password
    def get_created_at(self):
        return self.created_at
    def set_created_at(self, created_at):
        self.created_at = created_at
    def get_instance_id(self):
        return self.instance_id
    def set_instance_id(self, instance_id):
        self.instance_id = instance_id
    def get_is_super_admin(self):
        return self.is_super_admin
    def set_is_super_admin(self, is_super_admin):
        self.is_super_admin = is_super_admin
    def get_is_active(self):
        return self.is_active
    def set_is_active(self, is_active):
        self.is_active = is_active
    