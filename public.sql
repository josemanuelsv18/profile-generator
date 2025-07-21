INSERT INTO public.profiles (id, nombre, role )
VALUES ('3c380444-0258-4741-9d23-806c51e053f1', 'Josemanuel Sifontes', 'patient');
-- ¿Con qué frecuencia consume frutas y verduras frescas durante la semana?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	1,
	4,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Con qué frecuencia consume bebidas azucaradas o comidas ultraprocesadas?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	2,
	9,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Cuántas comidas principales realiza al día?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	3,
	15,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Con cuántas personas habla en el día?
--INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
--	"preguntaId",
--	"respuestaId",
--	"profileId_response",
--	"profileId_paciente",
--	CREATED_AT
--) VALUES (
--	5,
--	15,
--	'3c380444-0258-4741-9d23-806c51e053f1',
--	'3c380444-0258-4741-9d23-806c51e053f1',
--	NOW()
--);
--¿Con qué frecuencia interactúas con otras personas fuera de tu entorno familiar?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	6,
	21,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Te resulta fácil iniciar una conversación con desconocidos?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	7,
	24,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Participas regularmente en actividades sociales o comunitarias?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	8,
	27,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Tienes al menos una persona con la que puedas hablar de tus problemas?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	9,
	33,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Te sientes cómodo/a al trabajar en equipo con otras personas?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	10,
	37,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Con qué facilidad recuerdas lo que hiciste hace pocos días?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	11,
	40,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Te cuesta mantener la concentración en una tarea durante varios minutos?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	12,
	43,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Sientes que puedes resolver problemas o tomar decisiones con claridad?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	13,
	49,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Cómo evalúas tu capacidad para aprender cosas nuevas?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	14,
	53,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Te resulta fácil organizar tus ideas o planificar actividades?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	15,
	55,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Con qué frecuencia realiza alguna actividad física ligera, como caminar o estirarse?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	16,
	60,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Cómo se siente en cuanto a su nivel de energía física durante el día?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	17,
	63,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿El ejercicio o el movimiento forman parte de su rutina diaria?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	18,
	67,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Se siente motivado/a a mantenerse activo/a físicamente?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	19,
	69,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);
--¿Cómo responde su cuerpo cuando realiza algún esfuerzo físico prolongado, como caminar más de lo habitual?
INSERT INTO public.RESPUESTA_PREGUNTAS_USUARIOS (
	"preguntaId",
	"respuestaId",
	"profileId_response",
	"profileId_paciente",
	CREATED_AT
) VALUES (
	20,
	75,
	'3c380444-0258-4741-9d23-806c51e053f1',
	'3c380444-0258-4741-9d23-806c51e053f1',
	NOW()
);