class Analisi:

    # Valori di riferimento
    VALORI_NORMA = {
        "glicemia":    (70, 100),    # mg/dL
        "colesterolo": (0, 200),     # mg/dL
        "emocromo":    (4.5, 11.0),  # x10^3/uL (globuli bianchi)
        "trigliceridi":(0, 150),     # mg/dL
        "creatinina":  (0.6, 1.2),   # mg/dL
    }

    def __init__(self, tipo, risultato):
        self.tipo = tipo.lower()
        self.risultato = risultato

    def valuta(self):

        minimo, massimo = self.VALORI_NORMA[self.tipo]

        if self.risultato < minimo:
            esito = "Valore BASSO"
        elif self.risultato > massimo:
            esito = "Valore ALTO "
        else:
            esito = "Valore Nella norma"

        return (
            f"[{self.tipo.capitalize()}] "
            f"Valore: {self.risultato} | "
            f"Norma: {minimo}-{massimo} | "
            f"Esito: {esito}"
        )

    def __str__(self):
        return self.valuta()
