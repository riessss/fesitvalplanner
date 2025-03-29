from flask_jwt_extended import jwt_required

@app.route('/')
@jwt_required()
def test():
    return 'test'