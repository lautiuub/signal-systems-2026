import marimo

__generated_with = "0.23.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import time

    return math, np, plt, time


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 4: Ejercicios practicos
    ## El Universo NumPy y las Senales

    Completa cada ejercicio en la celda indicada. Todos los ejercicios requieren NumPy y Matplotlib.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Eje temporal

    Crea un eje temporal para una senal de **2 segundos** muestreada a **48000 Hz**.

    - Usa `np.arange`
    - Verifica que el numero de muestras sea correcto (debe ser 96000)
    - Verifica que la ultima muestra sea menor que 2.0 segundos
    - Imprime: numero de muestras, primera muestra, ultima muestra, duracion total
    """)
    return


@app.cell
def _(np):
    #valores que vamos a probar
    fs = 48000
    duracion = 2

    #calculamos N -> cantidad total de muestras de la senal de 2 segundos muestrada a 48000 Hz
    N = int(fs * duracion)

    #eje temporal -> idea: muestra0, muestra1, muestra2, ...*(1/fs) -> muestran/fs = segundos(eje temporal)
    t = np.arange(N) * (1/fs)

    #verificaciones
    print(f"lent(t) == 96000 ? -> {len(t) == 96000}")
    print(f"ultima muestra < 2.0 s ? -> {t[-1] < 2.0}")

    #impresiones
    print(f"numero de muestras -> {len(t)}")
    print(f"primera muestra -> {round(t[0], 6)}")
    print(f"ultima muestra -> {round(t[-1], 6)}")
    print(f"duracion total -> {round(t[-1] + (1/fs), 6)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Senoidal de 440 Hz

    Genera una senoidal de **440 Hz** con amplitud 1, muestreada a **44100 Hz**.

    - Calcula cuantas muestras corresponden a exactamente **5 periodos**
    - Genera la senal solo para esos 5 periodos
    - Graficala con `plt.plot()`, incluyendo titulo, labels y grid
    - El eje x debe estar en milisegundos
    """)
    return


@app.cell
def _(np, plt):
    #busco duracion = 5 periodos = 5 T = 5 2pi/omega = 5 2pi/2pif0 -> #muestras
    f0 = 440
    duracion_ = 5 * 1/f0      #segundos

    #defino N(#muestras)
    fs_ = 44100
    N_ = int(fs_ * duracion_)

    #puedo definir ahora si el eje temporal
    t_ = np.arange(N_) * 1/fs_

    #genero senoidal
    A = 1
    x = A * np.sin(2 * np.pi * f0 * t_) 

    print(f"cantidad de muestras que corresponden a 5 T -> {len(t_)}")

    fig, ax = plt.subplots(figsize = (12, 4))
    ax.plot(t_ * 1000, x,'b-', linewidth = 1.0)
    ax.set_title("Senoidal de 440 Hz", color = 'green', fontsize = 12)
    ax.set_xlabel("Tiempo (ms)")
    ax.set_ylabel("Amplitud")
    ax.grid(True, alpha = 0.3)

    plt.tight_layout()
    fig
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Suma de senoidales

    Genera dos senoidales:
    - **Fundamental**: 440 Hz, amplitud 1.0
    - **Armonico**: 880 Hz, amplitud 0.5

    Ambas a 44100 Hz durante 10 ms. Graficalas en **3 subplots** verticales:
    1. Fundamental sola
    2. Armonico solo
    3. Suma de ambas

    Usa la misma escala en Y para los tres graficos (`set_ylim(-1.6, 1.6)`).
    """)
    return


@app.cell
def _(np, plt):
    f1 = 440
    A1 = 1.0

    f_muestreo = 44100
    duracion1 = 10 / (10 ** 3)

    N1 = int(f_muestreo * duracion1)
    t1 = np.arange(N1) * 1/f_muestreo   
    #t es una lista con el instante exacto de cada muestra

    x1 = A1 * np.sin(2 * np.pi * f1 * t1)

    x2 = (A1 / 2) * np.sin(2 * np.pi * 2 * f1 * t1)

    x3 = x1 + x2

    #ploteamos, 3 subplots verticales

    fig1, axes = plt.subplots(3, 1, figsize = (12, 9), sharex = True)

    axes[0].plot(t1 * (10 ** 3), x1, 'b-', linewidth = 1.0)
    axes[0].set_title("Fundamental sola")
    axes[0].set_ylabel("Amplitud")
    axes[0].set_ylim(-1.6, 1.6)
    axes[0].grid(True, alpha = 0.3)

    axes[1].plot(t1 * (10 ** 3), x2, 'b-', linewidth = 1.0)
    axes[1].set_title("Armonico solo")
    axes[1].set_ylabel("Amplitud")
    axes[1].set_ylim(-1.6, 1.6)
    axes[1].grid(True, alpha = 0.3)

    axes[2].plot(t1 * (10 ** 3), x3, 'b-', linewidth = 1.0)
    axes[2].set_title("Suma de ambas senales: fundamental + armonico")
    axes[2].set_ylabel("Amplitud")
    axes[2].set_xlabel("Tiempo (ms)")
    axes[2].set_ylim(-1.6, 1.6)
    axes[2].grid(True, alpha = 0.3)

    plt.tight_layout()
    fig1
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Impulso unitario con stem

    Crea un array de **1000 muestras** de ceros y coloca un impulso unitario en la **muestra 100**.

    - Graficalo con `plt.stem()` mostrando solo las muestras 80 a 120 (para que se vea bien)
    - Titulo: "Impulso unitario en n=100"
    - Labels apropiados
    """)
    return


