#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
"""
Click Command definition for the enumerate classes command.
"""

import click
from pywbem import Error
from .pywbemclicmd import pywbemcli, CMD_OPTS_TXT, display_result


@pywbemcli.command('enumerateclassnames', options_metavar=CMD_OPTS_TXT)
@click.argument('classname', type=str, metavar='classname')
@click.option('-d', '--deepinheritance', is_flag=True, required=False,
              help='Return complete subclass hiearchy for this class.')
@click.pass_obj
def enumerateclassenames(context, classname, **options):
    """
    Get and display a class in the WBEM Server.

    In addition to the command-specific options shown in this help text, the
    general options (see 'zhmc --help') can also be specified before the
    command.
    """
    context.execute_cmd(
        lambda: cmd_enumerateclassnames(context, classname, options))


def cmd_enumerateclassnames(context, classname, options):
    """
    get and display a list of classnames.
    """
    try:
        if context._verbose:
            print('enumerateclassnames %s deepinheritance %s' %
                  (classname, options['deepinheritance']))
        result = context._conn.EnumerateClasseNames(
            classname, options['deepinheritance'])
        display_result(result)
    except Error as er:
        raise click.ClickException("%s: %s" % (er.__class__.__name__, er))
