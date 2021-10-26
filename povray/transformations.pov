#version 3.7;
global_settings {assumed_gamma 1.0}

camera { perspective 
    location <8, 8, 8> 
    look_at <0, 0, 0> }

light_source { <5, 12, 10> color rgb <1, 1, 1> }

background { color rgb <0, 0, 0> }

// Axes
cylinder { <0, 0, 0> <0.5, 0, 0> 0.1 
    pigment { color rgb <0.5, 0.2, 0.2> } } // X
cylinder { <0, 0, 0> <0, 0.5, 0> 0.1 
    pigment { color rgb <0.2, 0.5, 0.2> } } // Y
cylinder { <0, 0, 0> <0, 0, 0.5> 0.1 
    pigment { color rgb <0.2, 0.2, 0.5> } } // Z

// Original (White)
sphere { <0, 0, 3>, 1
    pigment { color rgb <1, 1, 1> }
    }

// Translate in y, z (Red)
sphere { <0, 0, 3>, 1
    pigment { color rgb <1, 0, 0> }
    translate <0, 4, -3>
    //translate 3*x  // equivalent to <3, 0, 0>
    }

// Rotate around y axis (Yellow)
sphere { <0, 0, 3>, 1
    pigment { color rgb <0.8, 1, 0> }
    // 90 degrees around the y-axis
    rotate <0, 90, 0>
    }

// Use inverse to undo rotation (Purple)
sphere { <0, 0, 3>, 1
    pigment { color rgb <0.8, 0, 0.8> }
    // Equivalent to rotate <0, -90, 0>
    transform { rotate <0, 90, 0> inverse}
    }

// Scale dimensions (Blue)
sphere { <0, 0, 3>, 1
    pigment { color rgb <0, 0, 1> }
    scale <5, 0.25, 1>
    //scale 2  // equivalent to <2, 2, 2>
    }

