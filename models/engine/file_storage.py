#!/usr/bin/python3
"""File storage"""

class Filestorage:
    """Constructor"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return Filestorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        return Filestorage.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(Filestorage.__file_path, 'w' encoding= 'utf-8') as fname:
            n_dict = {k:obj.to_dict() for k in
                    Filestorage.__objects.items()}
            json.dump(n_dict, fname)

    def reload(self):
        """ Reload the file """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                l_json = json.load(fname)
                for k, val in l_json.items():
                    FileStorage.__objects[k] = eval(
                        val['__class__'])(**val)
