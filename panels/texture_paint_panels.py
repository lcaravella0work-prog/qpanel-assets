"""
QPanel Assets - Texture Paint Sidebar Panels
Complete clones of Texture Paint sidebar panels
"""

import bpy
from bpy.types import Panel


class QPANEL_ASSET_PT_active_tool(Panel):
    """Active Tool panel"""
    bl_label = "Active Tool"
    bl_idname = "QPANEL_ASSET_PT_active_tool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_qpanel_category = 'TEXTUREPAINT'  # QPanel Assets category
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'PAINT_TEXTURE'
    
    def draw(self, context):
        layout = self.layout
        tool_settings = context.tool_settings
        
        # Active tool info
        if context.workspace.tools:
            active_tool = context.workspace.tools.from_space_view3d_mode(context.mode)
            if active_tool:
                layout.label(text=active_tool.label, icon=active_tool.icon)


class QPANEL_ASSET_PT_texture_slots(Panel):
    """Texture Slots panel"""
    bl_label = "Texture Slots"
    bl_idname = "QPANEL_ASSET_PT_texture_slots"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_qpanel_category = 'TEXTUREPAINT'  # QPanel Assets category
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'PAINT_TEXTURE' and context.active_object
    
    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings.image_paint
        
        layout.template_ID(settings, "canvas", new="image.new", open="image.open")
        
        if settings.canvas:
            layout.template_image(settings, "canvas", settings.brush, show_unique_hint=False)


class QPANEL_ASSET_PT_brushes(Panel):
    """Brushes panel"""
    bl_label = "Brushes"
    bl_idname = "QPANEL_ASSET_PT_brushes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_qpanel_category = 'TEXTUREPAINT'  # QPanel Assets category
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'PAINT_TEXTURE'
    
    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings.image_paint
        
        row = layout.row(align=True)
        row.template_ID_preview(settings, "brush", new="brush.add", rows=3, cols=8)


class QPANEL_ASSET_PT_brush_settings(Panel):
    """Brush Settings panel"""
    bl_label = "Brush Settings"
    bl_idname = "QPANEL_ASSET_PT_brush_settings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_options = {'DEFAULT_CLOSED'}
    bl_qpanel_category = 'TEXTUREPAINT'  # QPanel Assets category
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'PAINT_TEXTURE' and context.tool_settings.image_paint.brush
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        settings = context.tool_settings.image_paint
        brush = settings.brush
        
        if not brush:
            return
        
        # Radius
        col = layout.column()
        col.prop(brush, "size", slider=True)
        col.prop(brush, "use_pressure_size", text="Pressure Size")
        
        # Strength
        col = layout.column()
        col.prop(brush, "strength", slider=True)
        col.prop(brush, "use_pressure_strength", text="Pressure Strength")
        
        # Blend
        col = layout.column()
        col.prop(brush, "blend", text="Blend Mode")
        
        # Color
        if brush.image_tool == 'DRAW':
            col = layout.column()
            col.template_color_picker(brush, "color", value_slider=True)
            col.prop(brush, "color", text="")


class QPANEL_ASSET_PT_masking(Panel):
    """Masking panel"""
    bl_label = "Masking"
    bl_idname = "QPANEL_ASSET_PT_masking"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_options = {'DEFAULT_CLOSED'}
    bl_qpanel_category = 'TEXTUREPAINT'  # QPanel Assets category
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'PAINT_TEXTURE'
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        ipaint = context.tool_settings.image_paint
        
        col = layout.column()
        col.prop(ipaint, "use_stencil_layer", text="Stencil Mask")
        
        if ipaint.use_stencil_layer:
            col.template_ID(ipaint, "stencil_image", new="image.new", open="image.open")


class QPANEL_ASSET_PT_symmetry(Panel):
    """Symmetry panel"""
    bl_label = "Symmetry"
    bl_idname = "QPANEL_ASSET_PT_symmetry"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_options = {'DEFAULT_CLOSED'}
    bl_qpanel_category = 'TEXTUREPAINT'  # QPanel Assets category
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'PAINT_TEXTURE'
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        ipaint = context.tool_settings.image_paint
        
        col = layout.column()
        row = col.row(align=True)
        row.prop(ipaint, "use_symmetry_x", text="X", toggle=True)
        row.prop(ipaint, "use_symmetry_y", text="Y", toggle=True)
        row.prop(ipaint, "use_symmetry_z", text="Z", toggle=True)


class QPANEL_ASSET_PT_options(Panel):
    """Options panel"""
    bl_label = "Options"
    bl_idname = "QPANEL_ASSET_PT_options"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_options = {'DEFAULT_CLOSED'}
    bl_qpanel_category = 'TEXTUREPAINT'  # QPanel Assets category
    
    @classmethod
    def poll(cls, context):
        return context.mode == 'PAINT_TEXTURE'
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        tool_settings = context.tool_settings
        ipaint = tool_settings.image_paint
        
        col = layout.column()
        col.prop(ipaint, "seam_bleed", text="Bleed")
        col.prop(ipaint, "dither", slider=True)
        
        col.separator()
        
        col.prop(tool_settings, "use_auto_normalize", text="Auto Normalize")


class QPANEL_ASSET_PT_workspace(Panel):
    """Workspace panel"""
    bl_label = "Workspace"
    bl_idname = "QPANEL_ASSET_PT_workspace"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_options = {'DEFAULT_CLOSED'}    bl_qpanel_category = 'TEXTUREPAINT'  # QPanel Assets category    
    @classmethod
    def poll(cls, context):
        return context.mode == 'PAINT_TEXTURE'
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        
        # Workspace selector
        screen = context.screen
        if screen:
            layout.template_search(
                screen, "workspace",
                bpy.data, "workspaces",
                new="workspace.add",
                unlink="workspace.delete"
            )


# Registration
classes = (
    QPANEL_ASSET_PT_active_tool,
    QPANEL_ASSET_PT_texture_slots,
    QPANEL_ASSET_PT_brushes,
    QPANEL_ASSET_PT_brush_settings,
    QPANEL_ASSET_PT_masking,
    QPANEL_ASSET_PT_symmetry,
    QPANEL_ASSET_PT_options,
    QPANEL_ASSET_PT_workspace,
)


def register():
    """Register all Texture Paint panels"""
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    """Unregister all Texture Paint panels"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
