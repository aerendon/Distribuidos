# Proyecto I

## Enunciado:

* __Sincronización:__ Tener sincronizado los relojes de todos los clientes, se debe pedir cada cuanto se quiere que se actualicen los relojes.

* __Algortimo de cristian:__ Como hacer un programa para que tome la hora de internet con python. Para poder hacer bien la simulacion el segundo parametro de entrada que se requiere es hora minutos y segundos, para hacer pruebas.
Si llega una hora menor a la actual, hay que incrementar el reloj de forma reducida hasta que se iguale con la hora que entrego internet.

* __Algoritmo de berkeley:__ Se elije un programa servidor y este pregunta cada X tiempo la hora a todos los clientes, se saca un promedio de la hora y esa sera la nueva hora.
Si llega una hora menor a la actual, hay que incrementar el reloj de forma reducida hasta que se iguale con la hora que entrego internet.

* __Algoritmo con promedios:__ Dividir el tiempo en intervalos, se envian la hora todos entre todos y cada uno saca un promedio con lo que recibe y obtiene la hora. Cuando los tiempos dañan el promedio alejandolo de la media se descartan.
