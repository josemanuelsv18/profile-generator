from generator import Generator
from models.Profile import Profile
from datetime import datetime
import random
import uuid
import secrets
import string
import bcrypt

class ProfileGenerator(Generator):
    def __init__(self):
        super().__init__()

    #Random data generation methods
    #Generates a random UUID
    def random_uuid(self):
        return str(uuid.uuid4())
    
    def radom_nationality(self):
        # List of possible nationalities
        data = self.read_json('data/countries.json')
        #countries = ['Panamá', 'Colombia', 'Venezuela', 'China']
        countries = list(data.keys())
        nationality: str
        random_nationality = random.random()
        # 85% chance of being from Panama
        # 15% chance of being from Colombia, Venezuela, or China
        if random_nationality <= 0.85:
            nationality = countries[0]
        else:
            random_nationality = random.choice(countries[1:])
        return nationality
    
    def random_sex(self):
        sex = random.randomint(0, 1)
        if sex == 0:
            sex = "masculino"
        else:
            sex = "femenino"
        return sex

    def random_name(self, sex, nationality):
        # Reads names from a JSON file and returns a random name based
        try:
            data = self.read_json('data/names.json')
        except FileNotFoundError:
            print("Error: El archivo de nombres no se encontró.")
            return None
        try:
            name = ""
            if nationality == 'China': # Special case for China
                random_ch_hispanic = random.randomint(0, 1) # 50% chance of being Chinise-Hispanic
                if random_ch_hispanic == 1: # If it's Hispanic-Chinese
                    counrty = 'Panamá'
                    name = random.choice(counrty['nombres'][sex]) 
            # If it's not China, proceed with the normal logic
            counrty = data[nationality]
            name = random.choice(counrty['nombres'][sex])
            lastname = random.choice(counrty['apellidos'])
            return [name, lastname]
        except KeyError:
            print(f"Pais o sexo no encontrado: {nationality}, {sex}")
            return None
        
    def generate_email(self, n):
        # Generates a random email based on the name and a random email service
        email_service = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'utp.edu.pa']
        ran_email_service = random.random()
        email_service_choice = ''
        ran_num = random.randint(0,99)
        if ran_email_service <= 0.75: # 75% chance of using the first email service
            email_service_choice = email_service[0]
        else:
            email_service_choice = random.choice(email_service[1:]) # 25% chance of using any other email service
        email = f"{n[0]}.{n[1]}.{ran_num}@{email_service_choice}" # Format: name.lastname.randomnumber@service
        return email

    def random_password(self):
        # Generates a random password with a length between 8 and 16 characters
        password_length = random.randint(8, 16)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for i in range(password_length))
        # Hash the password using bcrypt (cost factor of 10)
        salt = bcrypt.gensalt(rounds=10)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def generate(self):
        # Generate a random profile
        nationality = self.radom_nationality()
        sex = self.random_sex()
        fullname_list = self.random_name(sex, nationality)
        fullname = ' '.join(fullname_list)
        user_role = 'patient'
        id = self.random_uuid()
        aud = 'authenticated'
        role = 'authenticated'
        email = self.generate_email(fullname_list)
        encrypted_password = self.random_password()
        created_at = datetime.now()
        instance_id = '00000000-0000-0000-0000-000000000000'
        is_super_admin = False
        is_active = True
        # Create a Profile instance
        profile = Profile(
            nombre=fullname,
            user_role=user_role,
            id=id,
            aud=aud,
            role=role,
            email=email,
            encrypted_password=encrypted_password,
            created_at=created_at,
            instance_id=instance_id,
            is_super_admin=is_super_admin,
            is_active=is_active
        )
        # Return the generated profile
        return profile