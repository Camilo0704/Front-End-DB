from proyectoff.gestor_base_datos import DatabaseManager

class Inventory:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.inventories = {}

    def register_item(self, player_id, item_key, item_description):
        self.db_manager.call_procedure('RegistrarItemInventario', [player_id, item_key, item_description])
        if player_id not in self.inventories:
            self.inventories[player_id] = {}
        self.inventories[player_id][item_key] = item_description

    def modify_item(self, inventory_id, item_key, item_description):
        self.db_manager.call_procedure('ModificarItemInventario', [inventory_id, item_key, item_description])
        for player_id, inventory in self.inventories.items():
            if item_key in inventory:
                inventory[item_key] = item_description

    def delete_item(self, inventory_id, item_key):
        self.db_manager.call_procedure('EliminarItemInventario', [inventory_id])
        for player_id, inventory in self.inventories.items():
            if item_key in inventory:
                del inventory[item_key]

    def get_item(self, inventory_id):
        results = self.db_manager.call_procedure('ConsultarItemInventario', [inventory_id])
        return results

    def get_inventory(self, player_id):
        if player_id not in self.inventories:
            results = self.db_manager.call_procedure('ConsultarInventarioJugador', [player_id])
            self.inventories[player_id] = {item['Clave_Item']: item['Descripcion_Item'] for item in results}
        return self.inventories[player_id]
