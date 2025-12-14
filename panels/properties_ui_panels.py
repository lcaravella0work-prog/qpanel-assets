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
        
        # Info box
        box = layout.box()
        box.label(text="Modifier Properties", icon='MODIFIER')
        
        # Try to switch to modifier context and draw the UI
        try:
            # Save current context
            original_context = context.space_data.context
            
            # Switch to MODIFIER context
            context.space_data.context = 'MODIFIER'
            
            # Get the modifier properties panel class
            modifier_panel = getattr(bpy.types, 'DATA_PT_modifiers', None)
            
            if modifier_panel and hasattr(modifier_panel, 'draw'):
                # Draw the modifier panel UI
                modifier_panel.draw(modifier_panel, context)
            else:
                layout.label(text="Switch to Properties > Modifiers", icon='INFO')
                layout.operator("screen.userpref_show", text="Open Properties").section = 'INTERFACE'
            
            # Restore original context
            context.space_data.context = original_context
            
        except Exception as e:
            layout.label(text="Unable to display modifier UI", icon='ERROR')
            layout.label(text=str(e))


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
        
        # Info box
        box = layout.box()
        box.label(text="Material Properties", icon='MATERIAL')
        
        # Try to switch to material context and draw the UI
        try:
            # Save current context
            original_context = context.space_data.context
            
            # Switch to MATERIAL context
            context.space_data.context = 'MATERIAL'
            
            # Get the material properties panel class
            material_panel = getattr(bpy.types, 'MATERIAL_PT_preview', None)
            
            if material_panel and hasattr(material_panel, 'draw'):
                # Draw the material panel UI
                material_panel.draw(material_panel, context)
            else:
                layout.label(text="Switch to Properties > Materials", icon='INFO')
            
            # Restore original context
            context.space_data.context = original_context
            
        except Exception as e:
            layout.label(text="Unable to display material UI", icon='ERROR')
            layout.label(text=str(e))


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
        
        # Info box
        box = layout.box()
        box.label(text="Render Properties", icon='RENDER_STILL')
        
        # Try to switch to render context and draw the UI
        try:
            # Save current context
            original_context = context.space_data.context
            
            # Switch to RENDER context
            context.space_data.context = 'RENDER'
            
            # Get the render properties panel class
            render_panel = getattr(bpy.types, 'RENDER_PT_context', None)
            
            if render_panel and hasattr(render_panel, 'draw'):
                # Draw the render panel UI
                render_panel.draw(render_panel, context)
            else:
                layout.label(text="Switch to Properties > Render", icon='INFO')
            
            # Restore original context
            context.space_data.context = original_context
            
        except Exception as e:
            layout.label(text="Unable to display render UI", icon='ERROR')
            layout.label(text=str(e))


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

