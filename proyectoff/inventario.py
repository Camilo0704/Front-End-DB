from proyectoff.gestor_base_datos import DatabaseManager

class Inventory:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def register_item(self, player_id, item_key, item_description):
        self.db_manager.call_procedure('RegistrarItemInventario', [player_id, item_key, item_description])

    def modify_item(self, inventory_id, item_key, item_description):
        self.db_manager.call_procedure('ModificarItemInventario', [inventory_id, item_key, item_description])

    def delete_item(self, inventory_id):
        self.db_manager.call_procedure('EliminarItemInventario', [inventory_id])

    def get_item(self, inventory_id):
        results = self.db_manager.call_procedure('ConsultarItemInventario', [inventory_id])
        return results

    def get_player_inventory(self, player_id):
        results = self.db_manager.call_procedure('ConsultarInventarioJugador', [player_id])
        return results
