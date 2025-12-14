"""
QPanel Assets - Properties UI Panels
Switch context and display native Blender UI panels
"""

import bpy


class QPANEL_ASSET_PT_modifier_properties(bpy.types.Panel):
    """Display Modifier Properties UI"""
    bl_label = "Modifier Properties UI"
    bl_idname = "QPANEL_ASSET_PT_modifier_properties"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_qpanel_category = 'GENERAL'
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        
        # Header
        box = layout.box()
        row = box.row()
        row.label(text="Modifiers", icon='MODIFIER')
        row.operator("object.modifier_add", text="", icon='ADD')
        
        # Display all modifiers
        if obj.modifiers:
            for mod in obj.modifiers:
                box = layout.box()
                
                # Modifier header
                row = box.row()
                row.prop(mod, "show_expanded", text="", emboss=False)
                row.label(text=mod.name, icon=self.get_modifier_icon(mod.type))
                
                # Modifier controls
                sub = row.row(align=True)
                sub.prop(mod, "show_viewport", text="", icon='RESTRICT_VIEW_OFF' if mod.show_viewport else 'RESTRICT_VIEW_ON')
                sub.prop(mod, "show_render", text="", icon='RESTRICT_RENDER_OFF' if mod.show_render else 'RESTRICT_RENDER_ON')
                
                # Move up/down and delete
                sub = row.row(align=True)
                op = sub.operator("object.modifier_move_up", text="", icon='TRIA_UP')
                op.modifier = mod.name
                op = sub.operator("object.modifier_move_down", text="", icon='TRIA_DOWN')
                op.modifier = mod.name
                op = sub.operator("object.modifier_remove", text="", icon='X')
                op.modifier = mod.name
                
                # Modifier settings (if expanded)
                if mod.show_expanded:
                    self.draw_modifier_settings(box, obj, mod)
        else:
            layout.label(text="No modifiers", icon='INFO')
    
    def get_modifier_icon(self, mod_type):
        """Get icon for modifier type"""
        icons = {
            'ARRAY': 'MOD_ARRAY',
            'BEVEL': 'MOD_BEVEL',
            'BOOLEAN': 'MOD_BOOLEAN',
            'MIRROR': 'MOD_MIRROR',
            'SOLIDIFY': 'MOD_SOLIDIFY',
            'SUBSURF': 'MOD_SUBSURF',
            'SUBDIVISION': 'MOD_SUBSURF',
        }
        return icons.get(mod_type, 'MODIFIER')
    
    def draw_modifier_settings(self, layout, obj, mod):
        """Draw basic modifier settings"""
        # Use template_modifier if available (Blender's built-in UI)
        if hasattr(layout, 'template_modifier'):
            layout.template_modifier(mod)
        else:
            # Fallback: draw some basic properties
            layout.label(text=f"Type: {mod.type}")
            layout.prop(mod, "name")


class QPANEL_ASSET_PT_material_properties(bpy.types.Panel):
    """Display Material Properties UI"""
    bl_label = "Material Properties UI"
    bl_idname = "QPANEL_ASSET_PT_material_properties"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_qpanel_category = 'GENERAL'
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        
        # Header
        box = layout.box()
        row = box.row()
        row.label(text="Materials", icon='MATERIAL')
        
        # Material slots
        if obj.material_slots:
            for i, slot in enumerate(obj.material_slots):
                box = layout.box()
                row = box.row()
                
                if slot.material:
                    row.prop(slot.material, "name", text="", icon='MATERIAL')
                    
                    # Material settings
                    col = box.column()
                    col.prop(slot.material, "use_nodes")
                    if not slot.material.use_nodes:
                        col.prop(slot.material, "diffuse_color", text="Base Color")
                        col.prop(slot.material, "metallic")
                        col.prop(slot.material, "roughness")
                else:
                    row.label(text=f"Slot {i+1}: Empty", icon='BLANK1')
        else:
            layout.label(text="No material slots", icon='INFO')
            layout.operator("object.material_slot_add", icon='ADD')


class QPANEL_ASSET_PT_render_properties(bpy.types.Panel):
    """Display Render Properties UI"""
    bl_label = "Render Properties UI"
    bl_idname = "QPANEL_ASSET_PT_render_properties"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_qpanel_category = 'GENERAL'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        rd = scene.render
        
        # Header
        box = layout.box()
        box.label(text="Render Settings", icon='RENDER_STILL')
        
        # Quick render settings
        col = layout.column(align=True)
        col.prop(rd, "engine", text="Engine")
        col.separator()
        
        col.prop(rd, "resolution_x", text="Resolution X")
        col.prop(rd, "resolution_y", text="Y")
        col.prop(rd, "resolution_percentage", text="%")
        
        col.separator()
        col.prop(rd, "fps")
        
        col.separator()
        box = layout.box()
        box.label(text="Output", icon='OUTPUT')
        col = box.column()
        col.prop(rd, "filepath", text="")
        col.prop(rd, "image_settings", "file_format", text="Format")
        
        # Quick render button
        layout.separator()
        col = layout.column(align=True)
        col.scale_y = 1.5
        col.operator("render.render", text="Render Image", icon='RENDER_STILL')
        col.operator("render.render", text="Render Animation", icon='RENDER_ANIMATION').animation = True


# Panel classes to register
PANELS = [
    QPANEL_ASSET_PT_modifier_properties,
    QPANEL_ASSET_PT_material_properties,
    QPANEL_ASSET_PT_render_properties,
]


def register():
    """Register all panels"""
    for panel in PANELS:
        bpy.utils.register_class(panel)


def unregister():
    """Unregister all panels"""
    for panel in reversed(PANELS):
        bpy.utils.unregister_class(panel)

