from instagrapi import Client
import keys

if not keys.login or not keys.password:
    print('Please fill correct credentials in keys.py')
    exit()

cl = Client()
cl.login(keys.login, keys.password)

print('Login to: ', cl.username)

user_id = cl.user_id

followers = cl.user_followers(user_id, True, amount=0)
following = cl.user_following(user_id, True, amount=0)

followersCount = len(followers)
followingCount = len(following)

print(cl.username)
print('Followers: ', followersCount)
print('Following: ', followingCount)

followersList = []
followingList = []

for key in followers:
    followersList.append(key)

for key in following:
    followingList.append(key)

unfollow = list(set(followingList) - set(followersList))

print(' '.join(str(cl.username_from_user_id(k)) for k in unfollow))