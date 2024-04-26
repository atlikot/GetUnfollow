from instagrapi import Client

import fake
import keys

# if not keys.login or not keys.password:
#     print('Please fill correct credentials in keys.py')
#     exit()

cl = Client()
cl.username = "Fake user"
user_id = ""


def LoginInstagram():
    #Get followers and following dicts from instagram
    cl.login(keys.login, keys.password)
    print('Login to: ', cl.username)
    user_id = cl.user_id
    _followers = cl.user_followers(str(user_id), True, amount=0)
    _following = cl.user_following(str(user_id), True, amount=0)
    return _followers, _following


followers = fake.GetFollowers()
following = fake.GetFollowing()

print('UserName:', cl.username)
print('Followers:', len(followers))
print('Following:', len(following))

unfollow = list(set(following) - set(followers))
print('Unfollower list (', len(unfollow), '):')
print(unfollow)

for k in unfollow:
    print(following.get(k))
