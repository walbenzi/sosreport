### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin, UbuntuPlugin, DebianPlugin
import glob

class libvirt(Plugin, RedHatPlugin, UbuntuPlugin, DebianPlugin):
    """libvirt-related information
    """
    def setup(self):
        self.addCopySpecs(["/etc/libvirt/", "/var/log/libvirt*"])

    def postproc(self):
       for xmlfile in glob.glob("/etc/libvirt/qemu/*.xml"):
            self.doFileSub(xmlfile,
                    r"(\s*passwd=\s*')([^']*)('.*$)",
                    r"\1******\3")
