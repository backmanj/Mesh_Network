import requests
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
    def __init__(self, address):
        self.address = address

    def set_att(self, port1: str, port2: str, atten: int):
        """
        set_att:
            This lets you change the attentuation level in on any connection between ports A-F\n
            It needs three arguments: port1, port2, atten\n
            port1 and port2 represent which ports you want to connect and atten represents the attenuation level\n
            Example: set_att('B','D', 50) will set attenuation for the connection between port B and port D to 50\n
            Using the function set_att('B','D', 50) and set_att('D', 'B', 50) will give you the same results\n
            If port1 and port2 arguments are the same, you will get an error\n
            atten is any number between 0-95 db\n
        """
        string = port1+port2
        ports = channels[string]
        block = ports[0]
        channel = ports[1]

        if(ports[0] == 0):
            print("Invalid Arguments for Ports")
        elif(atten < 0 or atten > 95):
            print("Invalid Argument for Attenuation")
        else:
            requests.get(
                f'http://{self.address}/:0{block}:CHAN:{channel}:SETATT:{atten}')
            print(f"\nPorts:{port1}{port2} Atten:{atten}\n")

    def check_att(self, port1: str, port2: str):
        """
        check_att:
            This lets you check what the attenuation is for any connection between ports A-F\n
            It needs two arguments: port1, port2\n
            port1 and port2 represent which ports you want to connect\n
            Example: check_att('B', 'D') will tell you the attenuatioln between ports B and D\n
            Using check_att('B', 'D') and check_att('D', B') will give you the same results\n
            If port1 and port2 arguments are the same, you will get an error\n
            The results are returned by the http command and will include the attenuator block\n
            Example of results: 01:30.0 this is showing that on the first attenuator block the attenuation is 30 db\n
        """
        string = port1+port2
        ports = channels[string]
        block = ports[0]
        channel = ports[1]

        if(ports[0] == 0):
            print("Invalid Arguments for Ports")

        else:
            crl = pycurl.Curl()
            command = f"http://{self.address}/:0{block}:CHAN:{channel}:ATT?"
            crl.setopt(crl.URL, command)
            crl.perform()
            crl.close()

    def sweep_time(self, direct: int, units: str, time: int):
        """
        sweep_time:
            This will set the time and direction for a sweep function to perform\n
            It has three arguments: direct, units, time\n
            direct will choose what direction you are sweeping\n
            Options are 0 for lowest to highest value, 1 for highest to lowest, and 2 for bi-directional sweep--a sweep forward and then backwards\n
            units will determine what units of time it will use.\n
            Options are 'U' for microseconds, 'M' for milliseconds and 'S' for seconds\n
            time is an integer that will be determine the length in units how long the sweep will run\n
            Example: sweep_time(0,'S', 120) will run for 120 seconds and run from lowest to highest value\n
        """
        requests.get(f'http://{self.address}/:SWEEP:DIRECTION:{direct}')
        requests.get(f'http://{self.address}/:SWEEP:DWELL_UNIT:{units}')
        requests.get(f'http://{self.address}/:SWEEP:DIRECTION:{direct}')

    def sweep_range(self, low: int, high: int):
        """
        sweep_range:
            This will allow you to choose what range of attenuation you want to sweep\n
            It needs two arguments: low, high\n
            low determines your lowest value on your sweep. high determines your highest value on your sweep\n
            Example: sweep_range(0, 50) will set my lowest attenuation value to 0 db and my highest attenuation value to 50 db\n
        """
        requests.get(f'http://{self.address}/:SWEEP:START:{low}')
        requests.get(f'http://{self.address}/:SWEEP:STOP:{high}')

    def sweep_address(self, port1: str, port2: str):
        """
        sweep_address:
            This will let you choose which port connections you would like to sweep. The class is only designed to do one connection at a time\n
            It needs two arguments: port1, port2\n
            port1 and port2 represent which ports you want to connect together\n
            Example: sweep_address('B', 'D') will sweep the attenuation between port B and port D\n
            Using sweep_address('B', 'D') and sweep_address('D', B') will give you the same results\n
            If port1 and port2 arguments are the same, you will get an error\n
        """
        string = port1+port2
        ports = channels[string]
        block = ports[0]
        channel = index[ports[1]]
        if(ports[0] == 0):
            print("Invalid Arguments for Ports")
        else:
            requests.get(f'http://{self.address}/:SWEEP:NOOFCHANNELS:1')
            requests.get(f'http://{self.address}/:SWEEP:CHANNEL_INDEX:0')
            requests.get(
                f'http://{self.address}/:SWEEP:CHANNEL_ADDRESS:0{block}{channel}')

    def sweep_start(self):
        """
        sweep_start:
            This will start the sweep. It will run indefinitely until stopped\n
        """
        requests.get(f'http://{self.address}/:SWEEP:MASTERMODE:ON')

    def sweep_stop(self):
        """
        sweep_stop:
            This will stop the sweep.\n
        """
        requests.get(f'http://{self.address}/:SWEEP:MASTERMODE:OFF')
