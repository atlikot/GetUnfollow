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

# Generate dict of unfollowers (key: UserShort class)
unfollow = {k: v for k, v in following.items() if k not in followers}

string = ''

for k in unfollow:
    string += following.get(k).username + ', '

string = string.rstrip(', ')

print('Unfollows:', string)