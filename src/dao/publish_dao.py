from src.dao.base_dao import BaseDao
from src.models.publish import Publish


class PublishDao(BaseDao):
    def __init__(self):
        super().__init__(Publish)
