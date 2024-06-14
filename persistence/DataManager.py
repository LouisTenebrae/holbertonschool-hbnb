import json
class DataManager():
    """DataManager class"""

    storage = {
        "User": {},
        "City": {},
        "Amenity": {},
        "Place": {},
        "Review": {},
    }
    objects = {}

    @classmethod
    def save(self, entity, data_type):
        """save data"""
        if data_type not in self.storage:
            raise ValueError(f"Invalid data type: {data_type}")
        self.objects[entity.id] = entity
        self.storage[data_type][entity.id] = entity.to_dict()
        with open("file.json", "w") as f:
            json.dump(self.storage, f)


    @classmethod
    def get(self, entity_id, entity_type):
        """Get the data for a given entity"""
        if entity_type not in self.storage:
            raise ValueError(f"Invalid data type: {entity_type}")
        return self.objects[entity_id]

    @classmethod
    def update(self, entity, entity_type):
        """Update the data for a given entity"""
        if entity_type not in self.storage:
            raise ValueError(f"Invalid data type: {entity_type}")
        if entity in self.storage[entity_type]:
            self.storage[entity_type][entity] = entity
            self.objects[entity]= entity
        else:
            raise ValueError(f"Entity {entity} does not exist")

    @classmethod
    def delete(self, entity_id, entity_type):
        """Delete a entity from the database"""
        if entity_type not in self.storage:
            raise ValueError(f"Invalid data type: {entity_type}")
        if entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            with open("file.json", "w", encoding="utf-8") as file:
                json.dump(self.storage, file)
                del self.objects[entity_id]
        else:
            raise ValueError(f"Entity {entity_type} does not exist")

    @classmethod
    def all_entities(self, entity_type):
        """Returns a list of all entities"""
        if entity_type not in self.storage:
            raise ValueError(f"Invalid data type: {entity_type}")
        return list(self.storage[entity_type].values())

    @classmethod
    def reload(self, entity, entity_type):
        """Retrieve data from storage"""
        if entity_type not in self.storage:
            raise ValueError(f"Invalid data type: {entity_type}")
        if entity not in self.storage[entity_type]:
            return None
        return self.storage[entity_type][entity]
