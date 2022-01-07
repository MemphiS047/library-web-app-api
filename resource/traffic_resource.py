import random
from flask_restful import Resource

class TrafficAPI(Resource):
    def post(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        lib1_traffic = random.randint(0, 100)
        lib2_traffic = random.randint(0, 100)
        lib3_traffic = random.randint(0, 100)
        return {
            "lib1_traffic" : lib1_traffic,
            "lib2_traffic" : lib2_traffic,
            "lib3_traffic" : lib3_traffic, }, 201, {'Access-Control-Allow-Origin': '*'}


class TrafficCompAPI(Resource):
    def get(self):
        comp1_available = random.randint(0, 3)
        comp2_available = random.randint(0, 3)
        comp3_available = random.randint(0, 3)
        return {
            "comp1_available" : comp1_available,
            "comp2_available" : comp2_available,
            "comp3_available" : comp3_available
        }