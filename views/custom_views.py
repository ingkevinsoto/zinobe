from models.generic_models import User
from orm.utils import SessionManger
from views.generic_views import View
from render.utils import render_to_string


class UserListView(View):

    def get(self):
        users = [
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
            {'name': 'kevin', 'username':'eldelflow', 'last_name':'soto'},
        ]
        context = {'users': users}
        if self.request.headers.getheader('Auth') and self.request.headers.getheader('Auth') == 'True':
            pass
        render = render_to_string('../templates/list_user.html', context)
        return render, 200


class UserLogin(View):

    def get(self):
        render = render_to_string('../templates/login_user.html', {})
        return render, 200

    def post(self):
        query = {
            'username': self.POST.get('username')[0],
            'password': self.POST.get('password')[0]
        }
        user = SessionManger.session().query(User).filter_by(**query).first()
        if not user:
            render = render_to_string('../templates/login_user.html', {})
            return render, 200
        self.request.send_header('Auth', user.username)
        users = SessionManger.session().query(User).all()
        context = {
            'users': users,
            'user_log': user
        }
        self.request.send_header('Location', '/list-user/')
        render = render_to_string('../templates/user_logged.html', context)
        return render, 200


class ManageUser(View):

    def get(self):
        render = render_to_string('../templates/add_user.html', {})
        return render, 200

    def post(self):

        user = User(
            username=self.POST.get('username')[0],
            name=self.POST.get('name')[0],
            email=self.POST.get('email')[0],
            country=self.POST.get('country')[0],
            password=self.POST.get('password')[0]
        )
        user2 = User(
            username=self.POST.get('username')[0],
            name=self.POST.get('name')[0],
            email=self.POST.get('email')[0],
            country=self.POST.get('country')[0],
            password=self.POST.get('password')[0]
        )
        SessionManger.session().add(user)
        SessionManger.session().add(user2)
        SessionManger.commit()

        # our_user = get_session().query(User) # .filter_by(name='kevin').first()
        our_user = SessionManger.session().query(User).filter_by(name='kevin').first()
        print('#'*10)
        print(our_user)
        print('#'*10)
        render = render_to_string('../templates/user_logged.html', {})
        return render, 200
