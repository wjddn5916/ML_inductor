
N1 = $N1

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

oDesktop.OpenProject("Y:/git/ML_inductor/inductor_LRT_v1/script29/ML_aedt/ML29.aedt")

oProject = oDesktop.SetActiveProject("ML29")
oProject.InsertDesign("Maxwell", "Maxwell_inductor_v$VERSION_IDX_STR", "EddyCurrent", "")
oDesign = oProject.SetActiveDesign("Maxwell_inductor_v$VERSION_IDX_STR")

#set variable

oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial(
	[
		"NAME:ferrite$VERSION_IDX_STR",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic","Thermal","Structural"]
		],
		[
			"NAME:AttachedData",
			[
				"NAME:MatAppearanceData",
				"property_data:="	, "appearance_data",
				"Red:="			, 89,
				"Green:="		, 94,
				"Blue:="		, 107
			]
		],
		"permittivity:="	, "12",
		"permeability:="	, "$per",
		"conductivity:="	, "0.01",
		"thermal_conductivity:=", "4",
		"mass_density:="	, "4600",
		"specific_heat:="	, "750",
		"youngs_modulus:="	, "119000000000",
		"thermal_expansion_coefficient:=", "1e-05"
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:l1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$l1mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$w1mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:l2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$l2mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:h1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$h1mm"
				]
			]
		]
	])


oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$gapmm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:air",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$airmm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:space2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$space2mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$space1mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:coil_width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$coil_widthmm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:move_z",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$move_zmm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N1"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:offset",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$offsetmm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:skin",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$skinmm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:freq_1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$freqHz"
				]
			]
		]
	])

#core
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2",
		"YPosition:="		, "-(4*l1+2*l2)/2",
		"ZPosition:="		, "-(2*l1+h1)/2",
		"XSize:="		, "w1",
		"YSize:="		, "(4*l1+2*l2)",
		"ZSize:="		, "(2*l1+h1)"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "core",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"ferrite$VERSION_IDX_STR\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2",
		"YPosition:="		, "-l1",
		"ZPosition:="		, "-h1/2",
		"XSize:="		, "w1",
		"YSize:="		, "-l2",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "core_sub1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"ferrite$VERSION_IDX_STR\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2",
		"YPosition:="		, "l1",
		"ZPosition:="		, "-h1/2",
		"XSize:="		, "w1",
		"YSize:="		, "l2",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "core_sub2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"ferrite$VERSION_IDX_STR\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2",
		"YPosition:="		, "-l1",
		"ZPosition:="		, "-gap/2",
		"XSize:="		, "w1",
		"YSize:="		, "2*l1",
		"ZSize:="		, "gap"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "gap",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"ferrite$VERSION_IDX_STR\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "core",
		"Tool Parts:="		, "core_sub1,core_sub2,gap"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

#air
		
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-air/2",
		"YPosition:="		, "-air/2",
		"ZPosition:="		, "-air/2",
		"XSize:="		, "air",
		"YSize:="		, "air",
		"ZSize:="		, "air"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "air",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 1,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

#Tx

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
					"X:="			, "w1/2+coil_width/2+space1",
					"Y:="			, "-l1-coil_width/2-space2",
					"Z:="			, "-0/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "-(w1/2+coil_width/2+space1)",
					"Y:="			, "-l1-coil_width/2-space2",
					"Z:="			, "-0/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "-(w1/2+coil_width/2+space1)",
					"Y:="			, "-(-l1-coil_width/2-space2)",
					"Z:="			, "-1/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "(w1/2+coil_width/2+space1)",
					"Y:="			, "-(-l1-coil_width/2-space2)",
					"Z:="			, "-1/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "(w1/2+coil_width/2+space1)",
					"Y:="			, "(-l1-coil_width/2-space2)+0.5mm",
					"Z:="			, "-2/2*(coil_width+move_z)"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],			
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "6",
			"XSectionBendType:="	, "Corner"
		]
	],
	[
		"NAME:Attributes",
		"Name:="		, "Tx_in",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
					"X:="			, "w1/2+coil_width/2+space1",
					"Y:="			, "-l1-coil_width/2-space2+0.5mm",
					"Z:="			, "-0/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "w1/2+coil_width/2+space1",
					"Y:="			, "-l1-coil_width/2-space2",
					"Z:="			, "-0/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "-(w1/2+coil_width/2+space1)",
					"Y:="			, "-l1-coil_width/2-space2",
					"Z:="			, "-0/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "-(w1/2+coil_width/2+space1)",
					"Y:="			, "-(-l1-coil_width/2-space2)",
					"Z:="			, "-1/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "(w1/2+coil_width/2+space1)",
					"Y:="			, "-(-l1-coil_width/2-space2)",
					"Z:="			, "-1/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "(w1/2+coil_width/2+space1)",
					"Y:="			, "(-l1-coil_width/2-space2)",
					"Z:="			, "-2/2*(coil_width+move_z)"
			],			
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 4,
				"NoOfPoints:="		, 2
			],
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "6",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
					"X:="			, "(w1/2+coil_width/2+space1)",
					"Y:="			, "(-l1-coil_width/2-space2)",
					"Z:="			, "-2/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "air/2",
					"Y:="			, "-l1-coil_width/2-space2",
					"Z:="			, "-2/2*(coil_width+move_z)"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],			
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "6",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out2",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
					"X:="			, "air/2",
					"Y:="			, "-l1-coil_width/2-space2",
					"Z:="			, "-0/2*(coil_width+move_z)"
			],
			[
				"NAME:PLPoint",
					"X:="			, "w1/2+coil_width/2+space1",
					"Y:="			, "-l1-coil_width/2-space2",
					"Z:="			, "-0/2*(coil_width+move_z)"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],			
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "6",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_in2",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_out,Tx_out2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])	

oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in,Tx_in2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])	

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "(N1-1)*(coil_width+move_z)"
	])

oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in,Tx_out"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])


#Tx turn

if N1>2 :
	oEditor.CreatePolyline(
		[
			"NAME:PolylineParameters",
			"IsPolylineCovered:="	, True,
			"IsPolylineClosed:="	, False,
			[
				"NAME:PolylinePoints",
			[
					"NAME:PLPoint",
						"X:="			, "w1/2+coil_width/2+space1",
						"Y:="			, "-l1-coil_width/2-space2+0.5mm",
						"Z:="			, "-0/2*(coil_width+move_z)"
				],
				[
					"NAME:PLPoint",
						"X:="			, "w1/2+coil_width/2+space1",
						"Y:="			, "-l1-coil_width/2-space2",
						"Z:="			, "-0/2*(coil_width+move_z)"
				],
				[
					"NAME:PLPoint",
						"X:="			, "-(w1/2+coil_width/2+space1)",
						"Y:="			, "-l1-coil_width/2-space2",
						"Z:="			, "-0/2*(coil_width+move_z)"
				],
				[
					"NAME:PLPoint",
						"X:="			, "-(w1/2+coil_width/2+space1)",
						"Y:="			, "-(-l1-coil_width/2-space2)",
						"Z:="			, "-1/2*(coil_width+move_z)"
				],
				[
					"NAME:PLPoint",
						"X:="			, "(w1/2+coil_width/2+space1)",
						"Y:="			, "-(-l1-coil_width/2-space2)",
						"Z:="			, "-1/2*(coil_width+move_z)"
				],
				[
					"NAME:PLPoint",
						"X:="			, "(w1/2+coil_width/2+space1)",
						"Y:="			, "(-l1-coil_width/2-space2)+0.5mm",
						"Z:="			, "-2/2*(coil_width+move_z)"
				]
			],
			[
				"NAME:PolylineSegments",
				[
					"NAME:PLSegment",
					"SegmentType:="		, "Line",
					"StartIndex:="		, 0,
					"NoOfPoints:="		, 2
				],
				[
					"NAME:PLSegment",
					"SegmentType:="		, "Line",
					"StartIndex:="		, 1,
					"NoOfPoints:="		, 2
				],
				[
					"NAME:PLSegment",
					"SegmentType:="		, "Line",
					"StartIndex:="		, 2,
					"NoOfPoints:="		, 2
				],
				[
					"NAME:PLSegment",
					"SegmentType:="		, "Line",
					"StartIndex:="		, 3,
					"NoOfPoints:="		, 2
				],
				[
					"NAME:PLSegment",
					"SegmentType:="		, "Line",
					"StartIndex:="		, 4,
					"NoOfPoints:="		, 2
				]
			],
			[
				"NAME:PolylineXSection",
				"XSectionType:="	, "Circle",
				"XSectionOrient:="	, "Auto",
				"XSectionWidth:="	, "coil_width",
				"XSectionTopWidth:="	, "0mm",
				"XSectionHeight:="	, "0mm",
				"XSectionNumSegments:="	, "6",
				"XSectionBendType:="	, "Corner"
			]
		], 
		[
			"NAME:Attributes",
			"Name:="		, "Tx1",
			"Flags:="		, "",
			"Color:="		, "(0 0 255)",
			"Transparency:="	, 0,
			"PartCoordinateSystem:=", "Global",
			"UDMId:="		, "",
			"MaterialValue:="	, "\"copper\"",
			"SurfaceMaterialValue:=", "\"\"",
			"SolveInside:="		, True,
			"ShellElement:="	, False,
			"ShellElementThickness:=", "0mm",
			"IsMaterialEditable:="	, True,
			"UseMaterialAppearance:=", False,
			"IsLightweight:="	, False
		])

	oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "(N1-2)*(coil_width+move_z)"
	])


#copy


for i in range(N1-3) : 

    selection = "Tx" + str(i+2)
    z_vector = "-" + str(i+1) + "*(coil_width+move_z)"

    oEditor.Copy(
        [
            "NAME:Selections",
            "Selections:="		, "Tx1"
        ])
    oEditor.Paste()

    oEditor.Move(
        [
            "NAME:Selections",
            "Selections:="		, selection,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, z_vector
        ])

