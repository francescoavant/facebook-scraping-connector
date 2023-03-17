from facebook_scraper import get_group_info
from flask_restx import Namespace, Resource
import json
from facebook_scraper import *
from utilities import *
import uuid
import shutil
api= Namespace('groups')


#download group's general informations (admins e partecipants)
@api.route('/<groupid>/info')
class GroupInfo(Resource):
    def get(groupinfo,groupid):
        Warn().warnignore()
        time.sleep(15)  
        cookie().accounts()
        cookie().rotatecookie()
        id = str(uuid.uuid4())
        groupinfo=get_group_info(groupid) 
        Path(id).mkdir(parents=True, exist_ok=True)
        name= id +".json"
        with open(id+'/'+name, "w") as f:
         f.write(json.dumps(groupinfo, default=str, indent=4))
        shutil.make_archive(id, 'zip', id) 
        shutil.rmtree(id)
        return ("file created")

#download group posts       
@api.route('/<groupid>/posts')       
class GroupPost(Resource):
    def get(grouppost,groupid):
        id = str(uuid.uuid4())
        posts = dl_posts(groupid)
        Path(id).mkdir(parents=True, exist_ok=True)
        groupposttotal= groupid+"_posts.json"
        with open(id+"/"+groupposttotal, "w") as f:
            f.write(json.dumps(posts, default=str,indent=4))
            download().dl_images(quality=download.LOW_QUALITY_KEY, posts=posts,id=id)
            download().dl_images(quality=download.HIGH_QUALITY_KEY, posts=posts, id=id)
            download().dl_video(posts=posts,id=id)
        download().create_archive(id)
        return json.dumps(posts, default=str, indent=4)

