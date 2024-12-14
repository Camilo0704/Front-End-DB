from proyectoff.gestor_base_datos import DatabaseManager
from proyectoff.grafo import Graph

class World:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.graph = Graph()

    def register_world(self, graph):
        self.db_manager.call_procedure('RegistrarMundo', [graph])

    def modify_world(self, world_id, graph):
        self.db_manager.call_procedure('ModificarMundo', [world_id, graph])

    def delete_world(self, world_id):
        self.db_manager.call_procedure('EliminarMundo', [world_id])

    def get_world(self, world_id):
        results = self.db_manager.call_procedure('ConsultarMundo', [world_id])
        return results

    def get_all_worlds(self):
        results = self.db_manager.call_procedure('ConsultarTodosLosMundos')
        return results

    def insert_connection(self, world_id, location1, location2, weight):
        self.db_manager.call_procedure('InsertarConexion', [world_id, location1, location2, weight])
        self.graph.add_edge(location1, location2, weight)

    def find_shortest_path(self, start, end):
        return self.graph.dijkstra(start, end)
