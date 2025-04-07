;TOOL_PATH_RENDER_METHOD_LINE
;----------- Start Gcode -----------
M2000;custom:line mode
M888 P0;custom:header is write&draw
M1112

G90
;-----------------------------------
G0 Z-55
G0 F1500
G1 F1500
G0 X-119 Y269 

G1 Z-78
G0 Z-55

G1 Z-78
G0 Z-55

G1 Z-78
G0 Z-55

M1112
;----------- End Gcode -------------
;-----------------------------------
