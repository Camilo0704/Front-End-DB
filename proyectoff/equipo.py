from proyectoff.gestor_base_datos import DatabaseManager

class Team:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def register_team(self, team_name, statistics):
        self.db_manager.call_procedure('RegistrarEquipo', [team_name, statistics])

    def modify_team(self, team_id, team_name, statistics):
        self.db_manager.call_procedure('ModificarEquipo', [team_id, team_name, statistics])

    def delete_team(self, team_id):
        self.db_manager.call_procedure('EliminarEquipo', [team_id])

    def get_team(self, team_id):
        results = self.db_manager.call_procedure('ConsultarEquipo', [team_id])
        return results

    def get_all_teams(self):
        results = self.db_manager.call_procedure('ConsultarTodosLosEquipos')
        return results
