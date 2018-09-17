import json
from httplib import HTTPResponse

from sqlalchemy.sql.elements import or_

from models.generic_models import User
from orm.utils import SessionManger
from views.generic_views import View, Response
from render.utils import render_to_string


class UserLogged(View):

    template = '../templates/user_logged.html'

    def get(self):
        self.request.headers.getheader('Auth')
        users = SessionManger.session().query(User).all()
        context = {'users': users}
        render = self.render({context})
        return Response(render, status=200)


class UserSearch(View):

    def get(self):
        search_param = self.GET.get('param')[0]
        users = SessionManger.session().query(User).filter(or_(User.name == search_param, User.email == search_param))
        render = render_to_string('../templates/list_users.html', {'users': users})
        headers = {'Location': '/user-logged/'}
        return Response(render, status=301, headers=headers, data=search_param)


class UserLogin(View):

    template = '../templates/login_user.html'

    def get(self):
        render = self.render({})
        return Response(render, status=200)

    def post(self):
        query = {
            'username': self.POST.get('username')[0],
            'password': self.POST.get('password')[0]
        }
        user = SessionManger.session().query(User).filter_by(**query).first()
        if not user:
            render = self.render({})
            return Response(render, status=200)
        headers = {'Location': '/user-logged/', 'Auth': user.username}
        return Response('', status=301, headers=headers)


class ManageUser(View):
    template = '../templates/add_user.html'

    def get(self):
        render = self.render({})
        return Response(render, status=200)

    def post(self):

        user = User(
            username=self.POST.get('username')[0],
            name=self.POST.get('name')[0],
            email=self.POST.get('email')[0],
            country=self.POST.get('country')[0],
            password=self.POST.get('password')[0]
        )

        SessionManger.session().add(user)
        SessionManger.commit()

        render = render_to_string('../templates/user_registred.html', {'user': user})
        return Response(render, status=301)
