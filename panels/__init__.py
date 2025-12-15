"""
QPanel Assets - Custom Panels Auto-Registration
This module automatically registers all custom panels when assets are loaded
"""

import bpy
from . import example_panels, useful_panels, texture_paint_panels, properties_ui_panels, outliner_portable


# List of all panel modules
modules = [
    example_panels,
    useful_panels,
    texture_paint_panels,
    properties_ui_panels,
    outliner_portable,
]


def register():
    """Register all custom panels"""
    for module in modules:
        if hasattr(module, 'register'):
            module.register()


def unregister():
    """Unregister all custom panels"""
    for module in reversed(modules):
        if hasattr(module, 'unregister'):
            module.unregister()
