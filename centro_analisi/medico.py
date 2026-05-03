class Medico:

    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        if(paziente):
            print(
                f"Il medico: {self.nome} {self.cognome} ({self.specializzazione}) "
                f"sta visitando: {paziente.nome} {paziente.cognome}"
            )
        else:
            print(f"Il medico: {self.nome} {self.cognome} ({self.specializzazione})" 
                  f"è libero al momento")

    def __str__(self):
        return f"Dott. {self.nome} {self.cognome} – {self.specializzazione}"