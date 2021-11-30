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
    children = request.json.get('children')
    user = User.query.filter_by(username=username).first()
    if user.role == 'parent' and children != 'all':
        for child in children:
            child_user = User.query.filter_by(username=child).first()
            task = Task(task_text=strtask, user_id=child_user.id)
            db.session.add(task)
            db.session.commit()
    elif user.role == 'parent' and children == 'all':
        children_list = user.children.split(' ')
        for child in children_list:
            child_user = User.query.filter_by(username=child).first()
            task = Task(task_text=strtask, user_id=child_user.id)
            db.session.add(task)
            db.session.commit()
    else: 
        return jsonify({"data":"дети не могут добавлять таск"}) 
    return jsonify({"resp":"resp"})

@app.route('/api/get_tasks', methods=['GET'])
@auth.login_required
def get_task():
    # если спрашиваем таски у родителя то перебираем все таски детей из поля и возвращаем не одинаковые
    # если ребенок то просто достать по связи 
    username = request.json.get('username')
    user = User.query.filter_by(username=username).first()
    ret_tasks = set()
    if user.role == 'parent':
        for child in user.children.split(' '):
            user_child = User.query.filter_by(username=child).first()
            child_tasks = Task.query.filter_by(user_id=user_child.id).all()
            for t in child_tasks:
                ret_tasks.add(t.task_text)
    elif user.role == 'child':
        tasks = Task.query.filter_by(user_id=user.id).all()
        for t in tasks:
            ret_tasks.add(t.task_text)
    return jsonify({"tasks": list(ret_tasks)})

@app.route('/api/get_children', methods=['GET'])
@auth.login_required
def get_children():
    if g.user.role == 'child':
        return jsonify({"data":"вы ребенок"})
    else:
        children = []
        for child in g.user.children.split(' '):
            children.append(child)
        return jsonify({"children":children})


@app.route('/api/del_task', methods=['POST'])
@auth.login_required
def del_task():
    # атрибут удаления ?
    strtask = request.json.get('task')
    username_del = request.json.get('username')
    user = User.query.filter_by(username=username_del).first()
    if user.role == 'parent':
        children_list = user.children
        children_list = children_list.split(' ')
        for child in children_list:
            child_user = User.query.filter_by(username=child).first()
            task = Task.query.filter_by(task_text=strtask, user_id=child_user.id).first()
            db.session.delete(task)
    else:   
        task = Task.query.filter_by(task_text=strtask, user_id=user.id).first()
        db.session.delete(task)
    db.session.commit()
    return jsonify({"data":"task deleted"})
    
# регистрация пользователя 
@app.route('/api/register', methods=['POST'])
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


@app.route('/api/add_children', methods=['POST'])
@auth.login_required
def add_children():
    # удаление ??
    # добавление к существующим
    if g.user.role == 'child':
        return jsonify({"response": "у детей нет детей"})
    else:
        children = g.user.children.split(' ')
        try:
            children.remove("None")
        except:
            pass
        new_children = request.json.get('children')
        for child in new_children:
            children.append(child)
        children = " ".join(child for child in children)
        db.session.query(User).filter(User.id == g.user.id).\
            update({User.children: children})
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
                    'children': user.children})


# @app.route('/api/token')
# @auth.login_required
# def get_auth_token():
#     token = g.user.generate_auth_token(86400)
#     return jsonify({'token': token.decode('ascii'), 'duration': 86400})

if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)
