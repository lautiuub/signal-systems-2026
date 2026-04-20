import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import math

    return math, mo


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 3: Ejercicios Practicos
    ## Construir con Funciones

    En estos ejercicios vas a crear funciones completas con docstrings, type hints, y (en algunos casos) tests.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: midi_a_hz

    Escribi una funcion `midi_a_hz(nota_midi)` que convierta un numero de nota MIDI a frecuencia en Hz.

    **Requisitos:**
    - Formula: `f = 440 * 2**((midi - 69) / 12)`
    - Docstring estilo NumPy
    - Type hints
    - Validacion: si `nota_midi` no esta entre 0 y 127, lanzar `ValueError`

    Proba con MIDI 60, 69, 72, y 48.
    """)
    return


@app.cell
def _():
    #defino funcion

    def midi_a_hz(nota_midi : int) -> float:

        """
        Convierte una nota MIDI a su frecuencia correspondiente en Hz.

        Parameters
        ----------
        nota_midi : int
            Numero de nota MIDI (debe estar entre 0 y 127)
    
        Returns
        -------
        float
            Frecuecnia en Hz
    
        Raises
        ------
        ValueError
            Si la nota esta fuera del rango : [0, 127]
        """


        if not (0<= nota_midi <= 127):
            raise ValueError(f"nota midi debe estar entre 0 y 127, se recibió {nota_midi}")
        return 440 * 2**((nota_midi - 69)/12)

    #pruebas

    for m in [60, 69, 72, 48]:
        print(f"{m} -> {midi_a_hz(m):.2f}")
    return (midi_a_hz,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: hz_a_midi

    Escribi la funcion inversa: `hz_a_midi(frecuencia)` que convierta una frecuencia en Hz al numero de nota MIDI mas cercano.

    **Requisitos:**
    - Formula: `midi = round(69 + 12 * log2(freq / 440))`
    - Docstring estilo NumPy
    - Type hints
    - Validacion: si `frecuencia <= 0`, lanzar `ValueError`
    - Necesitas `import math` y usar `math.log2()`

    Proba con 440 Hz, 261.63 Hz, 880 Hz.
    """)
    return


