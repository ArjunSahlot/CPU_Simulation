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

import tkinter as tk

WIDTH, HEIGHT = 1600, 900

FPS = 90

screen_width = tk.Tk().winfo_screenwidth()
screen_height = tk.Tk().winfo_screenheight()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

BOX = (50, 50, 1500, 745)

COLOR_MAP = {
    "and": (43, 124, 164),
    "not": (146, 32, 25),
    "nand": (93, 36, 180),
    "or": (141, 78, 163),
    "xor": (187, 58, 119),
    "nor": (54, 116, 59),
    "xnor": (129, 160, 200)
}
