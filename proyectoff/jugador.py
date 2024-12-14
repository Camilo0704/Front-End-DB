from proyectoff.gestor_base_datos import DatabaseManager

class Player:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def register_player(self, username, level, score, team_id):
        self.db_manager.call_procedure('RegistrarJugador', [username, level, score, team_id])

    def modify_player(self, player_id, username, level, score, team_id):
        self.db_manager.call_procedure('ModificarJugador', [player_id, username, level, score, team_id])

    def delete_player(self, player_id):
        self.db_manager.call_procedure('EliminarJugador', [player_id])

    def get_player(self, player_id):
        results = self.db_manager.call_procedure('ConsultarJugador', [player_id])
        return results

    def get_all_players(self):
        results = self.db_manager.call_procedure('ConsultarTodosLosJugadores')
        return results
