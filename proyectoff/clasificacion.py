from proyectoff.gestor_base_datos import DatabaseManager

class Ranking:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_score(self, player_id, new_score):
        self.db_manager.call_procedure('ActualizarPuntuacion', [player_id, new_score])

    def get_ranking(self):
        results = self.db_manager.call_procedure('ConsultarRanking')
        return results