@app.cell
def _(np, plt):
    #array de 1000 muestras
    N2 = 1000
    delta = np.zeros(N2)

    #impulso unitario en la muestra 100 (tiene valor 1 en vez de valor 0)
    delta[100] = 1

    #limito la cantidad de muestras que voy a ver
    n2 = np.arange(80, 121)
    fragmento = delta[80 : 121]

    #imprimo
    fig_imp2, ax2 = plt.subplots(figsize = (12, 4))

    ax2.stem(n2, fragmento, linefmt = 'b-', markerfmt = 'bo', basefmt = 'k-')
    ax2.set_title("Impulso unitario en n = 100")
    ax2.set_xlabel("muestras de 80 a 120 (40 muestras en total)")
    ax2.set_ylabel("Amplitud")
    ax2.set_ylim(-0.2, 1.3)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_imp2
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Exponencial decreciente en dB

    Genera una exponencial decreciente que modela una reverberacion con **T60 = 2 segundos**.

    - Frecuencia de muestreo: 44100 Hz
    - Duracion: 3 segundos
    - $\alpha = 6.908 / T_{60}$
    - Grafica en **2 subplots**: escala lineal y escala en dB
    - En el grafico dB, marca con una linea horizontal el nivel -60 dB
    - Marca con una linea vertical el instante T60

    Tip: para convertir a dB usa $20 \log_{10}(|x|)$ y evita el $\log$ de cero con `np.maximum(x, 1e-10)`.
    """)
    return


@app.cell
def _(np, plt):
    f5_muestreo = 44100
    duracion5 = 3
    T60 = 2


    #debo generar eje temporal

    #cantidad de muestras 
    N5 = f5_muestreo * duracion5

    #eje temporal
    t5 = np.arange(N5) * (1/f5_muestreo)
    alpha = 6.908/T60

    x5 = np.exp(-alpha * t5)

    fig5, (ax_lin, ax_dB) = plt.subplots(1, 2, figsize = (12, 4))


    #escala lineal
    x_exp = x5
    ax_lin.plot(t5, x_exp, 'b-', linewidth = 1.5)
    ax_lin.set_title("Exponencial decreciente [escala lineal]")
    ax_lin.set_xlabel("Tiempo [s]")
    ax_lin.set_ylabel("Amplitud ")
    ax_lin.grid(True, alpha = 0.3)

    ax_lin.axvline(x = T60, color = 'r', linestyle = '--', label = f'T60 = {T60:.1f} s')

    ax_lin.legend()
    ax_lin.grid(True, alpha = 0.3)

    #escala en dB
    x_dB = 20 * np.log10(np.maximum(x_exp, 1e-10))
    ax_dB.plot(t5, x_dB, 'b-', linewidth = 1.5)
    ax_dB.set_title("Exponencial decreciente [escala en dB]")
    ax_dB.set_xlabel("Tiempo [s]")
    ax_dB.set_ylabel("Amplitud [dB]")
    ax_dB.set_ylim(-80, 5)

    ax_dB.axvline(x = T60, color = 'r', linestyle = '--', label = f'T60 = {T60:.1f} s')
    ax_dB.axhline(y = -60, color = 'g', linestyle = ':', label = '-60 dB')

    ax_dB.legend()
    ax_dB.grid(True, alpha = 0.3)

    plt.tight_layout()
    fig5
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Envolvente ADSR

    Crea un array que represente una envolvente **ADSR** (Attack-Decay-Sustain-Release) con los siguientes parametros:

    - **Attack**: 10 ms, de 0 a 1.0 (lineal)
    - **Decay**: 20 ms, de 1.0 a 0.7 (lineal)
    - **Sustain**: 200 ms, nivel constante 0.7
    - **Release**: 50 ms, de 0.7 a 0 (lineal)
    - Frecuencia de muestreo: 44100 Hz

    Graficala con `plt.plot()`. Marca con lineas verticales punteadas las transiciones entre cada fase.

    Tip: usa `np.linspace` para cada segmento y `np.concatenate` para unirlos.
    """)
    return


