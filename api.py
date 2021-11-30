#!/usr/bin/env python
import requests
from config import * 
from models import Task, User
import os


@app.route('/api/post_task', methods=['POST'])
@auth.login_required
def post_task():
    # записывать исполнителям и принимать исполнителей ?
    strtask = request.json.get('task')
    username = request.json.get('username')
    user = User.query.filter_by(username=username).first()
    task = Task(task_text=strtask, user_id=user.id)
    db.session.add(task)
    db.session.commit()
    return jsonify({"resp":"resp"})

@app.route('/api/get_tasks', methods=['GET'])
@auth.login_required
def get_task():
    # проверить роль ?
    # если спрашиваем таски у родителя то перебираем все таски детей из поля и возвращаем не одинаковые
    # если ребенок то просто достать по связи 
    username = request.json.get('username')
    user = User.query.filter_by(username=username).first()
    user_idd = user.id
    tasks = Task.query.filter_by(user_id=user_idd).all()
    jsonretcal = {username: []}
    for i in tasks:
        jsonretcal.get(username).append(i.task_text)
    return jsonify(jsonretcal)

@app.route('/api/del_task', methods=['POST'])
@auth.login_required
def del_task():
    # атрибут удаления ?
    strtask = request.json.get('task')
    username_del = request.json.get('username')
    user = User.query.filter_by(username=username_del).first()
    if user.role == 'parent':
        childs_list = user.childs
        childs_list = childs_list.split(' ')
        for child in childs_list:
            child_user = User.query.filter_by(username=child).first()
            task = Task.query.filter_by(task_text=strtask, user_id=child_user.id).first()
            db.session.delete(task)
    else:   
        task = Task.query.filter_by(task_text=strtask, user_id=user.id).first()
        db.session.delete(task)
    db.session.commit()
    return jsonify({"data":"task deleted"})
    
# регистрация пользователя 
@app.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')
    if username is None or password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)    # existing user
    user = User(username=username, role=role)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201,
            {'Location': url_for('get_user', id=user.id, _external=True)})


@app.route('/api/add_childs', methods=['POST'])
@auth.login_required
def add_childs():
    db.session.query(User).filter(User.id == g.user.id).\
        update({User.childs: request.json.get('childs')})
    return jsonify({"response":"true"})


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@app.route('/api/users/<int:id>')
def get_user(id):
    # вернуть всю инфу ? 
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username,
                    'chids': user.childs})


# @app.route('/api/token')
# @auth.login_required
# def get_auth_token():
#     token = g.user.generate_auth_token(86400)
#     return jsonify({'token': token.decode('ascii'), 'duration': 86400})

if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)
