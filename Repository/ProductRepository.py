import requests as req
import json
from config import URL_ENDPOINT

from Repository.IRepository import IRepository
from Common.Constant import Constant
from Common.Exception.NotFoundException import NotFoundException

class ProductRepository(IRepository):
    def __init__(self):
        self.URL = URL_ENDPOINT + "/products"

    def getAll(self):
        res = req.get(self.URL)

        if (res.ok):
            return json.loads(res.content)
        else:
            return None
            
    def getById(self, id = None):
        if (id):
            try:
                res = req.get(self.URL + "/" + str(id))

                if (res.ok):
                    return json.loads(res.content)
                else:
                    return False
            except:
                return False
        else:
            return False
        
    def create(self, data = None):
        if (data):
            try:
                created = req.post(self.URL, json.dumps(data))

                if (created.ok):
                    return json.loads(created.content)
                else:
                    return False
            except:
                return False
        else:
            False

    def update(self, id, data = None):
        if (id):
            try:
                product = self.getById(id)

                if (product):
                    update = req.put(self.URL + "/" + str(id), data)
                    
                    if (update.ok):
                        return json.loads(update.content)
                    else:
                        return False
            except NotFoundException:
                return False
            else:
                return product
        else:
            return False

    def delete(self, id):
        if (id and isinstance(id, (int, float))):
            try:
                deleted = req.delete(self.URL + '/' + str(id))

                if (deleted.ok):
                    return json.loads(deleted.content)
                else:
                    return False
            except Exception:
                return False
        else:
            return False