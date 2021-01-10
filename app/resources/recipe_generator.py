import requests

from flask_restplus.reqparse import request

from flask_restplus import Resource


class RecipeGenerator(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ingredients = None

    def get(self):

        self.parse_query_args()

        possible_recipies = self.query_data_source_for_possibly_recipies()

        return {'status': 'success'}, 200

    def parse_query_params(self):
        assert 'ingredients' in request.args, f"Request did not receive a 'ingredients' param. This is required."
        self.ingredients = request.args.get('ingredients').split(',')

    def query_data_source_for_possibly_recipies(self):

        return None

