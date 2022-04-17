class Vehicul:
    def __init__(self, numar_roti: int, numar_usi: int, numar_locuri: int, capacitate_rezervor: int,
                 capacitate_portbagaj: int,
                 dimensiuni_lungime: int, dimensiuni_latime: int, dimensiuni_inaltime: int, consum_urban: int,
                 consum_extraurban: int,
                 consum_mixt: int):
        self.numar_roti = numar_roti
        self.numar_usi = numar_usi
        self.numar_locuri = numar_locuri
        self.capacitate_rezervor = capacitate_rezervor
        self.capacitate_portbagaj = capacitate_portbagaj
        self.dimensiuni_lungime = dimensiuni_lungime
        self.dimensiuni_latime = dimensiuni_latime
        self.dimensiuni_inaltime = dimensiuni_inaltime
        self.consum_urban = consum_urban
        self.consum_extraurban = consum_extraurban
        self.consum_mixt = consum_mixt


class Automobil(Vehicul):
    def __init__(self, vopsea_metalizata: bool, aer_conditionat: bool, sistem_de_franare: str, airbag_sofer: bool,
                 faruri_dublu_optice: bool):
        self.vopsea_metalizata = vopsea_metalizata
        self.aer_conditionat = aer_conditionat
        self.sistem_de_franare = sistem_de_franare
        self.airbag_sofer = airbag_sofer
        self.faruri_dublu_optice = faruri_dublu_optice


class Motor(Vehicul):
    def __init__(self, nr_cilindrii: int, nr_supape: int, putere_maxima: int, tip_carburant: str, tip_injectie: str,
                 catalizator: str, sistem_de_alimentare: str):
        self.nr_cilindrii = nr_cilindrii
        self.nr_supape = nr_supape
        self.putere_maxima = putere_maxima
        self.tip_carburant = tip_carburant
        self.tip_injectie = tip_injectie
        self.catalizator = catalizator
        self.sistem_de_alimentare = sistem_de_alimentare
