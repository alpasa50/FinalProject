# FinalProject

Codificar informacion del clima como enteros para reducir espacio de almacenamiento.


ISO 8601 Data elements and interchange formats – Information interchange – Representation of dates and times is an international standard covering the exchange of date- and time-related data.

Full format:
    yyyy-MM-ddTHH24:mm:ss.fff±hh:mm
        yyyy: Año
        MM: Mes
        dd: dia
        T: literal (separa Date de Time)
        HH24: Hora en formato 24 (00-23)
        mm: Minutos
        ss: segundos
        fff: milisegundos
        ±hh:mm: time zone en formato 24 hrs (00:00 - 23:59)

    Ejemplo: 2020-07-13T19:30:25.525-04:00
        "13 de Julio del 2020, a las 7 hrs, 30 minutos, 25 segundos con 525 milisegundos de la zona horaria GMT-04:00 (La Paz / Sando Domingo)"

2020     => 111 1110 0100 (año)                => 12 (hasta el 4,095 1111 1111 1111)
12         =>          1100 (mes)                    =>  4
31         =>        1 1111 (dia)                     =>  5
23         =>        1 0111 (hora)                   =>  5
59         =>       11 1011 (minutos)             =>  6
59         =>       11 1011 (segundos)           =>  6
999       =>  11 1110 0111 (millis)              => 10
23         =>        1 0111 (tz hora)               =>  5
59         =>       11 1011 (tz minutos)         =>  6
----------------------------------------------------------------------

01111110010011001111110111111011111011111110011110111111011 => 59 bits

Temperatura (C, There are 100 degrees between the freezing (0°) and boiling points (100°) of water on the Celsius scale):
    Min: 00-100 (110 0100) => 7 bits
    Max: 00-100               => 7 bits
    Precipitacion ("probabilidad de lluvias"): 0-100% => 7 bits

Sample Input Events (CSV input file):
DateAndTime,MinTemp,MaxTemp,Precipitation
2020-07-13T19:30:25.525-04:00,25,34,30

Codificar como una pareja de enteros: 64 bits (date) y 32 bits (variables climatologicas).
Ejemplo (CSV output file):
DateAndTime,Climate
5464687,465468

Notas:
Individual
Hacer 3 implementaciones:
Procedural (lenguaje C o Rust)
Orientado a objetos (lenguaje C# o Java)
Funcional (lenguaje JavaScript, Python, Scala, F#, o similar)
