from flask_restx import Namespace, Resource
import json
from facebook_scraper import get_page_info
from utilities import *
from cookie_manager import *
import uuid
import shutil
api= Namespace('pages')


#general page informations
@api.route('/<pagename>/info')
class PageInfo(Resource):
   def get(pageinfo,pagename):
      Warn().warnignore()
      cookie().accounts()
      cookie().rotatecookie()
      time.sleep(15)
      id = str(uuid.uuid4())
      pageinfo=get_page_info(pagename)
      Path(id).mkdir(parents=True, exist_ok=True)
      name= id +".json"
      with open(id+'/'+name, "w") as f:
         f.write(json.dumps(pageinfo, default=str, indent=4))
      shutil.make_archive(id, 'zip', id) 
      shutil.rmtree(id)
      return ("file created")

#download page posts
@api.route('/<pagename>/posts')       
class PagePost(Resource):
   def get(pagepost,pagename):
      name=pagename
      posts = dl_posts(name)
      id = str(uuid.uuid4())
      Path(id).mkdir(parents=True, exist_ok=True)
      pageposttotal= pagename+"_posts.json"
      with open(name+"/"+pageposttotal, "w") as f:
            f.write(json.dumps(posts, default=str,indent=4))
            download().dl_images(quality=download.LOW_QUALITY_KEY, posts=posts,id=id)
            download().dl_images(quality=download.HIGH_QUALITY_KEY, posts=posts, id=id)
            download().dl_video(posts=posts,id=id)
      download().create_archive(id)
      return json.dumps(posts, default=str, indent=4)


