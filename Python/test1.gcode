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


    G1 X0 Y200
    G1 X120 Y0
    G1 X0 Y-50
    G1 X-80 Y0
    G1 X0 Y-50
    G1 X80 Y0
    G1 X0 Y-50
    G1 X-80 Y0
    G1 X0 Y-50
    G1 X-40 Y0

G1 X100 Y100
G1 X100 Y-100
G1 X-100 Y-100
G1 X-100 Y100


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
