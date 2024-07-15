# Soporte Tecnico
Archivos de configuración para un sistema de organizacion de Soporte tecnico desarrollado por Pablo Valdivieso, este sistem permite tener un seguimiento de los clientes y las incidencias de cada uno.

**docker compose.yml**

Se puede utilizar en la consola:<br>
wget 

Cuenta con cuatro servicios que se deben iniciar juntos para que funcionen bien: <br>
1) app: Sistema de seguimiento de clientes desarrollado en python por Pablo Valdivieso que permite tener un seguimiento de los clientes y las incidencias de cada uno.<br>
2) postgress: Base de datos postgress.<br>
3) npm: Nginx-Proxy-Manager segun la documentacion oficial sirve para proporcionar a los usuarios una manera fácil de configurar hosts con un proxy inverso y certificados SSL, tiene que ser tan fácil que un mono pueda hacerlo. En resumen sirve para manejar dominios, sub-dominios y certificados ssl, etc.

Estan configurados con una lan para poder conectarse con otros docks y por nombre de host, hay que tener cuidado con dos aspectos muy importantes:<br>
1) Todos los docks deben tener la misma red para poder conectarse a otros servicios, para agregar un nuevo servicio se debe configurar la lan como "external: true"<br>
2) Los puertos no se declaran ya que se manejan con el NPM (Nginx-Proxy-Manager)

**IMPORTANTE**<br>

Hay que crear las carpetas:
* soporte-data -> en esta carpeta se guardan los datos del sistema
* postgres-data -> en esta carpeta se guarda la base de datos
* npm-data -> para guardar las configuraciones de Nginx-Proxy-Manager
* letsencrypt -> para guardar los certificados ssl
