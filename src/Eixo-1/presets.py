import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams

plt.rc('text',usetex=True)
plt.style.use('seaborn-v0_8-darkgrid')
# plt.style.use('bmh')

mpl.rcParams['figure.dpi'] = 350
plt.rcParams["figure.figsize"] = (14,6)
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 12
rcParams['font.family'] = 'Consolas'
rcParams['font.serif'] = 'Tahoma'
rcParams['svg.fonttype'] = 'none'

#   CORES   #
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"''
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
BLACK = "\033[0;30m"
YELLOW = "\033[0;93m"
MAGENTA = "\033[1;35m"
LIGHT_GREY = "\033[0;37m"
DARK_MAGENTA = "\033[1;95m"
DARK_GREY = "\033[0;90m"
LIGHT_RED = "\033[0;91m"
LIGHT_GREEN = "\033[0;92m"
LIGHT_BLUE = "\033[0;94m"
MARROM = "\033[0;3a"
BOLD = "\33[1:1m"
UNDER = "\33[:4m"
UNDER_BOLD = "\33[1:4m"

#   EMOJIS    #
banana = YELLOW + "\U0001f34C" + RESET
remedio = RED + "\U0001f48a" + RESET
cadeado = "\U0001f513"
caveira = "\U0001f480"
saco = MAGENTA + "\U0001f381" + RESET
diamante = BLUE + "\U0001f48E" + RESET