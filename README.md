# Scraping Precio Miel

El siguiente proyecto fue realizado para obtener actualizaciones de los precios de miel. El mismo simplemente obtiene información de las páginas especificadas en el archivo pages.csv

## Instalacion

1. Clonar el repositorio

    ``` bash

    git clone https://github.com/c05m4r/scraping_precio_miel.git

    ```

2. Dirigirse a la carpeta del proyecto

    ``` bash

    cd ./scraping_precio_miel

    ```

3. Crear un entorno virtual

    ``` bash

    python -m venv env

    ```

4. Activar el entorno virtual

    ``` bash

    source env/bin/activate

    ```

5. Instalar paquetes requeridos con pip

    ``` bash

    pip install -r requerements.txt 

    ```

6. Crear una API Key [aquí](https://core.telegram.org/bots#how-do-i-create-a-bot)

7. Agregar la API key de la forma

    <details>

    <summary>Desplegar</summary> 

    ### Windows

    1. Haz clic derecho en "Este equipo" y selecciona "Propiedades" en el menú contextual.
    2. En la ventana de Propiedades del sistema, haz clic en "Configuración avanzada del sistema".
    3. En la ventana Propiedades del sistema, selecciona la pestaña "Opciones avanzadas" y haz clic en 
    4. En la sección "Variables del sistema" o "Variables de usuario", haz clic en "Nuevo".
    5. Ingresa el nombre y el valor de la variable de entorno que deseas agregar y haz clic en "Aceptar".

    O por el comando

    ``` bash

    setx API_KEY <clave>
    setx CHAT_ID @nombrecanal

    ```

    ### POSIX

    ``` bash

    echo -e "API_KEY=<clave>\nCHAT_ID=@nombrecanal" >> .env

    ```

    </details>

5. Ejecutar el script

    ``` bash

    python main.py

    ```
