from mesh_class import MeshClass

mesh = MeshClass("NET Lab Mesh Network")

# MeshClass uses the python library pycurl to perform curl operations
#
# Functions in the MeshClass:
#
#   set_att:
#       This lets you change the attentuation level in on any connection between ports A-F
#       It needs three arguments: port1, port2, atten
#       port1 and port2 represent which ports you want to connect and atten represents the attenuation level
#       Example: set_att('B','D', 50) will set attenuation for the connection between port B and port D to 50
#       Using the function set_att('B','D', 50) and set_att('D', 'B', 50) will give you the same results
#       If port1 and port2 arguments are the same, you will get an error
#       atten is any number between 0-95 db
#
#
#   check_att:
#       This lets you check what the attenuation is for any connection between ports A-F
#       It needs two arguments: port1, port2
#       port1 and port2 represent which ports you wnat to connect
#       Example: check_att('B', 'D') will tell you the attenuatioln between ports B and D
#       Using check_att('B', 'D') and check_att('D', B') will give you the same results
#       If port1 and port2 arguments are the same, you will get an error
#       The results are returned by the http command and will include the attenuator block
#       Example of results: 01:30.0 this is showing that on the first attenuator block the attenuation is 30 db
#
#   To perform a sweep there are five functions to call: sweep_time, sweep_range, sweep_address, sweep_start, sweep_stop
#   They have been split up for convenience
#
#   sweep_time:
#       This will set the time and direction for a sweep function to perform
#       It has two arguments: direct, units, time
#       direct will choose what direction you are sweeping
#       units will determine what units of time it will use.
#       Options are 'U' for microseconds, 'M' for milliseconds and 'S' for seconds
#       time is an integer that will be determine the length in units how long the sweep will run
#       Options are 0 for lowest to highest value, 1 for highest to lowest, and 2 for bi-directional sweep, a sweep forward and then backwards
#       Example: sweep_time('S', 120, 0) will run for 120 seconds and run from lowest to highest value
#       This function runs three http commands. You will see three 1's printed to the terminal which are the results of the commands
#
#   sweep_range:
#       This will allow you to choose what range of attenuation you want to sweep
#       It needs two arguments: low, high
#       low determines your lowest value on your sweep. high determines your highest value on your sweep
#       Example: sweep_range(0, 50) will set my lowest attenuation value to 0 db and my highest attenuation value to 50 db
#       This function runs two http commands. You will see two 1's printed to the terminal which are the results of the commands
#
#   sweep_address:
#       This will let you choose which port connections you would like to sweep. The class is only designed to do one connection at a time
#       It needs two arguments: port1, port2
#       port1 and port2 represent which ports you want to connect together
#       Example: sweep_address('B', 'D') will sweep the attenuation between port B and port D
#       Using sweep_address('B', 'D') and sweep_address('D', B') will give you the same results
#       If port1 and port2 arguments are the same, you will get an error
#       This function runs three http commands. You will see three 1's printed to the terminal which are the results of the commands
#
#   sweep_start:
#       This will start the sweep. It will run indefinitely until stopped
#       This function runs one http command. You will see one 1 printed to the terminal which is the result of the command
#
#   sweep_stop:
#       This will stop the sweep.
#       This function runs one http command. You will see one 1 printed to the terminal which is the result of the command
#
#
#   hop_setup, hop_point_time, hop_point_atten, hop_point_address, hop_start, hop_stop
#
#
#
#
