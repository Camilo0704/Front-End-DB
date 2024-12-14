from proyectoff.gestor_base_datos import DatabaseManager

class Match:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def register_match(self, date, team1, team2, result, world_id):
        self.db_manager.call_procedure('RegistrarPartida', [date, team1, team2, result, world_id])

    def modify_match(self, match_id, date, team1, team2, result, world_id):
        self.db_manager.call_procedure('ModificarPartida', [match_id, date, team1, team2, result, world_id])

    def delete_match(self, match_id):
        self.db_manager.call_procedure('EliminarPartida', [match_id])

    def get_match(self, match_id):
        results = self.db_manager.call_procedure('ConsultarPartida', [match_id])
        return results

    def get_all_matches(self):
        results = self.db_manager.call_procedure('ConsultarTodasLasPartidas')
        return results
