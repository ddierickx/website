from flask import Response, render_template 

def wrap_json_response(fx):
        def helper():
                return Response(response=fx(), status=200, mimetype="application/json")
        return helper

def wrap_meta_list(fx):
        def helper(lst):
                json = fx(lst)  
                return render_template("utils/list.json", page=0, page_size=len(lst), size=len(lst), records_json=json)
        return helper
