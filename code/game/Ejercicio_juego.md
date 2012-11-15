


- Se crearan 3 clases Object, World, Player
- La clase Object tendra dos atributos que seran enteros llamados position_x, position_y
- La clase World tendra un atributo llamadosamado objects que sera una lista vacia
- La clase Player tendra los siguientes atributos

    - name que sera cadena
    - points, max_life, current_life, position_x, position_y, points que seran enteros

- Los atributos position_x y position_y de la clase Player seran valores aleatorios de 1 a 100
- La clase Player tendra 4 metodos

    - status que sera publico y muestra el nombre del player, sus cordenadas y una barra de vida, donde los puntos de vida actuales se muestran con [·] y el resto de los espacios de vida total con [ ]

    - command recice un parametro y si coincide con un comando definido lo ejecuta, se definiran 4 comandos basicos para moverse por el tablero de 100 x 100, los comandos seran up, down, left, right y se movera un punto a la vez sin salirse del mapa

    - __distribute_points el metodo privado servira para distribuir puntos en diferentes skills, primero se distribuira lo puntos a la barra de vida, si nuestro current_life es menor al max_life aumentamos el current_life en proporcion igual a los puntos asignados si es igual aumentamos el max_life y los current_life. Los puntos que agregas a la barra de vida los restaremos del atributo points.

    - constructor el constructor pedira el nombre del jugador, mostrara el status y distribuira puntos


- Al ejecutar la aplicacion instanciaremos las 4 clases, crearemos un objeto en una cordenada del mapa y lo agregaremos al mapa, entraremos a un bucle infinito done se nos pedira comandos constantemente y en el prompt mostraremos las cordenadas actuales si en la cordnada actual hay un objeto avisar.

