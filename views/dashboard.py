from core.style import *
from flet import *
from core.client import *
from core import fake


class Dashboard(Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        print(cl.username)
        print('Getting following list...')

        followers = fake.get_followers() if cl.username == 'fake' else cl.user_followers(str(cl.user_id))
        following = fake.get_following() if cl.username == 'fake' else cl.user_following(str(cl.user_id))

        print('-------------')
        print(followers)
        print('-------------')
        print(following)
        print('-------------')

        string = ''
        unfollow = {k: v for k, v in following.items() if k not in followers}
        print(unfollow)
        print('-------------')

        for k in unfollow:
            string += following.get(k).username + ', '
        string = string.rstrip(', ')
        print('-------------')

        print('Unfollows:', string)
        print('Done')