Tx_unite = "Tx_in,Tx_out"

for i in range(N1-2) : 

    
	Tx_unite = Tx_unite + ",Tx" + str(i+1)

	oEditor.Unite(
	[
	"NAME:Selections",
	"Selections:="		, Tx_unite
	], 
	[
	"NAME:UniteParameters",
	"KeepOriginals:="	, False
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "-(N1-2)*(coil_width+move_z)/2"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "offset"
	])

#terminal
oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "air/2",
		"YCenter:="		, "-l1-coil_width/2-space2",
		"ZCenter:="		, "-0/2*(coil_width+move_z)",
		"XStart:="		, "air/2",
		"YStart:="		, "-l1-coil_width/2-space2",
		"ZStart:="		, "-0/2*(coil_width+move_z)+coil_width/2",
		"NumSides:="		, "6",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_in_ter",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in_ter",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "(N1-1)*(coil_width+move_z)+offset"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in_ter",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "-(N1-2)*(coil_width+move_z)/2"
	])

oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "air/2",
		"YCenter:="		, "-l1-coil_width/2-space2",
		"ZCenter:="		, "-2/2*(coil_width+move_z)",
		"XStart:="		, "air/2",
		"YStart:="		, "-l1-coil_width/2-space2",
		"ZStart:="		, "-2/2*(coil_width+move_z)+coil_width/2",
		"NumSides:="		, "6",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out_ter",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_out_ter",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "offset"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_out_ter",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "-(N1-2)*(coil_width+move_z)/2"
	])

#boundary setup 

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignCoilTerminal(
	[
		"NAME:Tx_in",
		"Objects:="		, ["Tx_in_ter"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", False
	])
oModule.AssignCoilTerminal(
	[
		"NAME:Tx_out",
		"Objects:="		, ["Tx_out_ter"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", True
	])
oModule.AssignWindingGroup(
	[
		"NAME:Tx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "100A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.AddWindingTerminals("Tx", ["Tx_in", "Tx_out"])


oModule = oDesign.GetModule("MaxwellParameterSetup")
oModule.AssignMatrix(
	[
		"NAME:Matrix1",
		[
			"NAME:MatrixEntry",
			[
				"NAME:MatrixEntry",
				"Source:="		, "Tx",
				"NumberOfTurns:="	, "1"
			]
		],
		[
			"NAME:MatrixGroup"
		]
	])

oModule = oDesign.GetModule("MeshSetup")
oModule.AssignSkinDepthOp(
	[
		"NAME:SkinDepth1",
		"Enabled:="		, True,
		"Objects:="		, ["Tx_in"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"SkinDepth:="		, "skin",
		"SurfTriMaxLength:="	, "25mm",
		"NumLayers:="		, "2"
	])

# analysis

oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("EddyCurrent", 
	[
		"NAME:Setup1",
		"Enabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"MaximumPasses:="	, 10,
		"MinimumPasses:="	, 2,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"SolveFieldOnly:="	, False,
		"PercentError:="	, 1,
		"SolveMatrixAtLast:="	, True,
		"UseNonLinearIterNum:="	, False,
		"CacheSaveKind:="	, "Delta",
		"ConstantDelta:="	, "0s",
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-05,
		"NonLinearResidual:="	, 0.0001,
		"SmoothBHCurve:="	, False,
		"Frequency:="		, "freq_1",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunc:=", False,
		"UseMuLink:="		, False
	])
oProject.Save()
oDesign.Analyze("Setup1")

#report

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("inductance", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"w1:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"per:="			, ["Nominal"],
		"gap:="			, ["Nominal"],
		"space2:="		, ["Nominal"],
		"space1:="		, ["Nominal"],
		"coil_width:="		, ["Nominal"],
		"move_z:="		, ["Nominal"],
		"N1:="			, ["Nominal"],
		"offset:="		, ["Nominal"],
		"skin:="		, ["Nominal"],
		"frequency:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Matrix1.L(Tx,Tx)"]
	])
oModule.CreateReport("Loss", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"w1:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"per:="			, ["Nominal"],
		"gap:="			, ["Nominal"],
		"space2:="		, ["Nominal"],
		"space1:="		, ["Nominal"],
		"coil_width:="		, ["Nominal"],
		"move_z:="		, ["Nominal"],
		"N1:="			, ["Nominal"],
		"offset:="		, ["Nominal"],
		"skin:="		, ["Nominal"],
		"frequency:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["SolidLoss"]
	])


oModule.ExportToFile("inductance", "Y:/git/ML_inductor/inductor_LRT_v1/script29/ML_data/inductance_$VERSION_IDX_STR.csv", False)
oModule.ExportToFile("Loss", "Y:/git/ML_inductor/inductor_LRT_v1/script29/ML_data/Loss_$VERSION_IDX_STR.csv", False)
oDefinitionManager.RemoveMaterial("ferrite$VERSION_IDX_STR", True, "", "Project")

