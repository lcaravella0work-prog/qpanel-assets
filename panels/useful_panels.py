"""
QPanel Assets - Useful Professional Panels
Practical UI panels for common Blender workflows
"""

import bpy


class QPANEL_ASSET_PT_quick_primitives(bpy.types.Panel):
    """Quick access to primitive objects"""
    bl_label = "Quick Primitives"
    bl_idname = "QPANEL_ASSET_PT_quick_primitives"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    
    def draw(self, context):
        layout = self.layout
        
        # Mesh primitives
        box = layout.box()
        box.label(text="Mesh Primitives:", icon='MESH_DATA')
        col = box.column(align=True)
        col.operator("mesh.primitive_cube_add", text="Cube", icon='MESH_CUBE')
        col.operator("mesh.primitive_uv_sphere_add", text="UV Sphere", icon='MESH_UVSPHERE')
        col.operator("mesh.primitive_cylinder_add", text="Cylinder", icon='MESH_CYLINDER')
        col.operator("mesh.primitive_torus_add", text="Torus", icon='MESH_TORUS')
        col.operator("mesh.primitive_plane_add", text="Plane", icon='MESH_PLANE')
        col.operator("mesh.primitive_ico_sphere_add", text="Ico Sphere", icon='MESH_ICOSPHERE')
        
        # Curves
        box = layout.box()
        box.label(text="Curves:", icon='CURVE_DATA')
        col = box.column(align=True)
        col.operator("curve.primitive_bezier_circle_add", text="Bezier Circle", icon='CURVE_BEZCIRCLE')
        col.operator("curve.primitive_bezier_curve_add", text="Bezier Curve", icon='CURVE_BEZCURVE')
        
        # Empties & Lights
        box = layout.box()
        box.label(text="Other:", icon='OUTLINER')
        col = box.column(align=True)
        col.operator("object.empty_add", text="Empty", icon='EMPTY_AXIS').type = 'PLAIN_AXES'
        col.operator("object.light_add", text="Point Light", icon='LIGHT_POINT').type = 'POINT'
        col.operator("object.camera_add", text="Camera", icon='CAMERA_DATA')


class QPANEL_ASSET_PT_quick_modifiers(bpy.types.Panel):
    """Quick add common modifiers"""
    bl_label = "Quick Modifiers"
    bl_idname = "QPANEL_ASSET_PT_quick_modifiers"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        
        if not obj:
            layout.label(text="No active object", icon='INFO')
            return
        
        # Generate modifiers
        box = layout.box()
        box.label(text="Generate:", icon='MODIFIER')
        col = box.column(align=True)
        col.operator("object.modifier_add", text="Subdivision", icon='MOD_SUBSURF').type = 'SUBSURF'
        col.operator("object.modifier_add", text="Array", icon='MOD_ARRAY').type = 'ARRAY'
        col.operator("object.modifier_add", text="Mirror", icon='MOD_MIRROR').type = 'MIRROR'
        col.operator("object.modifier_add", text="Solidify", icon='MOD_SOLIDIFY').type = 'SOLIDIFY'
        col.operator("object.modifier_add", text="Bevel", icon='MOD_BEVEL').type = 'BEVEL'
        col.operator("object.modifier_add", text="Boolean", icon='MOD_BOOLEAN').type = 'BOOLEAN'
        
        # Deform modifiers
        box = layout.box()
        box.label(text="Deform:", icon='MOD_SIMPLEDEFORM')
        col = box.column(align=True)
        col.operator("object.modifier_add", text="Lattice", icon='MOD_LATTICE').type = 'LATTICE'
        col.operator("object.modifier_add", text="Shrinkwrap", icon='MOD_SHRINKWRAP').type = 'SHRINKWRAP'
        col.operator("object.modifier_add", text="Simple Deform", icon='MOD_SIMPLEDEFORM').type = 'SIMPLE_DEFORM'
        col.operator("object.modifier_add", text="Armature", icon='MOD_ARMATURE').type = 'ARMATURE'


