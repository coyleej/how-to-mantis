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

background { color rgb <0, 0, 0> }

// Basic primitive
cylinder 
	{
	<0, -1, 0>, 
	<0, 1, 0>, 
	0.6
	pigment { color rgb <0, 1, 1> }
	}

