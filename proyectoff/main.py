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

def player_menu(player_manager):
    while True:
        print("\nMenú de Jugadores:")
        print("1. Registrar jugador")
        print("2. Modificar jugador")
        print("3. Eliminar jugador")
        print("4. Consultar jugador")
        print("5. Consultar todos los jugadores")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                username = input("Nombre de usuario: ").strip()
                level = int(input("Nivel: ").strip())
                score = int(input("Puntuación: ").strip())
                team_id = int(input("ID del equipo: ").strip())
                player_manager.register_player(username, level, score, team_id)
            elif opcion == "2":
                player_id = int(input("ID del jugador: ").strip())
                username = input("Nombre de usuario: ").strip()
                level = int(input("Nivel: ").strip())
                score = int(input("Puntuación: ").strip())
                team_id = int(input("ID del equipo: ").strip())
                player_manager.modify_player(player_id, username, level, score, team_id)
            elif opcion == "3":
                player_id = int(input("ID del jugador: ").strip())
                player_manager.delete_player(player_id)
            elif opcion == "4":
                player_id = int(input("ID del jugador: ").strip())
                print(player_manager.get_player(player_id))
            elif opcion == "5":
                players = player_manager.get_all_players()
                for player in players:
                    print(player)
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

def world_menu(world_manager):
    while True:
        print("\nMenú de Mundos:")
        print("1. Registrar mundo")
        print("2. Modificar mundo")
        print("3. Eliminar mundo")
        print("4. Consultar mundo")
        print("5. Consultar todos los mundos")
        print("6. Insertar conexión en mundo")
        print("7. Encontrar ruta más corta en mundo")
        print("8. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                graph = input("Grafo (JSON): ").strip()
                world_manager.register_world(graph)
            elif opcion == "2":
                world_id = int(input("ID del mundo: ").strip())
                graph = input("Grafo (JSON): ").strip()
                world_manager.modify_world(world_id, graph)
            elif opcion == "3":
                world_id = int(input("ID del mundo: ").strip())
                world_manager.delete_world(world_id)
            elif opcion == "4":
                world_id = int(input("ID del mundo: ").strip())
                print(world_manager.get_world(world_id))
            elif opcion == "5":
                worlds = world_manager.get_all_worlds()
                for world in worlds:
                    print(world)
            elif opcion == "6":
                world_id = int(input("ID del mundo: ").strip())
                location1 = input("Ubicación 1: ").strip()
                location2 = input("Ubicación 2: ").strip()
                weight = int(input("Peso: ").strip())
                world_manager.insert_connection(world_id, location1, location2, weight)
            elif opcion == "7":
                start = input("Ubicación de inicio: ").strip()
                end = input("Ubicación de destino: ").strip()
                route, distance = world_manager.find_shortest_path(start, end)
                print(f"Ruta más corta de {start} a {end}: {route} con distancia {distance}")
            elif opcion == "8":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

def inventory_menu(inventory_manager):
    while True:
        print("\nMenú de Inventario:")
        print("1. Registrar ítem en inventario")
        print("2. Modificar ítem en inventario")
        print("3. Eliminar ítem en inventario")
        print("4. Consultar ítem en inventario")
        print("5. Consultar inventario de jugador")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                player_id = int(input("ID del jugador: ").strip())
                item_key = input("Clave del ítem: ").strip()
                item_description = input("Descripción del ítem: ").strip()
                inventory_manager.register_item(player_id, item_key, item_description)
            elif opcion == "2":
                inventory_id = int(input("ID del inventario: ").strip())
                item_key = input("Clave del ítem: ").strip()
                item_description = input("Descripción del ítem: ").strip()
                inventory_manager.modify_item(inventory_id, item_key, item_description)
            elif opcion == "3":
                inventory_id = int(input("ID del inventario: ").strip())
                item_key = input("Clave del ítem: ").strip()
                inventory_manager.delete_item(inventory_id, item_key)
            elif opcion == "4":
                inventory_id = int(input("ID del inventario: ").strip())
                print(inventory_manager.get_item(inventory_id))
            elif opcion == "5":
                player_id = int(input("ID del jugador: ").strip())
                print(inventory_manager.get_inventory(player_id))
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

def match_menu(match_manager):
    while True:
        print("\nMenú de Partidas:")
        print("1. Registrar partida")
        print("2. Modificar partida")
        print("3. Eliminar partida")
        print("4. Consultar partida")
        print("5. Consultar todas las partidas")
        print("6. Listar partidas entre fechas")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                date = input("Fecha (YYYY-MM-DD): ").strip()
                team1 = int(input("ID del equipo 1: ").strip())
                team2 = int(input("ID del equipo 2: ").strip())
                result = input("Resultado: ").strip()
                world_id = int(input("ID del mundo: ").strip())
                match_manager.register_match(date, team1, team2, result, world_id)
            elif opcion == "2":
                match_id = int(input("ID de la partida: ").strip())
                date = input("Fecha (YYYY-MM-DD): ").strip()
                team1 = int(input("ID del equipo 1: ").strip())
                team2 = int(input("ID del equipo 2: ").strip())
                result = input("Resultado: ").strip()
                world_id = int(input("ID del mundo: ").strip())
                match_manager.modify_match(match_id, date, team1, team2, result, world_id)
            elif opcion == "3":
                match_id = int(input("ID de la partida: ").strip())
                match_manager.delete_match(match_id)
            elif opcion == "4":
                match_id = int(input("ID de la partida: ").strip())
                print(match_manager.get_match(match_id))
            elif opcion == "5":
                matches = match_manager.get_all_matches()
                for match in matches:
                    print(match)
            elif opcion == "6":
                start_date = input("Fecha de inicio (YYYY-MM-DD): ").strip()
                end_date = input("Fecha de fin (YYYY-MM-DD): ").strip()
                matches = match_manager.list_matches_between_dates(start_date, end_date)
                for match in matches:
                    print(match)
            elif opcion == "7":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

def team_menu(team_manager):
    while True:
        print("\nMenú de Equipos:")
        print("1. Registrar equipo")
        print("2. Modificar equipo")
        print("3. Eliminar equipo")
        print("4. Consultar equipo")
        print("5. Consultar todos los equipos")
        print("6. Calcular estadísticas de equipos")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                team_name = input("Nombre del equipo: ").strip()
                statistics = input("Estadísticas (JSON): ").strip()
                team_manager.register_team(team_name, statistics)
            elif opcion == "2":
                team_id = int(input("ID del equipo: ").strip())
                team_name = input("Nombre del equipo: ").strip()
                statistics = input("Estadísticas (JSON): ").strip()
                team_manager.modify_team(team_id, team_name, statistics)
            elif opcion == "3":
                team_id = int(input("ID del equipo: ").strip())
                team_manager.delete_team(team_id)
            elif opcion == "4":
                team_id = int(input("ID del equipo: ").strip())
                print(team_manager.get_team(team_id))
            elif opcion == "5":
                teams = team_manager.get_all_teams()
                for team in teams:
                    print(team)
            elif opcion == "6":
                team_manager.calculate_statistics()
                for team_name, team_data in team_manager.teams.items():
                    print(f"Equipo: {team_name}")
                    print(f"Promedio de puntuación: {team_data['statistics']['average_score']}")
                    print(f"Promedio de nivel: {team_data['statistics']['average_level']}")
            elif opcion == "7":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

def main():
    db_manager = DatabaseManager()

    player_manager = Player(db_manager)
    world_manager = World(db_manager)
    inventory_manager = Inventory(db_manager)
    match_manager = Match(db_manager)
    ranking_manager = Ranking(db_manager)
    team_manager = Team(db_manager)

    while True:
        print("\nMenú Principal:")
        print("1. Gestión de Jugadores")
        print("2. Gestión de Mundos")
        print("3. Gestión de Inventario")
        print("4. Gestión de Partidas")
        print("5. Gestión de Equipos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                player_menu(player_manager)
            elif opcion == "2":
                world_menu(world_manager)
            elif opcion == "3":
                inventory_menu(inventory_manager)
            elif opcion == "4":
                match_menu(match_manager)
            elif opcion == "5":
                team_menu(team_manager)
            elif opcion == "6":
                db_manager.close()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
