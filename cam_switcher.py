import bpy

bl_info = {
    "name": "Camera Switcher",
    "description": "Switch Cameras and create Bound Timeline "
                   "markers naturally.",
    "author": "Daniel Fairhead",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "3D View > Tools",
    "category": "3D View",
    "wiki_url": "https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Camera_Switcher"
    }

# Helper internal functions:


def marker_now(context):
    ''' Drop a marker in the timeline at the current frame and return it,
        or return the current marker if there is already one there '''

    markers = context.scene.timeline_markers
    now = context.scene.frame_current
    for m in markers:
        if m.frame == now:
            return m
    return markers.new(name='new', frame=now)


class CutToCamera(bpy.types.Operator):
    bl_idname = "view3d.cut_to_camera"
    bl_label = "Cuts to the selected camera, and adds a marker linking to it."

    def execute(self, context):
        marker = marker_now(context)
        cam = context.active_object
        marker.camera = cam
        marker.name = cam.name
        return {'FINISHED'}


class CameraSwitcherPanel(bpy.types.Panel):
    bl_label = "Camera Switcher"
    bl_idname = "CAM_SWITCHER_BOX"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOL_PROPS'
    bl_context = "objectmode"

    bpy.types.Scene.camera_switcher_sorted = \
        bpy.props.BoolProperty(name="Sort Cameras", default=True)

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        cams = (c for c in scene.objects if c.type == 'CAMERA')
        if scene.camera_switcher_sorted:
            cams = sorted(cams, key=lambda c: c.name)
        for cam in cams:
            row = layout.row()
            row.label(text=cam.name)
            row = layout.row(align=True)
            row.context_pointer_set("active_object", cam)
            row.operator('view3d.object_as_camera', text="Preview")
            row.operator('view3d.cut_to_camera', text='Take')

        row = layout.row()
        row.prop(scene, "camera_switcher_sorted")


def register():
    bpy.utils.register_class(CutToCamera)
    bpy.utils.register_class(CameraSwitcherPanel)


def unregister():
    bpy.utils.unregister_class(CameraSwitcherPanel)
    bpy.utils.unregister_class(CutToCamera)

if __name__ == "__main__":
    register()