@app.cell
def _(math):
    #defino la funcion

    def hz_a_midi(frecuencia : float) -> int:

        """
        Convierte una frecuencia en Hz al numero de nota MIDI mas cercano.

        Parameters
        ----------
        frecuencia : float
            Frecuencia en Hz
    
        Returns
        -------
        int 
            Nota MIDI mas cercana

        Raises
        ------
        ValueError
            Si la frecuencia es menor a cero.
        """
        


        if (frecuencia <= 0):
            raise ValueError(f"frecuencia debe ser mayor a 0 Hz, se recibió {frecuencia}")
        return round(69 + 12 * math.log2(frecuencia / 440))

    #pruebas

    for f in [440, 261.63, 880]:
        print(f"frecuencia : {f:.2f} -> midi : {hz_a_midi(f)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: aplicar_fade

    Escribi una funcion `aplicar_fade(signal, tipo="in", duracion_ms=100, fs=44100)` que aplique un fade lineal a una senal.

    **Requisitos:**
    - `tipo` puede ser `"in"` (fade in) o `"out"` (fade out)
    - El fade es **lineal**: multiplica las muestras por un factor que va de 0 a 1 (fade in) o de 1 a 0 (fade out)
    - `duracion_ms` indica cuantos milisegundos dura el fade
    - La funcion retorna una **nueva lista** (no modifica la original)
    - Docstring y type hints

    **Ejemplo de fade in de 4 muestras sobre 8 muestras:**
    ```
    Original: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    Factores: [0.0, 0.33, 0.67, 1.0, 1.0, 1.0, 1.0, 1.0]
    Resultado:[0.0, 0.33, 0.67, 1.0, 1.0, 1.0, 1.0, 1.0]
    ```
    """)
    return


@app.cell
def _():
    #creo funcion

    def aplicar_fade(
        signal: list[float],
        tipo: str = "in",
        duracion_ms: float = 100,
        fs: int = 44100
        ) -> list[float]:

        """
        Aplica un fade lineal (aprecer o desaparecer progresivamente) a una senal.

        Parameters
        ----------
        signal: list[float]
            Lista de muestras de audio original
        tipo : str, optional
            "in" para fade-in, "out"para fade-out (default "in")
        duracion_ms : float, optional
             Cuanto dura el efecto en ms (default 100)
        fs : int, optional
            Frecuencia de muestreo en Hz (default 44100)
    
        Returns
        -------
        list[float]
            Una nueva lista con el fade aplicado a la senal de entrada(audio original)
        """


        #1.
        #cuantas muestras dura el fade?
        #ya que el fade lineal multiplica las muestras por un factor
        #(de 0 a 1 o de 1 a 0)

        n_fade = int(fs * (duracion_ms / 10**3))

        #luego, si el fade es mas largo que el audio,
        #lo limitamos

        n_fade = min(n_fade, len(signal))


        #2.
        #guardamos la senal

        resultado = list(signal)


        #3.
        #aplicar la logica

        for i in range(n_fade):
            factor = i / n_fade

            if tipo == "in":
                resultado[i] = round(resultado[i] * factor, 2)
            elif tipo == "out":
                resultado[-(i+1)] =round(resultado[-(i+1)] * factor, 2)
    
        return resultado



    #Pruebo la funcion

    #senal original (de prueba)
    original = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    #prueba de fade-in (utilizando valores por default)
    test_in = aplicar_fade(original, tipo = "in")

    #prueba de fade-out (utilizando valores por default)
    test_out = aplicar_fade(original, tipo = "out")

    #imprimo para ver los resultados

    print("Resultados:")
    print(f"Original : {original}")
    print(f"Fade in : {test_in}")
    print(f"Fade-out : {test_out}")



    #Prueba 2: el fade no ocupe toda la senal -> le paso una duracion menor (0.07 ms)
    original2= [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    test_in2= aplicar_fade(original2, tipo = "in", duracion_ms= 0.07)
    test_out2= aplicar_fade(original2, tipo = "out", duracion_ms=0.07)

    print("Resultados2")
    print(f"Orginal 2 : {original2}")
    print(f"Fade-in 2 : {test_in2}")
    print(f"Fade-out 2 : {test_out2}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: mezclar_senales

    Escribi una funcion `mezclar_senales(*signals, pesos=None)` que mezcle multiples senales.

    **Requisitos:**
    - Recibe un numero variable de senales (listas de floats) via `*signals`
    - Si `pesos` es `None`, todas las senales tienen el mismo peso (1/N)
    - Si `pesos` es una lista, cada senal se multiplica por su peso correspondiente
    - Todas las senales deben tener la misma longitud
    - Retorna la mezcla como una nueva lista
    - Docstring y type hints

    **Ejemplo:**
    ```python
    a = [1.0, 0.5, -0.5]
    b = [0.0, 1.0, 0.0]
    mezclar_senales(a, b)                  # -> [0.5, 0.75, -0.25]
    mezclar_senales(a, b, pesos=[0.8, 0.2]) # -> [0.8, 0.6, -0.4]
    ```
    """)
    return