@app.cell
def _(np, plt):
    f6_muestreo = 44100


    #attack: 0 -> 1 en 10 ms a 44100 Hz; cuantas muestras son 10 ms?, como generar ese segmento?
    duracion11 = 10 / (10 ** 3)
    N61 = f6_muestreo * duracion11
    #para el attack se necesita ir de 0 -> 1 en N6 cantidad de muestras
    segmento1 = np.linspace(0.0, 1.0, int(N61))

    #decay: 1 -> 0.7 durante 20 ms
    duracion2 = 2 * duracion11
    N62 = f6_muestreo * duracion2
    segmento2 = np.linspace(1.0, 0.7, int(N62))


    #sustain: constante en 0.7 durante 200 ms
    duracion3 = 200 / (10 ** 3)
    N63 = f6_muestreo * duracion3
    segmento3 = np.full(int(N63), 0.7)

    #release: de 0.7 -> 0 durante 50 ms
    duracion4 = 50 / (10 ** 3)
    N64 = f6_muestreo * duracion4
    segemento4 = np.linspace(0.7, 0.0, int(N64))


    #unimos todos los segmentos (obtengo un array adsr con un total de muestras: MI SENAL)
    adsr = np.concatenate([segmento1, segmento2, segmento3, segemento4])

    #eje temporal
    N6 = int(N61 + N62 + N63 + N64)
    t6 = np.arange(N6) * (1/f6_muestreo)

    #graficamos
    fig6, ax6 = plt.subplots(figsize = (12, 4))
    ax6.plot(t6 * (10 ** 3), adsr, 'b-', linewidth = 1.0)
    ax6.set_title("Envolvente ADSR")
    ax6.set_xlabel("Tiempo [ms]")
    ax6.set_ylabel("Amplitud")
    ax6.grid(True, alpha = 0.3)


    ax6.axvline(x = duracion11 * (10 ** 3), color = 'r', linestyle = '--', label = 'Attack')
    ax6.axvline(x = (duracion11 + duracion2) * (10 ** 3), color = 'g', linestyle = '--', label = 'Decay')
    ax6.axvline(x= (duracion11 + duracion2 + duracion3) * (10 ** 3), color = 'b', linestyle = '--', label = 'Sustain')

    ax6.legend()

    plt.tight_layout()
    fig6
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Broadcasting - Matriz de senoidales

    Usa broadcasting para crear una **matriz** donde cada fila contiene una senoidal de diferente frecuencia.

    - Frecuencias: [100, 200, 400, 800, 1600] Hz
    - Frecuencia de muestreo: 44100 Hz
    - Duracion: 20 ms
    - La matriz debe tener shape `(5, N)` donde N es el numero de muestras

    **Sin usar loops**. Pista: crea un vector columna de frecuencias `(5, 1)` y un vector fila de tiempo `(1, N)`, y multiplica.

    Grafica las 5 senoidales en subplots verticales.
    """)
    return


@app.cell
def _(np, plt):
    #vector columna de frecuencias (5, 1)
    frecuencias = np.array([100, 200, 400, 800, 1600])
    freq_col = frecuencias.reshape(5, 1)

    #debo buscar t
    f7_muestreo = 44100
    duracion7 = 20 / (10 ** 3)
    N7 = f7_muestreo * (duracion7)
    t7 = np.arange(N7) * (1 / f7_muestreo)

    #vector fila de tiempo (1, N)
    t7_fila = t7.reshape(1, int(N7))

    #genero matriz de senoidales usando broadcasting y np.sin

    senal_vect = np.sin(2 * np.pi * freq_col * t7_fila)

    #grafico las 5 senoidales en subplots verticales

    fig7, axes7 = plt.subplots(5, 1, figsize = (12, 10), sharex = True)

    for i in range(5):
        axes7[i].plot(t7 * (10 **3), senal_vect[i], 'b-', linewidth = 1.0)
        axes7[i].set_title(f"{frecuencias[i]} Hz")
        axes7[i].set_ylabel("Amplitud")
        axes7[i].set_xlabel("Tiempo [ms]")
        axes7[i].set_ylim(-1.6, 1.6)
        axes7[i].grid(True, alpha = 0.3)


    plt.tight_layout()
    fig7

    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Comparacion de rendimiento

    Genera **1 millon** de muestras de una senoidal de 440 Hz a 44100 Hz, de dos formas:

    1. Con un **loop for** de Python (usando `math.sin`)
    2. Con **NumPy vectorizado** (usando `np.sin`)

    Usa `time.perf_counter()` para medir el tiempo de cada metodo. Imprime:
    - Tiempo de cada metodo en milisegundos
    - Factor de speedup (cuantas veces mas rapido es NumPy)
    - Verificacion de que ambos resultados son iguales (`np.allclose`)
    """)
    return


