#version 3.7;
global_settings { assumed_gamma 1.0 }

/* Adapted from the tutorial found here:
http://povray.pl/tutorial.php?s=1,4,20
*/

#include "colors.inc" 
 
#declare ObjFinish = finish { reflection 1 diffuse 0 ambient 0 }

light_source { <-1000, 1000,-1000> color Flesh }
light_source { < 1000, 1000,-1000> color White } 

camera { location < 50, 50, -50> look_at < 0, 20, 0> } 

// Construct a background
plane { y,  0 texture { pigment {Gray45} } } 
plane { z, 30 texture { pigment {Gray75} } finish {ObjFinish} }
background { color Gray45 }

// Add the shape
box { < 10, 0, 10> <-10, 20, -10> 
    texture { pigment {CoolCopper} } 
    }
sphere { < 0, 30, 0> 10
    texture { pigment {CoolCopper} }
    }