@app.cell
def _():
    #defino la funcion

    def mezclar_senales(*signals : tuple[list[float]], pesos : list[float] | None = None) -> list[float]:

        """
        Mezclar multiples senales

        Parameters
        ----------
        *signals : tuple[list[float]]
            tupla de senales que se quieren mezclar; donde cada senal es una list[float]
        pesos : None (default); pesos es una lista -> pesos : list[float]
            peso de la senal en la mezcla
    
        Returns
        -------

        list[float]:
            Lista que contenga la mezcla de las senales de entrada.
        """

        #condiciones


        #1. defino valor de pesos de cada senal a mezclar
        if pesos is None:
            pesos_efectivos = [1 / len(signals)] * len(signals)
        else:
            pesos_efectivos = pesos
    

        #2. verifico que las longitudes de las senales sean iguales
        longitud = len(signals[0])
        for senal in signals:
            if longitud != len(senal):
                raise ValueError(f"Las longitudes de las senales deben ser iguales")
    
        #funcion

        #1. lista vacia(donde voy a ir sumando las muestras de cada senal con su correspondiente peso)
        resultado = [0.0] * longitud

        #2. suma muestra por muestra con su correspondiente peso
        for senal, peso in zip(signals, pesos_efectivos):
        
            #enumerate() recorre una lista y da dos cosas a la vez: indice(i) y valor(muestra)

            for i, muestra in enumerate(senal):
                resultado[i] += muestra * peso
                resultado[i] = round(resultado[i], 2)
    
        return resultado


    #probar la funcion

    a = [1.0, 0.5, -0.5]
    b = [0.0, 1.0, 0.0]

    #prueba con pesos : None = None
    mezcla_sin_pesos = mezclar_senales(a, b)

    #prueba con pesos = [0.8, 0.2]
    mezcla_pesos = mezclar_senales(a, b, pesos = [0.8, 0.2])

    #imprimo para ver los resultados

    print(f"Senal a : {a}")
    print(f"Senal b : {b}")
    print(f"Mezcla sin haber indicado pesos : {mezcla_sin_pesos}")
    print(f"Mezcla habiendo indicado pesos : {mezcla_pesos} ")

    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: info_audio

    Escribi una funcion `info_audio(nombre, sr=44100, **kwargs)` que retorne un string formateado con informacion del archivo de audio.

    **Requisitos:**
    - Siempre muestra nombre y sample rate
    - Cualquier parametro adicional (**kwargs) tambien se muestra
    - Retorna un string (no imprime directamente)
    - Docstring y type hints

    **Ejemplo de uso:**
    ```python
    info_audio("cancion.wav", sr=48000, bits=24, canales=2, artista="Queen")
    ```
    **Resultado:**
    ```
    === cancion.wav ===
    Sample Rate: 48,000 Hz
    bits: 24
    canales: 2
    artista: Queen
    ```
    """)
    return


@app.cell
def _():
    #funcion

    def info_audio(nombre : str = "nombre", sr : int = 44100, **kwargs) -> str:

        """
        Genera un string con informacion de un archivo de audio

        Paramters
        ---------
        nombre : str
            Nombre del archivo
        sr : int, optional
            Sample rate en Hz (default 44100)
        **kwargs
            Parametros adicionales
    
        Returns
        -------
        str
            String formateado con la informacion
        """

        #creo lineas (lista de strings)

        lineas = [
            f"=== {nombre} ===",
            f"Sample Rate : {sr:,} Hz",

        ]


        # cada elemento del diccionario kwargs -> lista lineas

        for clave, valor in kwargs.items():
            lineas.append(f"{clave} : {valor}")
    
        return "\n".join(lineas)


    #prueba

    prueba = info_audio("cancion.wav", sr = 48000, bits = 24, canales = 2, artista = "Queen")

    print(prueba)

    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Crear un modulo

    Este ejercicio es para hacer **fuera del notebook**, en un archivo separado.

    Crea un archivo llamado `mis_funciones.py` que contenga:

    1. `midi_a_hz(nota_midi)` - del ejercicio 1
    2. `hz_a_midi(frecuencia)` - del ejercicio 2
    3. `calcular_rms(signal)` - calcula el RMS de una lista de muestras

    Cada funcion debe tener docstring y type hints.

    Agrega un bloque `if __name__ == "__main__":` que demuestre el uso de cada funcion.

    Despues de crearlo, verifica que funciona:
    ```bash
    python mis_funciones.py
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    (Este ejercicio se resuelve creando el archivo. En la celda siguiente, simula la importacion.)
    """)
    return


