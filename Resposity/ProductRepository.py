import requests as req
import json
from config import URL_ENDPOINT

from Resposity.IRepository import IRepository
from Common.Constant import Constant
from Common.Exception.NotFoundException import NotFoundException

class ProductRepository(IRepository):
    def __init__(self):
        self.URL = URL_ENDPOINT + "/products"

    def getAll(self):
        res = req.get(self.URL)

        if (res.status_code == 200):
            return json.loads(res.content)
        else:
            return None
            
    def getById(self, id = None):
        if (id):
            try:
                res = req.get(self.URL + str(id))

                if (req.status_codes == Constant.OK):
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
                created = req.post(self.URL, data)

                if (created == Constant.OK):
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
                    update = req.put(self.URL + str(id), data)
                    
                    if (update.status_code == Constant.OK):
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
        if (id):
            try:
                product = self.getById(id)

                if (product):
                    deleted = req.delete(self.URL + str(id))

                    if (deleted.status_code == Constant.OK):
                        return json.loads(deleted.content)
                    else:
                        return False
                else:
                    return False
            except Exception:
                return False
        else:
            return False