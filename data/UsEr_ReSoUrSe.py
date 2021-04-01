from flask_restful import Resource
from data import db_session
from data.user_model import User
from flask import jsonify


class UsersResourse(Resource):
    def get(self, user_id):
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('surname',
                  'name',
                  'age',
                  'position',
                  )
        )})
