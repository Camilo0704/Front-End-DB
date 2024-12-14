from proyectoff.gestor_base_datos import DatabaseManager

class Team:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.teams = {}

    def register_team(self, team_name, statistics):
        self.db_manager.call_procedure('RegistrarEquipo', [team_name, statistics])
        self.teams[team_name] = {'statistics': statistics, 'players': []}

    def modify_team(self, team_id, team_name, statistics):
        self.db_manager.call_procedure('ModificarEquipo', [team_id, team_name, statistics])
        if team_name in self.teams:
            self.teams[team_name]['statistics'] = statistics

    def delete_team(self, team_id):
        self.db_manager.call_procedure('EliminarEquipo', [team_id])
        for team_name in list(self.teams.keys()):
            if self.teams[team_name]['id'] == team_id:
                del self.teams[team_name]

    def get_team(self, team_id):
        results = self.db_manager.call_procedure('ConsultarEquipo', [team_id])
        if results:
            row = results[0]
            return {
                'ID_Equipo': row[0],
                'Nombre_Equipo': row[1],
                'Estadisticas': row[2]
            }
        return None

    def get_all_teams(self):
        results = self.db_manager.call_procedure('ConsultarTodosLosEquipos')
        return results

    def add_player_to_team(self, team_name, player):
        if team_name not in self.teams:
            self.teams[team_name] = {'statistics': {}, 'players': []}
        self.teams[team_name]['players'].append(player)

    def calculate_statistics(self):
        for team_name, team_data in self.teams.items():
            total_score = sum(player['score'] for player in team_data['players'])
            total_level = sum(player['level'] for player in team_data['players'])
            num_players = len(team_data['players'])
            if num_players > 0:
                team_data['statistics']['average_score'] = total_score / num_players
                team_data['statistics']['average_level'] = total_level / num_players
            else:
                team_data['statistics']['average_score'] = 0
                team_data['statistics']['average_level'] = 0

        # Mostrar estadísticas calculadas
        for team_name, team_data in self.teams.items():
            print(f"Equipo: {team_name}")
            print(f"Promedio de puntuación: {team_data['statistics']['average_score']}")
            print(f"Promedio de nivel: {team_data['statistics']['average_level']}")
