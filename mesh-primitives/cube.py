import bpy

for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

bpy.ops.mesh.primitive_cube_add(location=(5.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0))
bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 2.0))
bpy.ops.mesh.primitive_cube_add(location=(-5.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 3.0))