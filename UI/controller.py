import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        SightingList = self._model.listSighting
        #self._listShape = self._model.listShape

        for s in SightingList:
            if s.datetime.year not in self._listYear:
                self._listYear.append(s.datetime.year)

        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(a))

        """for s in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(s))"""

        self._view.update_page()

    def fillDDShape(self, e):
        self._view.ddshape.options.clear()
        self._view.update_page()
        year = float(self._view.ddyear.value)
        print(year)
        SightingList = self._model.listSighting
        for s in SightingList:
            if s.shape not in self._listShape and s.datetime.year == year:
                self._listShape.append(s.shape)
        for s in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(s))
        self._view.update_page()
        self._listShape.clear()




    def handle_graph(self, e):
        a = self._view.ddyear.value
        s = self._view.ddshape.value

        self._model.buildGraph(s, a)
        self._view.txt_result.controls.clear()
        self._view.update_page()
        #self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))

        for p in self._model.get_sum_weight_per_node():
            self._view.txt_result.controls.append(ft.Text(f"Nodo {p[0]}, somma pesi su archi ={p[1]}"))

        self._view.update_page()
    def handle_path(self, e):
        pass