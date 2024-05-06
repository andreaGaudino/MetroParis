from dataclasses import dataclass


@dataclass
class Connessione:
    _id_connessione : int
    _id_linea : int
    _id_stazP : int
    _id_stazA : int


    def id_connessione(self):
        return self._id_connessione

    def id_linea(self):
        return self._id_linea
    def id_stazP(self):
        return self._id_stazP
    def id_stazA(self):
        return self._id_stazA


    def __hash__(self):
        return hash(self._id_connessione)

    def __eq__(self, other):
        return self._id_connessione == other._id_connesione

    def __str__(self):
        return self._id_connessione
