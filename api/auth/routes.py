from flask import Blueprint, request, jsonify
from models.users import User
from flask_jwt_extended import jwt_required, create_access_token, set_access_cookies, unset_jwt_cookies, get_jwt_identity

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.route('/login', methods=['POST'])
def login():
    post_data = request.get_json()

    username = post_data.get('username')
    password = post_data.get('password')

    #password hash

    user = User.query.filter_by(username=username).one_or_404()
    if not user or not user.check_password(password):
        return jsonify("wrong password"), 401

    access_token = create_access_token(identity=username)
    set_access_cookies(access_token)
    return jsonify(access_token=access_token)

@auth.route('/register')
def register():
    pass

@auth.route('/logout')
@jwt_required()
def logout():
    response = jsonify({"msg": "logout succesfull"})
    unset_jwt_cookies(response)
    return response

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identiy = get_jwt_identity()
    access_token = create_access_token(identity=identiy)
    response = jsonify(refresh=True)
    set_access_cookies(response, access_token)
    return response