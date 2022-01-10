from flask import request
from flask_restful import Resource
from serpapi import GoogleSearch

class GoogleScholarAPI(Resource):
    def get(self):
        result = {

        }
        search_string = request.args.get('searchString')
        print("SEARCH STRING FOR JOURNA:", search_string)
        params = {
            "engine": "google_scholar",
            "q": f"{search_string}",
            "api_key": "8a45032b94cbcf6cbae59f7a8164af4f611fb195377596d1a5d570bfd6276beb"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        result["queryLst"] = results['organic_results']
        return result, 201, {'Access-Control-Allow-Origin': '*'}
