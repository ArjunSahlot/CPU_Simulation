#
#  Cpu simulation
#  A simulation created in pygame in which you can explore how logic gates work.
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

def _and(a, b):
    return a.status and b.status


def _or(a, b):
    return a.status or b.status


def _xor(a, b):
    return a.status ^ b.status


def _not(a):
    return not a.status


def _nand(a, b):
    return not(a.status and b.status)


def _xnor(a, b):
    return a.status == b.status


def _nor(a, b):
    return not(a.status or b.status)
