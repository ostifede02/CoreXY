;FLAVOR:Marlin
;TIME:21
;Filament used: 0.00504667m
;Layer height: 0.2
;MINX:88.003
;MINY:84.654
;MINZ:0.1
;MAXX:131.951
;MAXY:135.346
;MAXZ:0.1
;Generated with Cura_SteamEngine 4.11.0
M140 S60
M105
M190 S60
M104 S200
M105
M109 S200
M82 ;absolute extrusion mode
; Ender 3 Custom Start G-code
G92 E0 ; Reset Extruder
G28 ; Home all axes
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
G1 Y20 X0.1  Z0.3 F5000.0 ; Move to start position
G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line
G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little
G1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line
G92 E0 ; Reset Extruder
G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed
G1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish
G92 E0
G92 E0
G1 F1500 E-6.5
;LAYER_COUNT:2
;LAYER:0
M107
;MESH:Corpo1.stl
G0 F6000 X131.851 Y97.385 Z0.1
;TYPE:WALL-OUTER
G1 F1500 E0
G1 F1200 X110 Y84.769 E0.4196
G1 X88.149 Y97.385 E0.8392
G1 X88.149 Y122.615 E1.25878
G1 X110 Y135.231 E1.67838
G1 X131.851 Y122.615 E2.09798
G1 X131.851 Y97.385 E2.51756
G1 F1500 E-3.98244
G0 F6000 X110 Y84.96
G0 X88.049 Y97.326
G1 F1500 E2.51756
G1 F1200 X110 Y84.654 E2.93907
G1 X131.951 Y97.326 E3.36058
G1 X131.951 Y122.674 E3.78212
G1 X110 Y135.346 E4.20362
G1 X88.049 Y122.674 E4.62513
G1 X88.049 Y97.326 E5.04667
G0 F6000 X88.003 Y97.301
;TIME_ELAPSED:21.290617
G1 F1500 E-1.45333
M140 S0
G91 ;Relative positioning
G1 E-2 F2700 ;Retract a bit
G1 E-2 Z0.2 F2400 ;Retract and raise Z
G1 X5 Y5 F3000 ;Wipe out
G1 Z10 ;Raise Z more
G90 ;Absolute positioning

G1 X0 Y220 ;Present print
M106 S0 ;Turn-off fan
M104 S0 ;Turn-off hotend
M140 S0 ;Turn-off bed

M84 X Y E ;Disable all steppers but Z

M82 ;absolute extrusion mode
M104 S0
;End of Gcode
;SETTING_3 {"global_quality": "[general]\\nversion = 4\\nname = Standard Quality
;SETTING_3  #2\\ndefinition = creality_ender3pro\\n\\n[metadata]\\ntype = qualit
;SETTING_3 y_changes\\nquality_type = standard\\nsetting_version = 17\\n\\n[valu
;SETTING_3 es]\\nadhesion_type = none\\nlayer_height_0 = 0.1\\nmaterial_bed_temp
;SETTING_3 erature = 60\\n\\n", "extruder_quality": ["[general]\\nversion = 4\\n
;SETTING_3 name = Standard Quality #2\\ndefinition = creality_ender3pro\\n\\n[me
;SETTING_3 tadata]\\ntype = quality_changes\\nquality_type = standard\\nsetting_
;SETTING_3 version = 17\\nposition = 0\\n\\n[values]\\nbrim_line_count = 10\\nin
;SETTING_3 fill_pattern = triangles\\ninfill_randomize_start_location = True\\ni
;SETTING_3 nfill_sparse_density = 90.0\\ninfill_sparse_thickness = 0.2\\nmagic_m
;SETTING_3 esh_surface_mode = both\\nmaterial_print_temperature = 200.0\\nspeed_
;SETTING_3 infill = 60.0\\ntop_bottom_thickness = 0.6\\nwall_line_count = 3\\nz_
;SETTING_3 seam_type = random\\n\\n"]}
