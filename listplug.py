import argparse
from colored import fg, bg, Fore, Style
from pxr import Plug

r1 = bg('navy_blue') + fg('red')
c1 = bg('navy_blue') + fg('white')
c2 = bg('navy_blue') + fg('yellow')
c3 = bg('navy_blue') + fg('green')
c4 = bg('navy_blue') + fg('magenta')
c5 = bg('navy_blue') + Fore.rgb(160, 160, 160)


def get_args():
    """ Get command line arguments
        returns the args
    """
    parser = argparse.ArgumentParser(description="Contact Closure Analysis ",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-md', '--pluginmetadata', action='store_true', default="",
                        help='Print out detailed metadata for each plugin')
    parser.add_argument('-fp', '--filter_plugins', action='store',  required=False, default="",
                        help='Only plugins starting with this string')
    # parser.add_argument('-pvf', '--plotveckfak', action='store', type=float, required=False, default=1.0,
    #                     help='Scale factor for ploting wrench vectors')
    # parser.add_argument('-mu', '--friction', action='store', type=float, required=False, default=-1.0,
    #                     help='Override friction value (mu) for all contact points with this value')
    # parser.add_argument('-t', '--title', action='store', required=False, default="",
    #                     help='Override plot title with this string')
    # parser.add_argument('-ch', '--check', action='store_true', required=False, default=False,
    #                     help='Check the status of the solution')
    # parser.add_argument('-plt', '--probplot', action='store_true', required=False, default=False,
    #                     help='Create a plot of the problem with Matplotlib')
    # parser.add_argument('-sh', '--showplot', action='store_true', required=False, default=False,
    #                     help='Show the plot')
    # parser.add_argument('-sp', '--saveplot', action='store', required=False, default="contactplot.png",
    #                     help='Save plot to this file')
    # parser.add_argument('-v', '--verbosity', default=3, type=int,
    #                     help='Verbosity - 0=minimum (errors+result), 1=info, 2=verbose, 3=debug')

    args = parser.parse_args()
    return args


ags = get_args()

do_filter_plugins = ags.filter_plugins != ""

for plugin in Plug.Registry().GetAllPlugins():
    if do_filter_plugins and not plugin.name.startswith(ags.filter_plugins):
        continue
    print(f"{c1}{plugin.name:20} {c2} loaded:{plugin.isLoaded} Path: {plugin.path}{Style.reset}")
    if ags.pluginmetadata:
        print(f"{c3}  Metadata:{c5}")
        for key, value in plugin.metadata.items():
            if type(value) is dict:
                for k, v in value.items():
                    if type(v) is dict:
                        for k1, v1 in value.items():
                            print(f"{c4}       {k:20} {c5} {k1:20} {v1}{Style.reset}")
                    print(f"{c4}       {key:20} {c5} {k:20} {v}{Style.reset}")
            print(f"{c4}    {key:20} {c5} {value}{Style.reset}")
