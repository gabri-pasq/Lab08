import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.nercSelezionato : model.Nerc
        self._idMap = {}
        self.fillIDMap()

    def handleWorstCase(self, e):
        self._view._txtOut.clean()
        self._view._txtOut.controls.append(ft.Text('CARICAMENTO...'))
        self._view.update_page()
        self._model.loadEvents(self.nercSelezionato)
        self._model.worstCase(self.nercSelezionato,self._view._txtYears.value, self._view._txtHours.value)
        self._view._txtOut.clean()
        self._view._txtOut.controls.append(ft.Text(f'Totale persone colpite: {self._model.maxPersone}'))
        lista = self._model.risultsto
        for e in lista:
            self._view._txtOut.controls.append(ft.Text(str(e)))
        self._view.update_page()


    def fillDD(self):
        nercList = self._model.listNerc
        for n in nercList:
            self._view._ddNerc.options.append(
                ft.dropdown.Option(key=n.id, text=n.value, data=n, on_click=self.readObjectNerc))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v

    def readObjectNerc(self,e):
        self.nercSelezionato = e.control.data
        #print(self.nercSelezionato)
