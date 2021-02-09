from flask_restful import fields, marshal_with

from src.dao.publish_dao import PublishDao
from src.models.publish import Publish
from src.resources.base_resource import BaseResource


class PublishResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "id_pool": fields.Integer,
        "id_channel": fields.Integer,
        "initial_date": fields.datetime,
        "final_date": fields.datetime,
        "is_activate": fields.Boolean
    }

    def __init__(self):
        self.__dao = PublishDao()
        self.__model_type = Publish

        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)
