# fav_tum
把你喜欢的汤不乐下载下来

#### 关于 user_like.py
It turns out we have two different "types" of likes. One is "liked by blog", in which we use API key to authenticate. The other one is "liked by user", in which we need to use OAuth.

I tried to find an easy implementation of OAuth that does not need pytumblr but failed. Anyway, to get the `secret_str_1`,...,`secret_str_4` in the code, visit https://api.tumblr.com/console/calls/user/info.
