from flask import request

# Try block for Boolean values
def boolean_try(resource,attribute):
    try:
        resource = request.json[attribute] 
    except:
        resource = resource