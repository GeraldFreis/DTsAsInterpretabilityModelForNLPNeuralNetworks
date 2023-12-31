from tkinter import *
import tkinter as tk
from tkinter import ttk


class ToolTip(object):
    """Class that handles creating little hovering tooltips for the DT"""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text

        def enter(event):
            self.showTooltip()
        def leave(event):
            self.hideTooltip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def showTooltip(self):
        self.tooltipwindow = tk.Toplevel(self.widget)
        tw = self.tooltipwindow
        tw.wm_overrideredirect(1) # window without border and no normal means of closing
        tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx(), self.widget.winfo_rooty()))
        label = tk.Label(tw, text = self.text, background = "#ffffe0", wraplength=150, relief = 'solid', borderwidth = 1).pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        tw.destroy()
        self.tooltipwindow = None