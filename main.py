import flet as ft
from views.routes import router
from views.app_bar import NavBar
from core.style import *

def main(page: ft.Page):

    page.theme_mode = "dark"
    page.window_center()
    page.window_width = windows_width
    page.window_height = windows_height
    page.window_resizable = False
    page.window_maximizable = False
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/')

ft.app(target=main, assets_dir="assets")



# if not keys.login or not keys.password:
#     print('Please fill correct credentials in keys.py')
#     exit()
#
# cl = Client()
# cl.username = "Fake user"
# user_id = ""
#
#
# def LoginInstagram():
#     #Get followers and following dicts from instagram
#     cl.login(keys.login, keys.password)
#     print('Login to: ', cl.username)
#     user_id = cl.user_id
#     _followers = cl.user_followers(str(user_id), True, amount=0)
#     _following = cl.user_following(str(user_id), True, amount=0)
#     return _followers, _following
#
#
# followers = fake.GetFollowers()
# following = fake.GetFollowing()
#
# print('UserName:', cl.username)
# print('Followers:', len(followers))
# print('Following:', len(following))
#
# # Generate dict of unfollowers (key: UserShort class)
# unfollow = {k: v for k, v in following.items() if k not in followers}
#
# string = ''
#
# for k in unfollow:
#     string += following.get(k).username + ', '
#
# string = string.rstrip(', ')
#
# print('Unfollows:', string)
