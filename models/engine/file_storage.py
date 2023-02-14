# models/engine/file_storage.py
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            objects_dict = {obj.__class__.__name__ + "." + obj.id: obj.to_dict()
                            for obj in FileStorage.__objects.values()}
            json.dump(objects_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def close(self):
        self.reload()
        
    def get(self, cls, id):
    """Retrieve an object from the file storage by its ID"""
    key = '{}.{}'.format(cls.__name__, id)
    return self.__objects.get(key, None)

    def count(self, cls=None):
    """Count the number of objects in the file storage"""
    if cls:
        return sum(1 for obj in self.__objects.values() if type(obj) == cls)
    else:
        return len(self.__objects)

