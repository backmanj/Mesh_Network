from mesh_class import MeshClass

mesh = MeshClass("192.168.0.66")

# MeshClass uses the python library pycurl to perform curl operations
#
# Functions in the MeshClass:
#
#   To perform a sweep there are five functions to call: sweep_time, sweep_range, sweep_address, sweep_start, sweep_stop
#   They have been split up for convenience
#
#
#   hop_setup, hop_point_time, hop_point_atten, hop_point_address, hop_start, hop_stop
#
#
#
#

mesh.set_att('E', 'B', 35)
mesh.check_att('E', 'B')
# mesh.sweep_time(0, 'M', 300)
# mesh.sweep_range(0, 65)
# mesh.sweep_address('F', 'A')
# mesh.sweep_start()

# mesh.sweep_stop()