@app.cell
def _(math, np, time):
    f8 = 440
    f8_muestreo = 44100
    duracion8 = 1
    N8 = int(f8_muestreo * duracion8)


    #loop for
    inicio = time.perf_counter()
    senal_loop = []
    for i8 in range(N8):
        t8_i = i8 * (1/f8_muestreo)
        senal_loop.append(math.sin(2 * math.pi * t8_i * f8))
    senal_loop = np.array(senal_loop)
    tiempo_loop_ms = round((time.perf_counter() - inicio) * (10 ** 3), 6)

    #NumPy vectorizado
    inicio = time.perf_counter()
    t8 = np.arange(N8) * (1/f8_muestreo)
    senal_vect8 = np.sin(2 * np.pi * f8 * t8)
    tiempo_vect_ms = round((time.perf_counter() - inicio) * (10 ** 3), 6)

    #impresiones
    print(f"Tiempo del metodo 1 : Utilizando Loop For -> {tiempo_loop_ms} [ms]")
    print(f"Tiempo del metodo 2 : Utilizando NumPy Vectorizado -> {tiempo_vect_ms} [ms]")

    print(f"Factor de speedup -> NumPy es {(tiempo_loop_ms / tiempo_vect_ms):.2f} veces mas rapido que loop for")
    print(f"Reusltados iguales -> {np.allclose(senal_loop, senal_vect8)}")


    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 9: Senoidal interactiva

    Crea una senoidal interactiva usando sliders de Marimo:

    - `mo.ui.slider` para **frecuencia** (100 a 2000 Hz, paso 10)
    - `mo.ui.slider` para **amplitud** (0.1 a 1.0, paso 0.1)

    La senal debe mostrarse con `plt.plot()`, siempre mostrando exactamente **5 periodos**.
    El titulo del grafico debe mostrar los valores actuales de frecuencia y amplitud.
    """)
    return


@app.cell
def _(mo):
    f9 = mo.ui.slider(start = 100, stop = 2000, step = 10, value = 440, label = "Frecuencia [Hz]")
    amp9 = mo.ui.slider(start = 0.1, stop = 1.0, step = 0.1, value = 1.0, label = "Amplitud")

    mo.md(f"""
    ### Senoidal interactiva

    Ajusta los parametros para observar como cambia la senal:

    {f9}
    {amp9} """)
    return amp9, f9


@app.cell
def _(amp9, f9, np, plt):
    f9_muestreo = 44100

    #Cuanta duracion es 5 periodos? -> depende de la frecuencia (slider)
    duracion9 = 5.0 / f9.value
    N9 = int(f9_muestreo * duracion9)
    t9 = np.arange(N9) * (1/f9_muestreo)
    x9 = (amp9.value) * np.sin(2 * np.pi * f9.value * t9)

    fig9, ax9 = plt.subplots(figsize = (12, 4))
    ax9.plot(t9 * (10 ** 3), x9, 'b-', linewidth = 1.5)
    ax9.set_title(
        f"Senoidal: A = {amp9.value:.1f},"
        f"f = {f9.value} [Hz]"
    )
    ax9.set_xlabel("Tiempo [ms]")
    ax9.set_ylabel("Amplitud")
    ax9.set_ylim(-1.1, 1.1)
    ax9.grid(True, alpha = 0.3)
    ax9.axhline(y = 0, color = 'k', linewidth = 0.5)
    plt.tight_layout()
    fig9
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 10: Analisis de una senal

    Dado el siguiente array que simula una senal de audio (ya proporcionado), calcula e imprime:

    1. **Duracion** en segundos (asumiendo fs = 44100)
    2. **Amplitud pico** (valor absoluto maximo)
    3. **Valor RMS** (Root Mean Square): $\text{RMS} = \sqrt{\frac{1}{N} \sum_{n=0}^{N-1} |x[n]|^2}$
    4. **RMS en dBFS** (dB Full Scale, referencia = 1.0): $\text{dBFS} = 20 \log_{10}(\text{RMS})$
    5. **Factor de cresta** (Peak / RMS)

    Usa la senal generada en la celda de abajo.
    """)
    return


