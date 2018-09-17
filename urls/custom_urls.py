from views.custom_views import UserLogged, UserLogin, ManageUser, UserSearch

url_paths = {
    '/user-logged/': UserLogged,
    '/user-login/': UserLogin,
    '/manage-user/': ManageUser,
    '/user-search/': UserSearch,
}
