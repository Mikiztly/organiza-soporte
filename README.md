# Soporte Tecnico

[![GitHub last commit](https://img.shields.io/github/last-commit/Mikiztly/organiza-soporte)](https://img.shields.io/github/last-commit/Mikiztly/organiza-soporte)
[![GitHub](https://img.shields.io/github/license/Mikiztly/organiza-soporte)](https://img.shields.io/github/license/Mikiztly/organiza-soporte)

Sistema para organizar y llevar un control de los trabajos realizados en el departamento de Soporte Técnico desarrollado por Pablo Valdivieso, este sistema permite tener un seguimiento de los clientes y las incidencias de cada uno.
Lo que hice fue poner todo el proyecto en un docker para mejorar su desarrollo y posterior publicacion, agregue varios servicios:

* [PostgreSQL](https://www.postgresql.org/): Es un potente sistema de base de datos relacional de código abierto con más de 35 años de desarrollo activo que le ha ganado una sólida reputación por su fiabilidad, robustez y rendimiento.
* [pgadmin](https://www.pgadmin.org/): pgAdmin es la plataforma de administración y desarrollo de código abierto más popular y rica en características para PostgreSQL, la base de datos de código abierto más avanzada del mundo.
* [Nginx-Proxy-Manager](https://nginxproxymanager.com/): Segun la documentacion oficial sirve para proporcionar a los usuarios una manera fácil de configurar hosts con un proxy inverso y certificados SSL, tiene que ser tan fácil que un mono pueda hacerlo. En resumen sirve para manejar dominios, sub-dominios y certificados ssl, etc.

Tiene configurada una red para poder manejar subdominios con Nginx-Proxy-Manager solamente refiriendose al nombre del contenedor y su puerto, los puertos que se deben abrir son: 80 - 443 - 81. El puerto 81 es para poder ingresar a NPM por primera vez. Todos los docks deben tener la misma red para poder conectarse a NPM y entre ellos, para agregar un nuevo servicio se debe configurar la lan como "external: true".

Para tener datos permanentes se declaran volumenes para redirigir esos archivos a otra particion, disco, etc. De esta forma se puede actualizar o recuperar facilmente todo el sistema.

**IMPORTANTE**<br>

Para evitar errores hay que crear las carpetas:
* letsencrypt -> para guardar los certificados ssl
* npm-data -> para guardar las configuraciones de Nginx-Proxy-Manager
* pgadmin-data -> aca se guardan las conecciones y datos para manejar la base de datos
* postgres-data -> en esta carpeta se guarda la base de datos
* soporte-data -> en esta carpeta se guardan los datos del sistema
