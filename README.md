# Generador de Perfiles Falsos

Este proyecto es una herramienta para generar perfiles de usuario falsos y respuestas asociadas, adaptados para ser insertados en una base de datos PostgreSQL. Está diseñado para apoyar prácticas y pruebas, permitiendo poblar bases de datos con datos simulados de manera automatizada.

## Características

- Generación automática de perfiles de usuario con datos realistas (nombre, nacionalidad, sexo, correo, contraseña, etc.).
- Generación de respuestas asociadas a cada perfil.
- Inserción directa de los datos en una base de datos PostgreSQL.
- Configuración flexible mediante variables de entorno.
- Estructura modular y extensible.
- Uso de archivos JSON para datos de nombres y nacionalidades.
- Manejo seguro de contraseñas con bcrypt.
- Context manager para transacciones seguras en la base de datos.

## Estructura del Proyecto

```
metodologia/
│
├── database/
│   └── connection.py         # Manejo de la conexión a PostgreSQL
│
├── generators/
│   ├── generator.py          # Clase base abstracta para generadores
│   ├── profile_generator.py  # Generador de perfiles
│   └── answer_generator.py   # Generador de respuestas
│
├── models/
│   ├── User.py               # Modelo de usuario
│   └── Profile.py            # Modelo de perfil
│
├── scripts/
│   └── answer_insertor.py    # Inserta respuestas en la base de datos
│
├── data/
│   └── names.json            # Datos de nombres y nacionalidades
│
├── main.py                   # Script principal de ejecución
├── .env                      # Variables de entorno para la conexión
├── LICENSE                   # Licencia GPL v3
└── README.md                 # Este archivo
```

## Instalación

1. **Clona el repositorio:**
   ```sh
   git clone <URL-del-repositorio>
   cd metodologia
   ```

2. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configura las variables de entorno:**
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```
   POSTGRESQL_HOST=localhost
   POSTGRESQL_PORT=5432
   POSTGRESQL_USER=tu_usuario
   POSTGRESQL_PASSWORD=tu_contraseña
   POSTGRESQL_DB=tu_base_de_datos
   ```

4. **Agrega el archivo de datos:**
   Asegúrate de que `data/names.json` exista y tenga el formato adecuado para los nombres y nacionalidades.

## Uso

Ejecuta el generador desde la terminal:

```sh
python main.py
```

El programa solicitará la cantidad de perfiles a generar y realizará la inserción automática en la base de datos configurada.

## Ejemplo de flujo

1. El usuario ingresa el número de perfiles a generar.
2. El sistema crea cada perfil con datos aleatorios y seguros.
3. Se generan respuestas asociadas a cada perfil.
4. Los datos se insertan en la base de datos PostgreSQL.
5. Al finalizar, se muestra un resumen de la operación.

## Requisitos

- Python 3.10+
- PostgreSQL
- Paquetes: `psycopg2`, `bcrypt`, `python-dotenv`, etc.
