# QPanel Assets

Custom UI panels for QPanel add-on.

## Structure

```
qpanel-assets/
├── version.json          # Version info (required for auto-update)
├── README.md
├── panels/               # Custom UI panels
│   └── ...
├── icons/                # Custom icons (optional)
│   └── ...
└── presets/              # Presets (optional)
    └── ...
```

## Version

Current version: **1.0.0**

## Installation

QPanel Assets are automatically downloaded and installed via the QPanel add-on in Blender:

1. Open Blender Preferences → Add-ons → QPanel
2. Go to "License" tab
3. Section "QPanel Assets Management"
4. Click "Install QPanel Assets" or "Update to vX.X.X"

## Development

To publish a new version:

1. Update `version.json` with new version number
2. Add your custom panels in the `panels/` folder
3. Commit and push to GitHub
4. Users will receive the update automatically!

## License

Same as QPanel add-on.
