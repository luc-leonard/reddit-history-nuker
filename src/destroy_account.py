import praw
import string
import random

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
    reddit = praw.Reddit(client_id='*********************',
                         client_secret='**************',
                         password='************',
                         user_agent='testscript by /u/fakebot3',
                         username='***********')

    while True:
        comments = reddit.user.me().comments.hot()
        i = 0
        for commentId in comments:
            i = i + 1
            comment = reddit.comment(commentId)
            comment.edit(randomString())
            comment.delete()
        print(i)
        if i == 0:
            return 0


if __name__ == '__main__':
    main()
