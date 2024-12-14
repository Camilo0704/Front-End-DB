import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from proyectoff.gestor_base_datos import DatabaseManager
from proyectoff.jugador import Player
from proyectoff.mundo import World
from proyectoff.inventario import Inventory
from proyectoff.partida import Match
from proyectoff.clasificacion import Ranking
from proyectoff.equipo import Team

def main():
    db_manager = DatabaseManager()

    player_manager = Player(db_manager)
    world_manager = World(db_manager)
    inventory_manager = Inventory(db_manager)
    match_manager = Match(db_manager)
    ranking_manager = Ranking(db_manager)
    team_manager = Team(db_manager)

    # Ejemplo de uso
    player_manager.register_player('NuevoJugador', 1, 100, 1)
    players = player_manager.get_all_players()
    for player in players:
        print(player)

    # Ejemplo de encontrar la ruta más corta
    world_manager.insert_connection(1, 'A', 'B', 1)
    world_manager.insert_connection(1, 'B', 'C', 2)
    world_manager.insert_connection(1, 'A', 'C', 4)
    route, distance = world_manager.find_shortest_path('A', 'C')
    print(f"Ruta más corta de A a C: {route} con distancia {distance}")

    db_manager.close()

if __name__ == "__main__":
    main()
