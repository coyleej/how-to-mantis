#version 3.7;
global_settings {assumed_gamma 1.0}

camera { angle 30 location <0, 15, -15> look_at <0, 0, 0> }

light_source { <20, 20, -20> color rgb <1, 1, 1> }

#declare MoveTriangle = 3*x;
#declare MoveSpline = -4*x;
#declare SphereColor = color rgb <1, 1, 0>;
#declare Xcrtl = 6;
#declare Zcrtl = 0.3;

// Triangle
prism 
    {
    linear_sweep
    linear_spline
    0, 0.5, // bounds in the y direction
    4,    // the number of points making up the shape
    // <x,z> coords, first and last match to close the shape
    <1.414,0>, <0,-1>, <0,1>, <1.414,0>
    pigment { color rgb <0.502, 0, 0.502> }
    translate MoveTriangle
    }

// Triangle with cubic spline
prism 
    {
    cubic_spline
    0, 0.5, 6,
    <Xcrtl, Zcrtl>    // a control point
    <1.414,0>, <0,-1>, <0,1>, <1.414,0>
    <Xcrtl, -Zcrtl>   // another control point
    pigment { color rgb <0, 0.8, 0> }
    translate MoveSpline
    }

// Highlight spline control points
sphere { <Xcrtl, 0, Zcrtl> 0.1 pigment {SphereColor} translate MoveSpline }
sphere { <Xcrtl, 0, -Zcrtl> 0.1 pigment {SphereColor} translate MoveSpline }

