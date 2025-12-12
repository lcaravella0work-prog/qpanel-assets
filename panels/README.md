# QPanel Assets - Panels Folder

Place your custom UI panels here.

Each panel should be a Python file that can be imported by QPanel users.

## Example

Create a file like `modeling_tools.py`:

```python
import bpy

class CustomModelingPanel(bpy.types.Panel):
    bl_label = "Custom Modeling Tools"
    bl_idname = "VIEW3D_PT_custom_modeling"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QPanel'
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="My Custom Tools")
        # Add your UI here
```

Users will be able to select this panel in their QPanel shortcuts.
