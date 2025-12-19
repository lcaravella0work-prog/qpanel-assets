# -*- coding: utf-8 -*-
"""
QPanel Assets - Native Outliner Panel
Full-featured Outliner display in popup (Blender-native style)

Based on Blender's space_outliner.py but adapted for popup display.
Shows hierarchical object tree with collections, visibility toggles, and selection.
"""

import bpy
from bpy.types import Panel


class QPANEL_PT_outliner_popup(Panel):
    """Full-featured Outliner in popup window"""
    bl_idname = "QPANEL_PT_outliner_popup"
    bl_label = "Outliner"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        view_layer = context.view_layer
        
        # Header with display mode selector
        row = layout.row(align=True)
        row.label(text="", icon='OUTLINER')
        row.label(text="Scene Objects")
        
        layout.separator()
        
        # Filter options (compact version)
        filter_box = layout.box()
        filter_row = filter_box.row(align=True)
        filter_row.label(text="Filters:", icon='FILTER')
        
        # Object type visibility toggles (similar to Outliner filters)
        type_row = filter_box.row(align=True)
        type_row.scale_y = 0.8
        
        # Create filter properties on the fly if needed
        if not hasattr(scene, "qpanel_outliner_show_mesh"):
            # Use scene properties for filter state
            pass
        
        layout.separator()
        
        # Collections section
        col_box = layout.box()
        col_header = col_box.row()
        col_header.label(text="Collections", icon='OUTLINER_COLLECTION')
        
        # Draw collections
        self.draw_collections(col_box, scene.collection, context)
        
        layout.separator()
        
        # Objects tree section
        obj_box = layout.box()
        obj_header = obj_box.row()
        obj_header.label(text="Objects", icon='OBJECT_DATAMODE')
        
        # Draw object hierarchy
        self.draw_object_tree(obj_box, context)
    
    def draw_collections(self, layout, collection, context, level=0):
        """Draw collections hierarchy"""
        if level == 0:
            # Root scene collection
            row = layout.row(align=True)
            row.label(text="Scene Collection", icon='SCENE_DATA')
            row.prop(collection, "hide_viewport", text="", emboss=False)
            row.prop(collection, "hide_render", text="", emboss=False)
        
        # Child collections
        for child_col in collection.children:
            row = layout.row(align=True)
            
            # Indentation
            for _ in range(level + 1):
                row.label(text="", icon='BLANK1')
            
            # Collection visibility
            row.prop(child_col, "hide_viewport", text="", emboss=False,
                    icon='HIDE_OFF' if not child_col.hide_viewport else 'HIDE_ON')
            
            # Collection name
            row.label(text=child_col.name, icon='OUTLINER_COLLECTION')
            
            # Render visibility
            row.prop(child_col, "hide_render", text="", emboss=False,
                    icon='RESTRICT_RENDER_OFF' if not child_col.hide_render else 'RESTRICT_RENDER_ON')
            
            # Recursive draw children
            if child_col.children:
                self.draw_collections(layout, child_col, context, level + 1)
    
    def draw_object_tree(self, layout, context, level=0):
        """Draw object hierarchy tree"""
        scene = context.scene
        
        # Get all top-level objects (no parent)
        top_level_objects = [obj for obj in scene.objects if obj.parent is None]
        
        if not top_level_objects:
            layout.label(text="No objects in scene", icon='INFO')
            return
        
        # Sort by name
        top_level_objects.sort(key=lambda x: x.name)
        
        # Draw each object and its children
        for obj in top_level_objects:
            self.draw_object_item(layout, obj, context, level)
    
    def draw_object_item(self, layout, obj, context, level=0):
        """Draw single object with children"""
        row = layout.row(align=True)
        
        # Indentation
        for _ in range(level):
            row.label(text="", icon='BLANK1')
        
        # Viewport visibility toggle
        row.prop(obj, "hide_viewport", text="", emboss=False,
                icon='HIDE_OFF' if not obj.hide_viewport else 'HIDE_ON')
        
        # Object type icon
        icon_map = {
            'MESH': 'OUTLINER_OB_MESH',
            'CURVE': 'OUTLINER_OB_CURVE',
            'SURFACE': 'OUTLINER_OB_SURFACE',
            'META': 'OUTLINER_OB_META',
            'FONT': 'OUTLINER_OB_FONT',
            'ARMATURE': 'OUTLINER_OB_ARMATURE',
            'LATTICE': 'OUTLINER_OB_LATTICE',
            'EMPTY': 'OUTLINER_OB_EMPTY',
            'LIGHT': 'OUTLINER_OB_LIGHT',
            'CAMERA': 'OUTLINER_OB_CAMERA',
            'SPEAKER': 'OUTLINER_OB_SPEAKER',
            'LIGHTPROBE': 'OUTLINER_OB_LIGHTPROBE',
            'GPENCIL': 'OUTLINER_OB_GREASEPENCIL',
            'CURVES': 'OUTLINER_OB_CURVES',
            'POINTCLOUD': 'OUTLINER_OB_POINTCLOUD',
            'VOLUME': 'OUTLINER_OB_VOLUME',
        }
        icon = icon_map.get(obj.type, 'OBJECT_DATA')
        
        # Selection toggle (make object active)
        op = row.operator("object.select_pattern", text=obj.name, icon=icon, emboss=False)
        op.pattern = obj.name
        op.case_sensitive = True
        op.extend = False
        
        # Render visibility
        row.prop(obj, "hide_render", text="", emboss=False,
                icon='RESTRICT_RENDER_OFF' if not obj.hide_render else 'RESTRICT_RENDER_ON')
        
        # Draw children recursively
        if obj.children:
            for child in sorted(obj.children, key=lambda x: x.name):
                self.draw_object_item(layout, child, context, level + 1)


# Operator to show Outliner in popup
class QPANEL_OT_show_outliner_native(bpy.types.Operator):
    """Show native Outliner panel in popup"""
    bl_idname = "qpanel.show_outliner_native"
    bl_label = "Outliner"
    bl_description = "Show complete Outliner with collections and hierarchy"
    bl_options = {'REGISTER'}
    
    width: bpy.props.IntProperty(default=500)
    
    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=self.width)
    
    def draw(self, context):
        layout = self.layout
        
        # Draw the panel directly
        panel = QPANEL_PT_outliner_popup()
        panel.draw(context)
    
    def execute(self, context):
        return {'FINISHED'}


# Registration
classes = (
    QPANEL_PT_outliner_popup,
    QPANEL_OT_show_outliner_native,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
