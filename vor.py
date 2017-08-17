import random
n_points = 10
file_to_write = "C:\\Users\\jedrz\\Documents\\POV-Ray\\v3.7\\scenes\\cones\\voronoi.pov"


basic = """global_settings {
    ambient_light rgb <0.723364, 0.723368, 0.723364>
}

camera{
    orthographic
    location <0.0,5,0>
    right x * 3
    up y * 3
    look_at <0.0,0.0,0.0>
    
}

light_source {
    <0.0,100,0>
    rgb <0.999996, 1.000000, 0.999996>
    parallel
    point_at <0.0,0.0,0.0>
}
"""
cone = """cone {{
    <0.0, -0.5, 0.0>, 2.0, <0.0, 0.5, 0.0>, 0.0
    hollow
    material {{
        texture {{
            pigment {{
                rgb {0}
            }}
            finish {{
                diffuse 0.6
                brilliance 1.0
            }}
        }}
        interior {{
            ior 1.3
        }}
    }}
    translate {1}
}}
cone {{
    <0.0, -0.5, 0.0>, 0.01, <0.0, 0.5, 0.0>, 0.01
    hollow
    material {{
        texture {{
            pigment {{
                rgb <0,0,0>
            }}
            finish {{
                diffuse 0.6
                brilliance 1.0
            }}
        }}
        interior {{
            ior 1.3
        }}
    }}
    translate {1}
}}
"""
positions = [x*0.05 for x in range(-20,21)]
rgb_values = [x*0.05 for x in range(20)]
colors = []
pos = []
#random choice of sites positions
for i in range(n_points):
    rnd = [random.choice(rgb_values) for i in range(3)]
    n_str = '<{0},{1},{2}>'.format(rnd[0],rnd[1],rnd[2])
    colors.append(n_str)

#random choice of colors
for i in range(n_points):
    n_pos = '<{0},{1},{2}>'.format(random.choice(positions),0,random.choice(positions))
    pos.append(n_pos)



new_file = open(file_to_write,'w')
new_file.write(basic)
for i in range(n_points):
    rgb = colors[i]
    translation = pos[i]
    n_cone = cone.format(rgb,translation)
    new_file.write(n_cone)
new_file.close()