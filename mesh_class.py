import pycurl

channels = {
    "AA": (0, 0),
    "AB": (1, 1),
    "AC": (1, 4),
    "AD": (1, 2),
    "AE": (2, 4),
    "AF": (2, 2),
    "BA": (1, 1),
    "BB": (0, 0),
    "BC": (1, 3),
    "BD": (2, 1),
    "BE": (2, 3),
    "BF": (4, 1),
    "CA": (1, 4),
    "CB": (1, 3),
    "CC": (0, 0),
    "CD": (3, 1),
    "CE": (4, 4),
    "CF": (4, 2),
    "DA": (1, 2),
    "DB": (2, 1),
    "DC": (3, 1),
    "DE": (3, 2),
    "DD": (0, 0),
    "DF": (4, 3),
    "EA": (2, 4),
    "EB": (2, 3),
    "EC": (4, 4),
    "ED": (3, 2),
    "EE": (0, 0),
    "EF": (3, 3),
    "FA": (2, 2),
    "FB": (4, 1),
    "FC": (4, 2),
    "FD": (4, 3),
    "FE": (3, 3),
    "FF": (0, 0),
}

index = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D'
}


class MeshClass:
    def __init__(self, name):
        self.name = name

    def set_att(self, port1, port2, atten):
        string = port1+port2
        ports = channels[string]
        block = ports[0]
        channel = ports[1]

        if(ports[0] == 0):
            print("Invalid Arguments for Ports")
        elif(atten < 0 or atten > 95):
            print("Invalid Argument for Attenuation")
        else:
            crl = pycurl.Curl()
            command = f"http://192.168.0.66/:0{block}:CHAN:{channel}:SETATT:{atten}"
            crl.setopt(crl.URL, command)
            crl.perform()
            crl.close()
            print(f"\nPorts:{port1}{port2} Atten:{atten}\n")

    def check_att(self, port1, port2):
        string = port1+port2
        ports = channels[string]
        block = ports[0]
        channel = ports[1]

        if(ports[0] == 0):
            print("Invalid Arguments for Ports")

        else:
            crl = pycurl.Curl()
            command = f"http://192.168.0.66/:0{block}:CHAN:{channel}:ATT?"
            crl.setopt(crl.URL, command)
            crl.perform()
            crl.close()

    def sweep_time(self, direct, units, time):
        crl = pycurl.Curl()
        command = f"http://192.168.0.66/:SWEEP:DIRECTION:{direct}"
        crl.setopt(crl.URL, command)
        crl.perform()

        command = f"http://192.168.0.66/:SWEEP:DWELL_UNIT:{units}"
        crl.setopt(crl.URL, command)
        crl.perform()

        command = f"http://192.168.0.66/:SWEEP:DWELL:{time}"
        crl.setopt(crl.URL, command)
        crl.perform()
        crl.close()

    def sweep_range(self, low, high):
        crl = pycurl.Curl()
        command = f"http://192.168.0.66/:SWEEP:START:{low}"
        crl.setopt(crl.URL, command)
        crl.perform()

        command = f"http://192.168.0.66/:SWEEP:STOP:{high}"
        crl.setopt(crl.URL, command)
        crl.perform()
        crl.close()

    def sweep_address(self, port1, port2):
        string = port1+port2
        ports = channels[string]
        address = ports[0]
        channel = index[ports[1]]
        if(ports[0] == 0):
            print("Invalid Arguments for Ports")
        else:
            crl = pycurl.Curl()
            command = f"http://192.168.0.66/:SWEEP:NOOFCHANNELS:1"
            crl.setopt(crl.URL, command)
            crl.perform()

            command = f"http://192.168.0.66/:SWEEP:CHANNEL_INDEX:0"
            crl.setopt(crl.URL, command)
            crl.perform()

            command = f"http://192.168.0.66/:SWEEP:CHANNEL_ADDRESS:0{address}{channel}"
            crl.setopt(crl.URL, command)
            crl.perform()
            crl.close()

    def sweep_start(self):
        crl = pycurl.Curl()
        command = f"http://192.168.0.66/:SWEEP:MASTERMODE:ON"
        crl.setopt(crl.URL, command)
        crl.perform()

    def sweep_stop(self):
        crl = pycurl.Curl()
        command = f"http://192.168.0.66/:SWEEP:MASTERMODE:OFF"
        crl.setopt(crl.URL, command)
        crl.perform()
