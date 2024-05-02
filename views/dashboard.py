from core.style import *
from flet import *
from core.client import *


class Dashboard(Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.content = Column(
            [
                Text(value='Панель управления'),
                Text(cl.username),
            ]
        )



#
#
# def LoginInstagram():
#     #Get followers and following dicts from instagram
#     cl.login(keys.login, keys.password)
#     print('Login to: ', cl.username)
#     user_id = cl.user_id
#     _followers = cl.user_followers(str(cl.user_id), True, amount=0)
#     _following = cl.user_following(str(cl.user_id), True, amount=0)
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
