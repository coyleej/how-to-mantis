#version 3.7;
global_settings {assumed_gamma 1.0}

camera 
	{
	perspective  
	location <1, 2, 3>
	look_at <0, 0, 0>
	}

light_source 
	{
	<4, 4, 3> 
	color rgb <1, 1, 1> 
	}

// The four objects (a box and three cylinders)
box { <-1.5, -1.5, -0.8>, <1.5, 1.5, 0> pigment {color rgb <1, 1, 1>} }
cylinder { <0, -1, 0>, <0, 1, 0>, 0.6 pigment { color rgb <0, 1, 1> } }
cylinder { <-1, 0, 0>, <1, 0, 0>, 0.6 pigment { color rgb <1, 0, 1> } }
cylinder { <0, 0, -1>, <0, 0, 1>, 0.6 pigment { color rgb <1, 1, 0> } }

// CSG, each cylinder assigned a color
//union
//    {
//    cylinder { <0, -1, 0>, <0, 1, 0>, 0.6 pigment { color rgbt <0, 1, 1, 0.6> } }
//    cylinder { <-1, 0, 0>, <1, 0, 0>, 0.6 pigment { color rgbt <1, 0, 1, 0.6> } }
//    cylinder { <0, 0, -1>, <0, 0, 1>, 0.6 pigment { color rgbt <1, 1, 0, 0.6> } }
//    }

// CSG, color applied to final shape
//union
//    {
//    cylinder { <0, -1, 0>, <0, 1, 0>, 0.6 }
//    cylinder { <-1, 0, 0>, <1, 0, 0>, 0.6 }
//    cylinder { <0, 0, -1>, <0, 0, 1>, 0.6 }
//    pigment { color rgbft <0, 1, 1, 0.5, 0> }
//    }

// CSG of four objects (box and three cylinders)
//intersection
//    {
//    box { <-1.5, -1.5, -0.8>, <1.5, 1.5, 0> }
//    cylinder { <0, -1, 0>, <0, 1, 0>, 0.6 }
//    cylinder { <-1, 0, 0>, <1, 0, 0>, 0.6 }
//    cylinder { <0, 0, -1>, <0, 0, 1>, 0.6 }
//    pigment {color rgb <0, 1, 1>}
//    }

// CSG of box and union
//intersection
//    {
//    box { <-1.5, -1.5, -0.8>, <1.5, 1.5, 0> }
//    union
//        {
//        cylinder { <0, -1, 0>, <0, 1, 0>, 0.6 }
//        cylinder { <-1, 0, 0>, <1, 0, 0>, 0.6 }
//        cylinder { <0, 0, -1>, <0, 0, 1>, 0.6 }
//        }
//    pigment {color rgb <0, 1, 1>}
//    }

// Co-incident surface artifacts
//difference
//    {
//    box { <-1, -1, -1>, <1, 1, 1>  pigment { color rgb <1, 1, 0> } }
//    union
//        {
//        cylinder { <0, -1, 0>, <0, 1, 0>, 0.6 }
//        cylinder { <-1, 0, 0>, <1, 0, 0>, 0.6 }
//        cylinder { <0, 0, -1>, <0, 0, 1>, 0.6 }
//        pigment {color rgb <0, 1, 1>}
//        }
//    }

