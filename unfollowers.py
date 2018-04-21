import sys, numpy
followers_file, following_file = sys.argv[1], sys.argv[2]
with open(followers_file) as followers_file, open(following_file) as following_file:
	followers_list, following_list = followers_file.read().splitlines(), following_file.read().splitlines()
print("\n".join(unfollower for unfollower in numpy.setdiff1d(following_list,followers_list) if unfollower.lower() == unfollower and ' ' not in unfollower))