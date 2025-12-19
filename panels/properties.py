# -*- coding: utf-8 -*-
"""
QPanel Assets - Properties Panels
Essential properties panels (Modifiers, Materials, Object Data)

Based on Blender's native properties_*.py files
"""

import bpy
from bpy.types import Panel


class QPANEL_PT_modifiers(Panel):
    """Modifiers List"""
    bl_label = "Modifiers"
    bl_idname = "QPANEL_PT_modifiers"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_category = "QPanel"
    
    @classmethod
    def poll(cls, context):
        return context.object is not None
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        if not obj.modifiers:
            layout.label(text="No modifiers", icon='INFO')
            return
        
        for mod in obj.modifiers:
            box = layout.box()
            row = box.row()
            row.label(text=mod.name, icon='MODIFIER')
            row.prop(mod, "show_viewport", text="")
            row.prop(mod, "show_render", text="")


class QPANEL_PT_materials(Panel):
    """Materials List"""
    bl_label = "Materials"
    bl_idname = "QPANEL_PT_materials"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_category = "QPanel"
    
    @classmethod
    def poll(cls, context):
        return context.object is not None
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        if not obj.material_slots:
            layout.label(text="No materials", icon='INFO')
            return
        
        for slot in obj.material_slots:
            box = layout.box()
            if slot.material:
                row = box.row()
                row.label(text=slot.material.name, icon='MATERIAL')
                row.prop(slot.material, "diffuse_color", text="")
            else:
                box.label(text="Empty Slot", icon='INFO')


class QPANEL_PT_object_data(Panel):
    """Object Data Properties"""
    bl_label = "Object Data"
    bl_idname = "QPANEL_PT_object_data"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_category = "QPanel"
    
    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH'
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        mesh = obj.data
        
        col = layout.column()
        col.label(text="Mesh Statistics:", icon='MESH_DATA')
        col.separator()
        
        stats_box = col.box()
        stats_box.label(text=f"Vertices: {len(mesh.vertices)}")
        stats_box.label(text=f"Edges: {len(mesh.edges)}")
        stats_box.label(text=f"Faces: {len(mesh.polygons)}")


class QPANEL_PT_constraints(Panel):
    """Object Constraints"""
    bl_label = "Constraints"
    bl_idname = "QPANEL_PT_constraints"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_category = "QPanel"
    
    @classmethod
    def poll(cls, context):
        return context.object is not None
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        if not obj.constraints:
            layout.label(text="No constraints", icon='INFO')
            return
        
        for con in obj.constraints:
            box = layout.box()
            row = box.row()
            row.label(text=con.name, icon='CONSTRAINT')
            row.prop(con, "mute", text="")


classes = (
    QPANEL_PT_modifiers,
    QPANEL_PT_materials,
    QPANEL_PT_object_data,
    QPANEL_PT_constraints,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
