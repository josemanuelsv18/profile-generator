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
	'00000000-0000-0000-0000-000000000000',
	gen_random_uuid(),
	'authenticated',
	'authenticated',
	'josemanuelsv18@gmail.com',
	'$2a$10$.QbRs1bsTJ7Pgj6ziQfioOKrYME9KmZW4s7VMS9s2Y9Czq1GEtMaO',
	NOW(),
	FALSE,
	FALSE
);