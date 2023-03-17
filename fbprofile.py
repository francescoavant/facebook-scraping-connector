from flask_restx import Namespace, Resource
from operator import contains
import json
from facebook_scraper import get_posts
from facebook_scraper import get_profile
from facebook_scraper import *
from flask import request
from utilities import *
from cookie_manager import *
import uuid
import shutil

api= Namespace('profile')

@api.route('/<username>/info')
class ProfileInfo(Resource):
   def get(profileinfo, username):
         Warn().warnignore()
         cookie().accounts()
         cookie().rotatecookie()
         id = str(uuid.uuid4())
         #set_cookies('./cookies/cookie_test.txt')  
         time.sleep(15)
         Path(id).mkdir(parents=True, exist_ok=True)
         profileinfo=get_profile(username, friends=10) 
         name= id +".json"
         with open(id+'/'+name, "w") as f:
            f.write(json.dumps(profileinfo, default=str, indent=4))
         shutil.make_archive(id, 'zip',id) 
         shutil.rmtree(id)  
         return ("file created")

@api.route('/<username>/posts')  
#download user's post
class UserPost(Resource):
    def get(UserPost,username):
         name=username
         posts = dl_posts(name)
         id = str(uuid.uuid4())
         #print(posts)
         Path(id).mkdir(parents=True, exist_ok=True)
         #print(f"Reached {len(posts)} posts, with {sum(p['comments'] for p in posts)} total comments")
         usernamepost= id+"_posts.json"
         with open(id+"/"+usernamepost, "w") as f:
            f.write(json.dumps(posts, default=str,indent=4))
            download().dl_images(quality=download.LOW_QUALITY_KEY, posts=posts,id=id)
            download().dl_images(quality=download.HIGH_QUALITY_KEY, posts=posts, id=id)
            download().dl_video(posts=posts,id=id)
         download().create_archive(id)
         return json.dumps(posts, default=str, indent=4)


