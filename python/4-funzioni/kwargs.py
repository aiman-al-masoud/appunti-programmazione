from enum import Enum

class Colors(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 

def color_print(text, **kwargs):
    params = {"color" : Colors.OKBLUE.value}
    params.update(kwargs)
    print( params["color"] + text+Colors.ENDC.value)


color_print("ciao")

color_print("ciao mondo", color=Colors.UNDERLINE.value)

