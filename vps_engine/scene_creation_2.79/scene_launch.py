# reload every import 
import sys, os
import importlib
import bpy
# TODO: change this to relative path using os/pathlib
# NOTE: If you load Blender first then open a project then the CWD is where Blender is. If you script from the blender the CWD is the location of the blender program.

# TODO: When excecuted in blender the os.path gives out C:/ instead of abs path of scene_launch; for now hard code the abs path of this file.
# office WS C:/Users/Qutub/Documents/VPS/scene_content/VPS_project/scene_creation
# HP laptop C:/Users/squtub/Documents/Master_Thesis/Git/vps_engine/scene_creation
filepath = bpy.context.space_data.text.filepath
print(filepath)
launch_path = os.path.dirname(filepath)
launch_path = launch_path.replace('\\','/')
scenecontent_path = os.path.join(launch_path.rsplit("/",2)[0] + '/scene_content')
sys.path.append(launch_path)

import blender_utils
importlib.reload(blender_utils)
from blender_utils import *

import asset_import
importlib.reload(asset_import)
from asset_import import *
DEBUG = False
if DEBUG == True:
     PYDEV_SOURCE_DIR = "C:/Users/Qutub/.p2/pool/plugins/org.python.pydev.core_7.4.0.201910251334/pysrc"
     # "/usr/lib/eclipse/dropins/pydev/eclipse/plugins/org.python.pydev_4.5.4.201601292234/pysrc"
     #C:/Users/Qutub/.p2/pool/plugins/org.python.pydev.core_7.4.0.201910251334/pysrc

     if PYDEV_SOURCE_DIR not in sys.path:
          sys.path.append(PYDEV_SOURCE_DIR)

     import pydevd

     pydevd.settrace()

     bling = "the parrot has ceased to be"
     print(bling)
     
def test_edited_bvh(character_path):
     mocap_data_basicwalk_edited = os.path.join(scenecontent_path + '/graphics/3D_characters/Motion Capture data/Female1_bvh/Female1_B03_Walk1.bvh')
     male_char_01 = MakeHuman('male_basic01', character_path)
     male_char_01.attach_mocap(mocap_data_basicwalk_edited)

def main():

     blender_utils.bld_clearscreenspace()
     DEBUG = False
     if DEBUG == True:
          print('In DEBUGGER MODE')
          import sys
          PYDEV_SOURCE_DIR = "C:/Users/squtub/.p2/pool/plugins/org.python.pydev.core_7.4.0.201910251334/pysrc"

          if PYDEV_SOURCE_DIR not in sys.path:
              sys.path.append(PYDEV_SOURCE_DIR)
          import pydevd

          pydevd.settrace()

          bling = "the parrot has ceased to be"
          print(bling)
          # TODO: Import city and character models form bash file
     citymodel_path= os.path.join(scenecontent_path + '/graphics/city_models/9btvoxf8n0cg-3dt/Street environment_V01.FBX') #"C:/Users/Qutub/Documents/VPS_System/scene_content/graphics/city_models/9btvoxf8n0cg-3dt/Street environment_V01.FBX"
     filetype = "FBX"
     city = CityModels(name='Square_City',path=citymodel_path,filetype=filetype)

     mhchar_path = os.path.join(scenecontent_path + '/graphics/3D_characters/makehuman_characters/characters/female_basic/female_basic.mhx2')
     #mocap_data_basicwalk = os.path.join(scenecontent_path + '/graphics/3D_characters/Motion Capture data/Female1_bvh/Female1_B03_Walk1.bvh')
     mocap_data_basicwalk = os.path.join(scenecontent_path + '/graphics/3D_characters/Motion Capture data/cmuconvert-mb2-01-09/02/02_02.bvh')
     male_char_00 = MakeHuman('male_basic00', mhchar_path )
     male_char_00.attach_mocap(mocap_data_basicwalk)

     sky_spotlights = ['Sky001']
     camera = ['Camera001']
     blender_utils.relocate_object(object = sky_spotlights[0], loc = (0,0,20))
     blender_utils.attributeDataChange(sky_spotlights[0], attribute = 'energy', value = 20)
     blender_utils.relocate_object(object = camera[0], loc = (9.7, 5, 1.6))
     blender_utils.rotate_object(object = camera[0], eulerAngle = (1.5707963705062866, 0.016647271811962128, 2.2514748573303223))

     #TODO : Define this function
     #cameras = define_CAMS(units = 1)
     cameras = ['Camera001']
     generateDataset(cameras, launch_path)



if __name__ == "__main__":
     main()
     

