from views.custom_views import UserListView, UserLogin, ManageUser

url_paths = {
    '/list-user/': UserListView,
    '/user-login/': UserLogin,
    '/manage-user/': ManageUser,
}
