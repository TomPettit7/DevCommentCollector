import praw

r = praw.Reddit(user_agent='The Official DeadByDaylight Bot',
                client_id='',
                client_secret='',
                username='',
                password='')

def dev_comments_collect():
    devs = ['tozzer7']
    dev_comments = []
    ids = []
    dev_commented = False
    subreddit = r.subreddit('BotTestingGroundPlace')
    for submission in subreddit.new():
        reddit_comment = submission.reply('Here is a list of all comments by developers: \n\n')
        for comment in submission.comments:
            if comment.id not in ids:
                ids.append(comment.id)
                if str(comment.author) in devs:
                    dev_commented = True
                    print('Comment initiated')
                    comment_body = str(comment.body.encode('utf-8'))
                    comment_author = comment.author

                    dev_comments.append([comment_author, comment_body])

                    for item in dev_comments:
                        user = item[0]
                        body = item[1]

                        string = 'User: ' + str(user) + ' said: ' + str(body) + '\n\n'
                        with open('comment.txt', 'a') as comment_file:
                            comment_file.write(string)
                        with open('comment.txt', 'r') as comment_file_r:
                            reddit_comment_body = comment_file_r.read()

                        reddit_comment.append(string)

                    reddit_comment.mod.distinguish(how='yes', sticky=True)

                    print('Comment Edited')

                else:
                    print('Not a dev comment. Still appended')

            else:
                print('Comment seen already')

        if dev_commented == False:
            reddit_comment.delete()
            print('No dev comments found in this thread')

        dev_comments.clear()

dev_comments_collect()
