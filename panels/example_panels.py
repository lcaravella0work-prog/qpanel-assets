"""
Example Custom Panel for QPanel Assets
This is a template showing how to create custom UI panels for QPanel
"""

import bpy


class QPANEL_ASSET_PT_example_modeling(bpy.types.Panel):
    """Example modeling tools panel"""
    bl_label = "Modeling Tools (Example)"
    bl_idname = "QPANEL_ASSET_PT_example_modeling"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Example Custom Panel", icon='MODIFIER')
        layout.separator()
        
        box = layout.box()
        box.label(text="Common Modeling Operations:")
        col = box.column(align=True)
        col.operator("mesh.subdivide", text="Subdivide")
        col.operator("mesh.bevel", text="Bevel")
        col.operator("mesh.inset", text="Inset Faces")
        col.operator("mesh.loop_multi_select", text="Select Loops")
        
        layout.separator()
        
        box = layout.box()
        box.label(text="Modifiers:")
        col = box.column(align=True)
        col.operator("object.modifier_add", text="Add Subdivision").type = 'SUBSURF'
        col.operator("object.modifier_add", text="Add Solidify").type = 'SOLIDIFY'
        col.operator("object.modifier_add", text="Add Bevel").type = 'BEVEL'


class QPANEL_ASSET_PT_example_materials(bpy.types.Panel):
    """Example materials panel"""
    bl_label = "Quick Materials (Example)"
    bl_idname = "QPANEL_ASSET_PT_example_materials"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Material Quick Actions", icon='MATERIAL')
        layout.separator()
        
        obj = context.active_object
        if obj and obj.type == 'MESH':
            box = layout.box()
            box.label(text=f"Object: {obj.name}")
            
            col = box.column(align=True)
            col.operator("object.material_slot_add", text="Add Material Slot", icon='ADD')
            col.operator("object.material_slot_remove", text="Remove Slot", icon='REMOVE')
            
            layout.separator()
            
            if obj.data.materials:
                box = layout.box()
                box.label(text="Current Materials:")
                for i, mat in enumerate(obj.data.materials):
                    if mat:
                        row = box.row(align=True)
                        row.label(text=f"{i+1}. {mat.name}", icon='MATERIAL_DATA')
            else:
                layout.label(text="No materials assigned", icon='INFO')
        else:
            layout.label(text="Select a mesh object", icon='INFO')


# Registration
classes = (
    QPANEL_ASSET_PT_example_modeling,
    QPANEL_ASSET_PT_example_materials,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
