import bpy
import os

# Personal method to delete all meshes in scene
def delete_stray_meshes():
    objects = bpy.ops.object.select_by_type(type="MESH")
    bpy.ops.object.delete(confirm=False)

# Grab the font from within the same directory
filepath = "//OpenDyslexicMono-Regular.otf"
# open_dyslexic_font = bpy.ops.font.open(filepath="//OpenDyslexicMono-Regular.otf", relative_path=True)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# First thing to do
delete_stray_meshes()

### Start with Uppercase Letters
alphabet = alphabet.upper()

for l in range(0, len(alphabet)):
    # Create the object
    bpy.ops.object.text_add()
    letter = bpy.context.object
    letter.data.body = alphabet[l]
    letter.name = "uppercase_" + alphabet[l]

    # Changing physical features
    letter.data.font = bpy.data.fonts.load("//OpenDyslexicMono-Regular.otf")
    letter.data.extrude = 0.05

    # Convert to mesh
    bpy.ops.object.convert(target='MESH')

    # Set Origin to Volume
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')


### Move onto lowercase letters
alphabet = alphabet.lower()

for l in range(0, len(alphabet)):
    # Create the object
    bpy.ops.object.text_add()
    letter = bpy.context.object
    letter.data.body = alphabet[l]
    letter.name = "lowercase_" + alphabet[l]

    # Changing physical features
    letter.data.font = bpy.data.fonts.load("//OpenDyslexicMono-Regular.otf")
    letter.data.extrude = 0.05

    # Convert to mesh
    bpy.ops.object.convert(target='MESH')

    # Set Origin to Volume
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')


### Export all letters

# get the path where the blend file is located
basedir = bpy.path.abspath('//')

# deselect all objects
bpy.ops.object.select_all(action='DESELECT')    

view_layer = bpy.context.view_layer

for ob in view_layer.objects:
    # make the current object active and select it
    view_layer.objects.active = ob
    ob.select_set(True)

    # make sure that we only export meshes
    if ob.type == 'MESH':
        # export the currently selected object to its own file based on its name
        bpy.context.object.rotation_euler[0] = 1.5708
        bpy.context.object.rotation_euler[2] = 3.14159
        
        bpy.ops.object.location_clear()
        bpy.ops.export_scene.fbx(
                filepath=os.path.join(basedir, ob.name + '.fbx'), global_scale=0.25, 
                apply_unit_scale=False, apply_scale_options='FBX_SCALE_UNITS',
                use_selection=True, axis_forward="Y", axis_up="-Z"
        )
    # deselect the object and move on to another if any more are left
    ob.select_set(False)

delete_stray_meshes()