@app.cell
def _():
    from mis_funciones import midi_a_hz as _midi_a_hz, hz_a_midi as _hz_a_midi, calcular_rms

    print(f"midi_a_hz(69) -> {_midi_a_hz(69): .2f} Hz")
    print(f"hz_a_midi(440) -> {_hz_a_midi(440):.2f}")
    print(f"calcular_rms([10, -10, 10, -10]) -> {calcular_rms([10, -10, 10, -10])}")


    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Tests para midi_a_hz

    Escribi **3 funciones de test** para la funcion `midi_a_hz` del ejercicio 1.

    Los tests deben seguir el formato de pytest (funciones que empiezan con `test_`):

    1. `test_midi_a_hz_a4()` - verifica que MIDI 69 retorna 440.0
    2. `test_midi_a_hz_octavas()` - verifica que subir 12 semitonos duplica la frecuencia
    3. `test_midi_a_hz_rango_invalido()` - verifica que MIDI -1 o 128 lanza ValueError

    Para el test 3, usa un bloque `try/except`:
    ```python
    try:
        midi_a_hz(-1)
        assert False, "Deberia haber lanzado ValueError"
    except ValueError:
        pass  # OK, se espera el error
    ```

    Ejecuta todos los tests y muestra los resultados.
    """)
    return


@app.cell
def _(midi_a_hz):
    def test_midi_a_hz_a4():
        assert midi_a_hz(69) == 440.0

    def test_midi_a_hz_octavas():
        assert midi_a_hz(81) == midi_a_hz(69) * 2

    def test_midi_a_hz_rango_invalido():
        try:
            midi_a_hz(-1)
            assert False, "Deberia haber lanzado ValueError"
        except ValueError:
            pass #OK, se espera el error


    tests = [test_midi_a_hz_a4, test_midi_a_hz_octavas, test_midi_a_hz_rango_invalido]

    for test in tests:
        try:
            test()
            print(f"PASS : {test.__name__}")
        except AssertionError as e:
            print(f"FAIL : {test.__name__} - {e}")



    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: normalizar con tests

    Escribi una funcion `normalizar(signal)` que normalice una senal al rango [-1, 1].

    **Requisitos:**
    - Encuentra el valor absoluto maximo de la senal
    - Divide todas las muestras por ese valor
    - Si la senal es toda ceros, retorna la senal sin cambios
    - Docstring, type hints

    Ademas, escribi **3 tests**:
    1. `test_normalizar_basico()` - una senal con pico en 0.5 debe tener pico en 1.0
    2. `test_normalizar_ya_normalizada()` - una senal con pico en 1.0 no cambia
    3. `test_normalizar_silencio()` - una senal de ceros retorna ceros

    Ejecuta los tests y muestra resultados.
    """)
    return


@app.cell
def _():



    def normalizar(signal : list[float]) -> list[float]:
        """
        normaliza los valores de muestra de una senal

        Parameters
        ----------
        signal : list[float]
            senal de entrada(no normalizada)
    
        Returns
        -------
        list[float]
            senal de entrada NORMALIZADA al rango [-1, 1]
        """


        _resultado = [0.0] * len(signal)
        maximo = max(abs(m) for m in signal)

        if maximo == 0:
            _resultado = signal
        else:
            for i, muestra in enumerate(signal):
                _resultado[i] += muestra * (1/maximo)
                _resultado[i] = round(_resultado[i], 2)
    
        return _resultado



    def test_normalizar_basico():
        assert normalizar([0.5]) == [1.0]

    def test_normalizar_ya_normliazada():
        assert normalizar([1.0]) == [1.0]

    def test_normalizar_silencio():
        assert normalizar([0.0]) == [0.0]


    tests_ = [test_normalizar_basico, test_normalizar_silencio, test_normalizar_ya_normliazada]

    for test_ in tests_:

        try:
            test_()
            print(f"PASS : {test_.__name__}")
        except AssertionError as e:
            print(f"FAIL : {test_.__name__} - {e}")




    return


if __name__ == "__main__":
    app.run()
