"""
QPanel Assets - Outliner Portable
Replicate Blender's Outliner functionality in a portable panel
Access collections and objects hierarchy anywhere via QPanel shortcuts
"""

import bpy
from bpy.types import Panel, Operator


# Operator to select object in viewport
class QPANEL_OT_select_object(Operator):
    """Select object in viewport"""
    bl_idname = "qpanel.select_object"
    bl_label = "Select Object"
    bl_options = {'REGISTER', 'UNDO'}
    
    object_name: bpy.props.StringProperty()
    
    def execute(self, context):
        obj = bpy.data.objects.get(self.object_name)
        if obj:
            # Deselect all
            bpy.ops.object.select_all(action='DESELECT')
            # Select target
            obj.select_set(True)
            context.view_layer.objects.active = obj
            self.report({'INFO'}, f"Selected: {obj.name}")
        else:
            self.report({'WARNING'}, f"Object not found: {self.object_name}")
        return {'FINISHED'}


# Main Outliner Portable Panel
class QPANEL_ASSET_PT_outliner_portable(Panel):
    """Portable Outliner - Access collections and objects anywhere"""
    bl_label = "Outliner Portable"
    bl_idname = "QPANEL_ASSET_PT_outliner_portable"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_qpanel_category = 'GENERAL'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Header
        box = layout.box()
        box.label(text="Scene Outliner", icon='OUTLINER')
        
        # Collections Section
        box = layout.box()
        box.label(text="Collections:", icon='OUTLINER_COLLECTION')
        
        # Master Collection (Scene Collection)
        master_box = box.box()
        row = master_box.row(align=True)
        row.label(text=f"{scene.name} (Scene)", icon='SCENE_DATA')
        row.prop(scene.collection, "hide_viewport", text="", icon='HIDE_OFF' if not scene.collection.hide_viewport else 'HIDE_ON', emboss=False)
        row.prop(scene.collection, "hide_render", text="", icon='RESTRICT_RENDER_OFF' if not scene.collection.hide_render else 'RESTRICT_RENDER_ON', emboss=False)
        
        # List all collections
        if bpy.data.collections:
            for collection in bpy.data.collections:
                col_box = box.box()
                row = col_box.row(align=True)
                
                # Collection name
                row.label(text=collection.name, icon='OUTLINER_COLLECTION')
                
                # Object count
                row.label(text=f"({len(collection.objects)})")
                
                # Visibility toggles
                sub = row.row(align=True)
                sub.prop(collection, "hide_viewport", text="", icon='HIDE_OFF' if not collection.hide_viewport else 'HIDE_ON', emboss=False)
                sub.prop(collection, "hide_render", text="", icon='RESTRICT_RENDER_OFF' if not collection.hide_render else 'RESTRICT_RENDER_ON', emboss=False)
                
                # Show objects in this collection
                if collection.objects:
                    obj_col = col_box.column(align=True)
                    obj_col.scale_y = 0.8
                    
                    for obj in collection.objects:
                        obj_row = obj_col.row(align=True)
                        obj_row.separator()
                        obj_row.separator()
                        
                        # Object icon based on type
                        icon_map = {
                            'MESH': 'OUTLINER_OB_MESH',
                            'CURVE': 'OUTLINER_OB_CURVE',
                            'SURFACE': 'OUTLINER_OB_SURFACE',
                            'META': 'OUTLINER_OB_META',
                            'FONT': 'OUTLINER_OB_FONT',
                            'ARMATURE': 'OUTLINER_OB_ARMATURE',
                            'LATTICE': 'OUTLINER_OB_LATTICE',
                            'EMPTY': 'OUTLINER_OB_EMPTY',
                            'GPENCIL': 'OUTLINER_OB_GREASEPENCIL',
                            'CAMERA': 'OUTLINER_OB_CAMERA',
                            'LIGHT': 'OUTLINER_OB_LIGHT',
                            'SPEAKER': 'OUTLINER_OB_SPEAKER',
                            'LIGHT_PROBE': 'OUTLINER_OB_LIGHTPROBE',
                        }
                        obj_icon = icon_map.get(obj.type, 'OBJECT_DATA')
                        
                        # Select button
                        op = obj_row.operator("qpanel.select_object", text=obj.name, icon=obj_icon, emboss=False)
                        op.object_name = obj.name
                        
                        # Active indicator
                        if context.view_layer.objects.active == obj:
                            obj_row.label(text="", icon='LAYER_ACTIVE')
                        
                        # Visibility toggles
                        obj_row.prop(obj, "hide_viewport", text="", icon='HIDE_OFF' if not obj.hide_viewport else 'HIDE_ON', emboss=False)
                        obj_row.prop(obj, "hide_render", text="", icon='RESTRICT_RENDER_OFF' if not obj.hide_render else 'RESTRICT_RENDER_ON', emboss=False)
        else:
            box.label(text="No collections in scene", icon='INFO')
        
        # Quick Actions
        layout.separator()
        box = layout.box()
        box.label(text="Quick Actions:", icon='SETTINGS')
        col = box.column(align=True)
        col.operator("object.select_all", text="Select All").action = 'SELECT'
        col.operator("object.select_all", text="Deselect All").action = 'DESELECT'
        col.operator("object.hide_view_clear", text="Unhide All", icon='HIDE_OFF')


# Registration
classes = (
    QPANEL_OT_select_object,
    QPANEL_ASSET_PT_outliner_portable,
)


def register():
    """Register Outliner Portable panel and operators"""
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    """Unregister Outliner Portable panel and operators"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
