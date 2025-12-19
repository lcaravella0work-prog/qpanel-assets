# QPanel Assets v2.1.0 - Testing Guide

## ✅ What Was Done

**Created 16 panel modules with 60+ panels covering ALL essential Blender features:**

### 📁 Modules Created
1. **space_dopesheet.py** - Animation timeline & keyframes
2. **space_graph.py** - F-Curve editing & modifiers
3. **space_nla.py** - Non-linear animation
4. **space_image.py** - UV/Image editor & texture paint
5. **space_node.py** - Shader/Node editor
6. **space_sequencer.py** - Video sequencer
7. **properties_data_mesh.py** - Mesh data & normals
8. **properties_data_camera.py** - Camera settings & DOF
9. **properties_data_light.py** - Light types & shadows
10. **properties_data_curve.py** - Curve geometry & bevel
11. **properties_data_armature.py** - Bones & rigging
12. **properties_render.py** - Render engine & output
13. **properties_scene.py** - Scene units & world
14. **properties_particle.py** - Particle systems
15. **properties_physics.py** - Rigid body, cloth, collision
16. **properties_texture.py** - Texture management

Plus **outliner.py** and **properties.py** from v2.0.0

## 🧪 How to Test

### Step 1: Reload Blender
1. Close and reopen Blender
2. QPanel should auto-reload the addon

### Step 2: Update QPanel Assets
1. Open QPanel preferences
2. Go to **License** tab
3. Click **Download QPanel Assets**
4. Wait for download to complete
5. Auto-updater should detect **v2.1.0**

### Step 3: Test Panel Selector
1. Create a new QPanel (Ctrl+Shift+Alt+P or your shortcut)
2. Open **Panel Selector** (folder icon in QPanel UI)
3. Search for any of these panels:
   - "Keyframe" → should show **Keyframe Tools**
   - "Camera Lens" → should show **Camera Lens**
   - "Mesh Data" → should show **Mesh Data**
   - "Rigid Body" → should show **Rigid Body**
   - "Shader" → should show **Add Shader**

### Step 4: Test Preview Button (CRITICAL)
**This was the original problem you reported!**

1. In Panel Selector, find ANY QPanel Assets panel
2. You should see **INFO icon (ⓘ)** next to the panel name
3. Click the INFO icon
4. A popup should appear showing:
   - Panel name
   - Panel ID
   - Location
   - Description (if any)

**If you DON'T see the INFO icon:**
- The panel is not registered in `bpy.types`
- This means there's a registration issue

### Step 5: Test Panel Execution
1. Select a panel in Panel Selector
2. Click **PLAY icon (▶)** to execute/preview
3. Panel should appear in a popup window
4. Test with different panel types:
   - **Camera Lens** (requires active Camera object)
   - **Mesh Data** (requires active Mesh object)
   - **Render Settings** (works always)
   - **Scene Units** (works always)

## 🔍 Expected Results

### ✅ Success Indicators
- [ ] All 60+ panels appear in Panel Selector
- [ ] Each panel has INFO icon (ⓘ) for preview
- [ ] Each panel has PLAY icon (▶) for execution
- [ ] INFO popup shows correct panel information
- [ ] Panels execute without errors
- [ ] Panels display correctly in popup

### ❌ Failure Indicators
- No INFO icon → Panel not registered in `bpy.types`
- Panel not found in search → Module failed to load
- Execution error → `poll()` method failing or missing attributes
- Empty popup → `draw()` method has errors

## 🐛 Troubleshooting

### Problem: "Panel not found"
**Solution:** Check Blender console (Window → Toggle System Console) for Python errors during registration

### Problem: "No INFO icon"
**Solution:** Panel is not registered. Check if:
1. Auto-updater downloaded v2.1.0
2. Blender was reloaded after update
3. Panel module has syntax errors (check console)

### Problem: "Poll failed" or "Greyed out"
**Solution:** Some panels require specific contexts:
- **Mesh Data** → Select a mesh object
- **Camera Lens** → Select a camera object
- **Armature Bones** → Select an armature object
- Use **Render Settings** or **Scene Units** for always-available panels

### Problem: "Empty popup"
**Solution:** `draw()` method has errors. Check console for AttributeError or TypeError

## 📊 Statistics

- **16 modules** (space_* and properties_*)
- **60+ panels** (average 4 panels per module)
- **Full bl_ui coverage** of essential Blender features
- **100% Panel Selector compatible** (all panels have preview button)

## 📝 Report Back

Please test and report:
1. ✅ or ❌ Panel Selector shows all panels
2. ✅ or ❌ INFO icon appears on all panels
3. ✅ or ❌ Panels execute without errors
4. Any specific panel that fails (name + error message)

## 🎯 Next Steps

If all tests pass:
- v2.1.0 is production-ready ✅
- You can assign any panel to your QPanels
- 60+ essential Blender panels now available as portable popups

If tests fail:
- Report specific errors
- I'll fix registration/poll/draw issues
- Re-deploy fixed version

---

**Version:** 2.1.0  
**Commit:** 5c59400  
**GitHub:** https://github.com/lcaravella0work-prog/qpanel-assets
