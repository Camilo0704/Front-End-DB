from proyectoff.gestor_base_datos import DatabaseManager
from proyectoff.equipo import Team

class Player:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.team_manager = Team(db_manager)

    def register_player(self, username, level, score, team_id):
        self.db_manager.call_procedure('RegistrarJugador', [username, level, score, team_id])
        player = {'username': username, 'level': level, 'score': score, 'team_id': team_id}
        team_name = self.get_team_name_by_id(team_id)
        if team_name:
            self.team_manager.add_player_to_team(team_name, player)

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

    def get_team_name_by_id(self, team_id):
        team = self.team_manager.get_team(team_id)
        return team['Nombre_Equipo'] if team else None
