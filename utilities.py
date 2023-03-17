from facebook_scraper import *
import warnings
from flask_restx import Resource
from operator import contains
import json
from facebook_scraper import get_posts
from facebook_scraper import get_profile
import requests
from utilities import *
from pathlib import Path
from cookie_manager import *
import uuid
import shutil

class Warn:
    def warnignore(self):
        warnings.filterwarnings("ignore", message="Facebook says 'Unsupported Browser'")


def dl_posts(name,read_from_file = True):
    #if read_from_file:
    #    with open('test_file.json') as f:
    #        posts = json.load(f)
    #else:
        Warn().warnignore()
        cookie().accounts()
        cookie().rotatecookie()
        time.sleep(15)
        posts=list(get_posts(name, options={"allow_extra_requests": True, "post_per_page": 20,"comments":True}))
        return posts

class download(Resource):
    HIGH_QUALITY_KEY = "images"
    LOW_QUALITY_KEY = "images_lowquality"

    def _get_image_name(self,image):
        nome=image.split('?')[0].split('/')[-1]
        return nome
    
    def dl_images(self,quality, posts, id):
        contatore=0
        Path(id+"/media").mkdir(parents=True, exist_ok=True)
        for post in posts:
            if post[quality]:
                for image in post[quality]:
                    if image is not None:
                        #print(image) 
                        contatore+=1 
                        response= requests.get(image)
                        nome = self._get_image_name(image)
                        open(id+"/media"+"/"+nome, "wb").write(response.content)           
        return posts   

    def dl_video(self,posts, id):
        contatore=0
        Path(id+"/media").mkdir(parents=True, exist_ok=True)
        for post in posts:
            if post['video']:
                    if post is not None:
                        #print(post['video']) 
                        contatore+=1 
                        response= requests.get(post['video'])
                        nome = self._get_image_name(post['video'])
                        open(id+"/media"+"/"+nome, "wb").write(response.content) 
        return posts 
#zip output
    def create_archive(self, id):
        shutil.make_archive(id, 'zip',id) 
        time.sleep(1)
        shutil.rmtree(id)  
