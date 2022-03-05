from datetime import datetime
import models
import uuid

class BaseModel(self, *args, **kwargs):
    def __init__(self):
        if len(kwargs) != 0:
            if key == "created_at" or key == "updated_at":
                self.__dict__[key] = datetime.strptime(
                                        value, "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