app._unparsable_cell(
    r"""
    # Senal de ejemplo: mezcla de senoidales con ruido
    np.random.seed(42)
    fs_ej10 = 44100
    duracion_ej10 = 2.0
    t_ej10 = np.arange(int(fs_ej10 * duracion_ej10)) / fs_ej10
    audio_ej10 = (0.5 * np.sin(2 * np.pi * 440 * t_ej10) 
                  0.3 * np.sin(2 * np.pi * 880 * t_ej10) +
                  0.05 * np.random.randn(len(t_ej10)))
    """,
    name="_"
)


@app.cell
def _(audio_ej10, fs_ej10, np, plt, t_ej10):
    #Duracion -> cantidad de muestras en total * (1/frec de muestreo)
    duracion10 = len(audio_ej10) * (1/fs_ej10)

    Amp10 = max(np.abs(audio_ej10))

    #root mean square -> square, mean, root
    RMS = np.sqrt(np.mean(audio_ej10 ** 2))

    #RMS -> dBFS
    dBFS = 20 * np.log10(RMS) if RMS > 0 else float('-inf')

    #Factor cresta
    FC = Amp10 / RMS

    #Analisis de la senal de prueba
    print(f"duracion de la senal -> {duracion10} [s]")
    print(f"amplitud -> {Amp10:.4f}")
    print(f"Valor RMS -> {RMS:.4f}")
    print(f"Valor dBFS -> {dBFS:.4f}")
    print(f"Factor Cresta -> {FC:.4f}")


    #Visualizacion de la senal de prueba
    fig10, ax10 = plt.subplots(figsize = (12, 4))
    ax10.plot(t_ej10 * (10 ** 3), audio_ej10, 'b-', linewidth = 1.5)
    ax10.set_title(f"Mezcla de senoidales con ruido")
    ax10.set_xlabel("Tiempo [ms]")
    ax10.set_ylabel("Amplitud")
    ax10.set_ylim(-1.1, 1.1)
    ax10.grid(True, alpha = 0.3)
    ax10.axhline(y = 0, color = 'k', linewidth = 0.5)
    plt.tight_layout()
    fig10
    return


if __name__ == "__main__":
    app.run()