class QPANEL_ASSET_PT_mesh_tools(bpy.types.Panel):
    """Mesh editing and cleanup tools"""
    bl_label = "Mesh Tools"
    bl_idname = "QPANEL_ASSET_PT_mesh_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        
        if not obj or obj.type != 'MESH':
            layout.label(text="Select a mesh object", icon='INFO')
            return
        
        # Cleanup tools
        box = layout.box()
        box.label(text="Cleanup:", icon='BRUSHES_ALL')
        col = box.column(align=True)
        col.operator("mesh.remove_doubles", text="Merge by Distance", icon='AUTOMERGE_ON')
        col.operator("mesh.delete_loose", text="Delete Loose", icon='STICKY_UVS_DISABLE')
        col.operator("mesh.normals_make_consistent", text="Recalculate Normals", icon='NORMALS_FACE')
        col.operator("mesh.flip_normals", text="Flip Normals", icon='FLIP')
        
        # Mesh operations
        box = layout.box()
        box.label(text="Operations:", icon='EDITMODE_HLT')
        col = box.column(align=True)
        col.operator("mesh.subdivide", text="Subdivide", icon='MOD_SUBSURF')
        col.operator("mesh.bevel", text="Bevel", icon='MOD_BEVEL')
        col.operator("mesh.inset", text="Inset Faces", icon='MOD_SOLIDIFY')
        col.operator("mesh.extrude_region_move", text="Extrude", icon='ORIENTATION_NORMAL')
        
        # Selection
        box = layout.box()
        box.label(text="Select:", icon='RESTRICT_SELECT_OFF')
        col = box.column(align=True)
        col.operator("mesh.select_all", text="All").action = 'SELECT'
        col.operator("mesh.select_all", text="None").action = 'DESELECT'
        col.operator("mesh.select_all", text="Invert").action = 'INVERT'


class QPANEL_ASSET_PT_quick_shading(bpy.types.Panel):
    """Quick shading and viewport options"""
    bl_label = "Quick Shading"
    bl_idname = "QPANEL_ASSET_PT_quick_shading"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        
        # Viewport shading
        box = layout.box()
        box.label(text="Viewport Shading:", icon='SHADING_RENDERED')
        shading = context.space_data.shading
        row = box.row(align=True)
        row.prop(shading, "type", expand=True)
        
        if obj and obj.type == 'MESH':
            # Object shading
            box = layout.box()
            box.label(text="Object Shading:", icon='SHADING_SOLID')
            col = box.column(align=True)
            col.operator("object.shade_smooth", text="Shade Smooth", icon='SMOOTHCURVE')
            col.operator("object.shade_flat", text="Shade Flat", icon='MESH_PLANE')
            
            # Auto Smooth
            if obj.data:
                box.separator()
                box.prop(obj.data, "use_auto_smooth", text="Auto Smooth")
                if obj.data.use_auto_smooth:
                    box.prop(obj.data, "auto_smooth_angle", text="Angle")


class QPANEL_ASSET_PT_transform_tools(bpy.types.Panel):
    """Quick transform operations"""
    bl_label = "Transform Tools"
    bl_idname = "QPANEL_ASSET_PT_transform_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        
        if not obj:
            layout.label(text="No active object", icon='INFO')
            return
        
        # Transform
        box = layout.box()
        box.label(text="Transform:", icon='ORIENTATION_GLOBAL')
        col = box.column(align=True)
        col.prop(obj, "location", text="Location")
        col.prop(obj, "rotation_euler", text="Rotation")
        col.prop(obj, "scale", text="Scale")
        
        # Transform operations
        box = layout.box()
        box.label(text="Operations:", icon='OBJECT_ORIGIN')
        col = box.column(align=True)
        col.operator("object.origin_set", text="Origin to Geometry").type = 'ORIGIN_GEOMETRY'
        col.operator("object.origin_set", text="Origin to 3D Cursor").type = 'ORIGIN_CURSOR'
        col.operator("object.location_clear", text="Clear Location", icon='LOOP_BACK')
        col.operator("object.rotation_clear", text="Clear Rotation", icon='LOOP_BACK')
        col.operator("object.scale_clear", text="Clear Scale", icon='LOOP_BACK')
        
        # Apply
        box = layout.box()
        box.label(text="Apply:", icon='CHECKMARK')
        col = box.column(align=True)
        col.operator("object.transform_apply", text="Apply All").properties = 'LOCATION'
        col.operator("object.transform_apply", text="Apply Scale").properties = 'SCALE'


# Registration
classes = (
    QPANEL_ASSET_PT_quick_primitives,
    QPANEL_ASSET_PT_quick_modifiers,
    QPANEL_ASSET_PT_mesh_tools,
    QPANEL_ASSET_PT_quick_shading,
    QPANEL_ASSET_PT_transform_tools,
)


def register():
    """Register all custom panels"""
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    """Unregister all custom panels"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
