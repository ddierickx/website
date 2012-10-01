import json
from flask import Response, render_template 

def obj_to_json(obj):
	return json.dumps(obj, cls=new_alchemy_encoder(), check_circular=False)

def wrap_json_response(fx):
        def helper():
                return Response(response=fx(), status=200, mimetype="application/json")
        return helper

def wrap_meta_list(fx):
        def helper(lst):
                json = fx(lst)  
                return render_template("utils/list.json", page=0, page_size=len(lst), size=len(lst), records_json=json)
        return helper

from sqlalchemy.ext.declarative import DeclarativeMeta
def new_alchemy_encoder():
	_visited_objs = []
        class AlchemyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj.__class__, DeclarativeMeta):
                    # don't re-visit self
                    if obj in _visited_objs:
                        return None
                    _visited_objs.append(obj)

                    # an SQLAlchemy class
                    fields = {}
                    for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                        fields[field] = obj.__getattribute__(field)
                    # a json-encodable dict
                    return fields

                return json.JSONEncoder.default(self, obj)
        return AlchemyEncoder
