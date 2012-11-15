# Entornos virtuales #

## Instalacion ## 

Como root:

    sudo pip install virtualenv virtualenvwrapper

Como usuario:

    source /usr/local/bin/virtualenvwrapper.sh 
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc 


## Uso ##

### Nuevos entornos ###

    mkvirtualenv nombre_entorno

### Listar entornos ###

    workon

### Entrar a un entorno ###

    workon nombre_entorno

### Eliminar entorno ###

    rmvirtualenv nombre_entorno

### Salirse de un entorno ###

    deactivate

### Listar paquetes de un entorno ###

    lssitepackages


