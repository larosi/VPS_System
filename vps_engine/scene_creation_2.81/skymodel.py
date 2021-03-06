import bpy
import os

CITY_LAT_LONG = [['munich', [48.1351, 11.5820]], ['berlin',[52.5200, 13.4050]], ['london',[51.507351, -0.127758]]]

class SkyModel():
    def __init__(self):
        tree = bpy.data.worlds['World'].node_tree
        links = tree.links

        bgNode = bpy.data.worlds['World'].node_tree.nodes['Background']
        worldopNode = bpy.data.worlds['World'].node_tree.nodes['World Output']
        self.sky_texture = tree.nodes.new('ShaderNodeTexSky')
        links.new(bgNode.inputs['Color'], self.sky_texture.outputs['Color'])
        links.new(bgNode.outputs['Background'], worldopNode.inputs['Surface']) 
        self.sky_texture_brightness = bgNode.inputs[1].default_value

        #sky type 'PREETHAM'/ 'HOSEK_WILKIE'
        self.sky_texture.sky_type = 'HOSEK_WILKIE'
        self.sky_texture.turbidity = 2
        self.sky_texture.ground_albedo = 0.5 

        sun = bpy.data.lights.new("Sun", "SUN")
        self.sun = bpy.data.objects.new("SunRig", sun)  
        self.sun.data.color = [1,1,1]
        self.sun.data.energy = 1        
        bpy.context.collection.objects.link(self.sun)
        self.time = 12
        bpy.data.scenes['Scene'].sun_pos_properties.sun_object = self.sun
        bpy.data.scenes['Scene'].sun_pos_properties.sun_distance = 149999992832
        bpy.data.scenes['Scene'].sun_pos_properties.latitude = 0
        bpy.data.scenes['Scene'].sun_pos_properties.longitude = 0

        #date
        bpy.data.scenes['Scene'].sun_pos_properties.day = 1
        bpy.data.scenes['Scene'].sun_pos_properties.month = 1
        bpy.data.scenes['Scene'].sun_pos_properties.year = 2014
        #time
        bpy.data.scenes['Scene'].sun_pos_properties.time = 12

    def skydomeSettings(self, turbidity, albedo, brightness):
        self.sky_texture.turbidity = turbidity
        self.sky_texture.ground_albedo = albedo
        self.sky_texture_brightness = brightness
    
    def location_cordinates(self, lat_long):
        bpy.data.scenes['Scene'].sun_pos_properties.latitude = lat_long[0]
        bpy.data.scenes['Scene'].sun_pos_properties.longitude = lat_long[1]

    def sunSettings(self, color, energy):
        self.sun.data.color = color
        self.sun.data.energy = energy
        
    def date_timeSettings(self,mm, dd, hrs):
        bpy.data.scenes['Scene'].sun_pos_properties.month = mm
        bpy.data.scenes['Scene'].sun_pos_properties.day = dd
        bpy.data.scenes['Scene'].sun_pos_properties.time = hrs

        
def sky_parameter(del_nodes=False):
    # set render to Cycles
        # remove all nodes
    if del_nodes == True:
        for currentNode in bpy.data.worlds['World'].node_tree.nodes:
            bpy.data.worlds['World'].node_tree.nodes.remove(currentNode)

    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.world.use_nodes = True

    sky = SkyModel()
    return sky