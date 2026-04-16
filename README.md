# cura-ringing-tower-script
Cura implementation of custom layer change G-code macro used in slicing [Ringing Tower STL](//marlinfw.org/assets/stl/ringing_tower.stl) for [M593](//marlinfw.org/docs/gcode/M593.html) or [M493](//marlinfw.org/docs/gcode/M493.html) based input shaping.
Use the script with Post Processing Plugin on Cura Marketplace.

Copy the `InputShaping.py` file into your cura directory as follows:
* (Windows) `C:\Users\{USERNAME}\AppData\Roaming\cura\{VERSION}\scripts`
* (Mac) `/Users/{USERNAME}/Library/Application Support/cura/{VERSION}/scripts`

# Available settings
1. Motion planning type (M593 or M493)
2. Start frequency
3. End frequency
