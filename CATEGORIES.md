# QPanel Assets - Panel Categories

## Overview
All QPanel Assets panels are organized by categories for easy filtering and discovery.

## Available Categories

### 🛠️ GENERAL - General Tools
Practical panels for common Blender workflows:
- **Quick Primitives** - Add mesh, curve, light, camera objects
- **Quick Modifiers** - Add common generate and deform modifiers
- **Mesh Tools** - Cleanup, operations, selection tools
- **Quick Shading** - Viewport shading and smooth/flat controls
- **Transform Tools** - Transform properties and origin manipulation

### 🎨 TEXTUREPAINT - Texture Paint
Complete Texture Paint sidebar clones:
- **Active Tool** - Display active tool info
- **Texture Slots** - Canvas texture selection
- **Brushes** - Brush picker with preview grid
- **Brush Settings** - Size, strength, blend mode, color
- **Masking** - Stencil mask controls
- **Symmetry** - X/Y/Z symmetry toggles
- **Options** - Bleed, dither, auto-normalize
- **Workspace** - Workspace selector

### 📝 EXAMPLES - Example Panels
Template panels showing how to create custom QPanel Assets:
- **Modeling Tools (Example)** - Example modeling operators
- **Quick Materials (Example)** - Example material management

## How to Use Categories

### In QPanel Preferences
When selecting panels, use the left column to filter by category:
- **🎁 QPanel Assets (All)** - Shows all custom panels
- **├─ General Tools** - Shows only general utility panels
- **├─ Texture Paint** - Shows only texture paint panels
- **└─ Examples** - Shows only example/template panels

### Creating Your Own Panels
To add a panel to a category, set the `bl_qpanel_category` attribute:

```python
class QPANEL_ASSET_PT_my_custom_panel(bpy.types.Panel):
    bl_label = "My Custom Panel"
    bl_idname = "QPANEL_ASSET_PT_my_custom_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    bl_qpanel_category = 'GENERAL'  # or 'TEXTUREPAINT' or 'EXAMPLES'
```

### Supported Category Values
- `'GENERAL'` - General utility tools
- `'TEXTUREPAINT'` - Texture paint specific panels
- `'EXAMPLES'` - Example/template panels

## Version History
- **v1.0.5** - Added category system with GENERAL, TEXTUREPAINT, EXAMPLES
- **v1.0.4** - Added Texture Paint panels + auto-reload
- **v1.0.3** - Added useful professional panels
- **v1.0.2** - Fixed registration with panels/__init__.py
- **v1.0.1** - Initial release
