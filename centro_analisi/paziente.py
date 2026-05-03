import numpy as np

class Paziente:

    def __init__(self, nome, cognome, codice_fiscale, eta, peso):
        self.nome           = nome
        self.cognome        = cognome
        self.codice_fiscale = codice_fiscale
        self.eta            = eta
        self.peso           = peso
        self.lista_analisi  = []    # tutti gli oggetti Analisi nel tempo

    def aggiungi_analisi(self, analisi):
        self.lista_analisi.append(analisi)

    def scheda_personale(self):
        tipi_unici = sorted(set(a.tipo for a in self.lista_analisi))
        tipi_str   = ", ".join(tipi_unici) if tipi_unici else "nessuna"
        return (
            f"\n{'='*50}\n"
            f"  SCHEDA PAZIENTE\n"
            f"{'='*50}\n"
            f"  Nome:           {self.nome} {self.cognome}\n"
            f"  Codice Fiscale: {self.codice_fiscale}\n"
            f"  Età:            {self.eta} anni\n"
            f"  Peso:           {self.peso} kg\n"
            f"  Analisi svolte: {tipi_str}\n"
            f"{'='*50}"
        )

    def _raggruppa_per_tipo(self):
        gruppi = {}
        for a in self.lista_analisi:
            if a.tipo not in gruppi:
                gruppi[a.tipo] = []
            gruppi[a.tipo].append(a.risultato)

        # converte ogni lista in array NumPy
        return {tipo: np.array(valori, dtype=float)
                for tipo, valori in gruppi.items()}

    def statistiche_analisi(self):

        if not self.lista_analisi:
            return f"  {self.nome} {self.cognome}: nessun risultato disponibile."

        righe = [f"\n  Statistiche analisi – {self.nome} {self.cognome}:"]

        for tipo, valori in self._raggruppa_per_tipo().items():
            righe.append(
                f"    {tipo.capitalize():<15} "
                f"valori: {valori}  |  "
                f"media: {np.mean(valori):.2f}  "
                f"min: {np.min(valori):.2f}  "
                f"max: {np.max(valori):.2f}  "
                f"std: {np.std(valori):.2f}"
            )

        return "\n".join(righe)

    def __str__(self):
        return f"Paziente: {self.nome} {self.cognome} (CF: {self.codice_fiscale})"