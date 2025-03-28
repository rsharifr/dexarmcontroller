;TOOL_PATH_RENDER_METHOD_LINE
;----------- Start Gcode -----------
M2000;custom:line mode
M888 P0;custom:header is write&draw
M1112
G92 X0 Y300 Z90 E0
G90
;-----------------------------------
G0 Z20
G0 F2000
G1 F2000
G0 X113 Y332 ; used to be X-120 Y253
G1 Z-7
G0 Z20
G0 X-120 Y253
;----------- End Gcode -------------
;-----------------------------------
