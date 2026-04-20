import math

# defino funcion


def midi_a_hz(nota_midi: int) -> float:
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

    if not (0 <= nota_midi <= 127):
        raise ValueError(f"nota midi debe estar entre 0 y 127, se recibió {nota_midi}")
    return 440 * 2 ** ((nota_midi - 69) / 12)


# defino la funcion


def hz_a_midi(frecuencia: float) -> int:
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

    if frecuencia <= 0:
        raise ValueError(f"frecuencia debe ser mayor a 0 Hz, se recibió {frecuencia}")
    return round(69 + 12 * math.log2(frecuencia / 440))


# defino funcion rms


def calcular_rms(signal: list[float]) -> float:
    """
    Calcula el valor eficaz (RMS) de una senal

    Parameters
    ----------
    signal : list[float]
        Senal de entrada

    Returns
    -------
    float
        Valor RMS de la senal de entrada
    """

    if signal == []:
        v_rms = 0
    else:
        square = sum(i**2 for i in signal)
        mean = square / len(signal)
        root = math.sqrt(mean)
        v_rms = root

    return v_rms


if __name__ == "__main__":
    # prueba def midi_a_hz
    for m in [60, 69, 72, 48]:
        print(f"{m} -> {midi_a_hz(m):.2f}")

    # prueba def hz_a_midi
    for f in [440, 261.63, 880]:
        print(f"frecuencia : {f:.2f} -> midi : {hz_a_midi(f)}")

    # prueba def calcular_rms
    signal_prueba = [10, -10, 10, -10]
    print(f"RMS de la senal : {signal_prueba} -> {calcular_rms(signal_prueba): .2f}")
