1. Propósito de los Archivos SQL

El proyecto de la base de datos de hogar inteligente está dividido en dos archivos SQL para una mejor organización y claridad:

`consultasDDL.sql`: Contiene el Lenguaje de Definición de Datos (DDL), responsable de crear y estructurar la base de datos. 
Este script crea la base de datos smart_home_solutions y todas las tablas (usuarios, dispositivos, automatizaciones, y acciones) 
con sus respectivas claves primarias (PRIMARY KEY) y claves foráneas (FOREIGN KEY).

`consultasDML.sql`: Contiene el Lenguaje de Manipulación de Datos (DML), que se encarga de insertar los datos de ejemplo en las 
tablas creadas por el script DDL. Este script sirve para poblar la base de datos con información relevante para probar las relaciones 
y las funcionalidades del sistema.

2. Instrucciones de Ejecución

Para garantizar una ejecución exitosa, es fundamental seguir un orden específico:

Ingresar a https://onecompiler.com/sqlite, allí deberás pegar y ejecutar los siguientes archivos que se encuentran en esta carpeta.

Ejecutar `consultasDDL.sql`: Este es el primer archivo que se debe ejecutar. Al crearse la base de datos y las tablas, se establece la estructura que las consultas DML necesitan para funcionar. Es necesario ejecutar este script primero para evitar errores de referencia a tablas que aún no existen.

Ejecutar `consultasDML.sql`: Después de que la base de datos y las tablas estén creadas, se puede ejecutar este script. Si se ejecuta antes, las instrucciones INSERT fallarán porque las tablas a las que intentan agregar datos no se habrán creado.