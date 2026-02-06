bl_info = {
    "name": "Auto Highlight in Outliner",
    "description": "Automatically highlights the selected object in the Outliner",
    "author": "Blendermark",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "Outliner",
    "category": "Object"
}

import bpy

def highlight_in_outliner():
    outliner_area = None
    for area in bpy.context.screen.areas:
        if area.type == 'OUTLINER':
            outliner_area = area
            break

    if outliner_area:
        region = next((r for r in outliner_area.regions if r.type == 'WINDOW'), None)
        if region:
            with bpy.context.temp_override(area=outliner_area, region=region):
                try:
                    bpy.ops.outliner.show_active()
                except Exception as e:
                    print(f"Error: {e}")

@bpy.app.handlers.persistent
def auto_highlight(scene, depsgraph):
    if bpy.context.active_object:
        highlight_in_outliner()

def register():
    if auto_highlight not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(auto_highlight)

def unregister():
    if auto_highlight in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(auto_highlight)

if __name__ == "__main__":
    register()