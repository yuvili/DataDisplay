{"Type":"GPS",
"WorldTime":"12:19:44.1018570",
"SimulationTime":0.0333333350718021,
"FrameID":1,
"SimulationPosition":{"x":"93.286","y":"145.143","z":"-0.007"},
"Latitude":48.1764546604836,
"Longitude":11.5853974377919,
"Orientation":{"x":"360.000","y":"360.000","z":"98.141"},
"Speed":8.97119522094727,
"Acceleration":{"x":"0.000","y":"0.000","z":"-0.981"},
"PositionInLane":0,
"LaneWidth":3.31491374969482,
"LaneNumber":-1,
"NavigationSegment":189,
"VelocityLocal3D":{"x":"8.971","y":"0.000","z":"-0.294"},
"AngularVelocityLocal3D":{"x":"0.000","y":"0.000","z":"0.000"},
"AngularAccelerationLocal3D":{"x":"0.000","y":"0.000","z":"0.000"},
"AngularAccelerationLocal3D":6643,
"Name":"Spawn area Spawn area 0001, vehicle 1 of type motor_scooter_three_wheel_White(Clone)"},


{"Type":"Anchor",
"WorldTime":"",
"SimulationTime":0,
"FrameID":0,
"Anchors":[{"AnchorName":"J1-Southbound",
"Position":{"x":"206.600","y":"0.000","z":"-1178.600"},
"Lane":-4}]

// far
{"Type":"Anchor",
"WorldTime":"",
"SimulationTime":0,
"FrameID":0,
"Anchors":[{"AnchorName":"No Lines Start","Position":{"x":"-165.090","y":"1.110","z":"1.540"},"Lane":1}]},

// close
{"Type":"Anchor",
"WorldTime":"",
"SimulationTime":0,
"FrameID":0,
"Anchors":[{"AnchorName":"No Lines Start","Position":{"x":"-165.090","y":"1.110","z":"1.540"},"Lane":1}]},

ActionScript
{"Type":"ActionScript",
"WorldTime":"",
"SimulationTime":0,
"FrameID":0,
"ActorName":"EgoCar",
"Trigger":{"Script":"SimulationTimeTrigger","SimulationTime":"0"},
"Action":{
    "Script":"SetXYLocation",
    "Position":{"X":"133.8484","Y":"77.71294"},
    "RoadSegment":{"RoadID":"16","LaneID":"-1","FirstSectionID":"0","LastSectionID":"0"},
    "Orientation":"0"}},

SensorConfiguration
{"Type":"SensorConfiguration",
"WorldTime":"",
"SimulationTime":0,
"FrameID":0,
"SensorType":"RgbCamera",
"SensorName":"camera0001",
"Position":{"x":"0.340","y":"0.000","z":"1.650"},
"Rotation":{"x":"0.000","y":"13.500","z":"0.000"},
"ProjectionMatrix":{"x":"0.68728090, 0.00000000, 0.00000000, 0.00000000","y":"0.00000000, 3.77022700, 0.00000000, 0.00000000","z":"0.00000000, 0.00000000, -1.00060000, -0.60018000","w":"0.00000000, 0.00000000, -1.00000000, 0.00000000"},
"Near":"0.3",
"Far":"1000",
"FOV":"111",
"Width":"5760",
"Height":"1050",
"AspectRatio":"5.485714",
"OutputQuality":0},

VehicleInfo
{"Type":"VehicleInfo",
"WorldTime":"",
"SimulationTime":0,
"FrameID":0,
"Name":"Ego",
"Dimensions":{"x":"2.199","y":"1.728","z":"4.534"}}

MovingObject Path
"Type":"MovingObject Path",
"WorldTime":"",
"SimulationTime":0,
"FrameID":0,
"VehicleName":"Moving object 0001",
"Waypoints":[{"x":"217.076","y":"0.000","z":"30.700"}]},
