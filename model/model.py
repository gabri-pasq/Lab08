import copy
from datetime import datetime
from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()
        self.nPersone = None
        self.maxYear = 0
        self.maxHour = 0
        self.risultsto = []
        self.maxPersone = -1

    def worstCase(self, nerc, maxY, maxH):
        print('entro model-worstCase')
        self.maxYear = int(maxY)
        self.maxHour = int(maxH)
        self.risultsto = []
        self.maxPersone = -1
        print(f'lista iniziale: {self._listEvents}')
        self.ricorsione([], 0)
        print(self.risultsto)
        print(self.maxPersone)
        #print(f'lista iniziale: {self._listEvents}')
        # TO FILL

    def ricorsione(self, parziale, indice):
        if indice == len(self._listEvents):
            return
        else:
            for i in range(indice, len(self._listEvents)):
                parziale.append(self._listEvents[i])
                #print(parziale)
                self.controlli(parziale)
                indice += 1
                self.ricorsione(parziale, indice)
                parziale.pop()

    def controlli(self, lista):
        ore = 0
        nPersone = 0
        for evento in lista:
            o = evento.nOre()
            ore += o
            nPersone += evento._customers_affected
        #print(lista[-1].anno() - lista[0].anno())
        #print( nPersone)
        #print(ore)
        if ore <= self.maxHour  and (lista[-1].anno() - lista[0].anno()) <= self.maxYear and nPersone > self.maxPersone:
            self.maxPersone = nPersone
            self.risultsto = copy.deepcopy(lista)

    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()

    @property
    def listNerc(self):
        return self._listNerc
