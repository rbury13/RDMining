#!/usr/bin/python

import praw

### Import CLI parser, global variables, scrapers and titles
import src.cli as cli
import src.global_vars as global_vars
import src.scrapers.basic as basic
import src.scrapers.comments as comments
import src.scrapers.redditor as redditor
import src.scrapers.subreddit as subreddit
import src.titles as titles
from src.scraper_functions import (basic_functions, comments_functions,
                                   redditor_functions, subreddit_functions)

### Global variables
options = global_vars.options
s_t = global_vars.s_t

### Reddit API Credentials
c_id = ''                # Personal Use Script (14 char)
c_secret = ''           # Secret key (27 char)
u_a = ''               # App name
usrnm = ''      # Reddit username
passwd = ''     # Reddit login password

### Putting it all together
def main():
    ### Reddit Login
    reddit = praw.Reddit(client_id = c_id, \
                         client_secret = c_secret, \
                         user_agent = u_a, \
                         username = usrnm, \
                         password = passwd)

    ### Parse and check args, and initialize Subreddit, Redditor, post comments,
    ### or basic Subreddit scraper
    parser,args = cli.parse_args()
    cli.check_args(parser,args)
    titles.title()
    if args.sub:
        ### Subreddit scraper
        subreddit.run_subreddit(args,options,parser,reddit,s_t,subreddit_functions)
    if args.user:
        ### Redditor scraper
        redditor.run_redditor(args,s_t,parser,reddit,redditor_functions)
    if args.comments:
        ### Post comments scraper
        comments.run_comments(args,comments_functions,parser,reddit,s_t)
    elif args.basic:
        ### Basic Subreddit scraper
        basic.run_basic(args,basic_functions,options,parser,reddit,subreddit)

if __name__ == "__main__":
    main()
