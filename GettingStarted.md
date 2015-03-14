# Requisitos #

  * Python (2.5.1 o superior)
  * Pygame
  * Subversion


# Antes de empezar #

Localiza tu archivo de configuración de Subversion (archivo _config_ en C:\Documents and Settings\User\Application Data\Subversion en Windows XP, /home/User/.subversion en Linux). Añade la siguiente línea a la sección [auto-props]:
```
*.py = svn:eol-style=native; svn:keywords=Id Author Date Revision
```