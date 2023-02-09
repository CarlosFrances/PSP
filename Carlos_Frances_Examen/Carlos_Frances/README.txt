Lista de rutas:
    /usuarios --> retorna el objeto con la lista de usuarios completa.


    /usuarios/<user> --> retorna el diccionario con los datos del usuario introducido.
    Mostrará un error en su lugar cuando no exista ningun usuario que coincida con el introducido.


    /log_usuario/<user>/<passw> --> retorna el diccionario con los datos del usuario introducido.
    Mostrará un error en su lugar cuando no exista ningun usuario que coincida con el introducido o
    cuando el usuario no tenga la contraseña indicada.


    /registrar/<usuario>/<password>/<nombre>/<correo>/<nacimiento> --> retorna el usuario "registrado".
    Mostrará un error en su lugar cuando los parámetros introducidos no cumplan las condiciones de regulación indicadas
    dentro del método "registrar()"