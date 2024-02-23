from manim import *

class pltExamp(Scene):

    def construct(self):

        ax = Axes(x_range= (-3, 3), y_range= (-3, 3))

        self.add(ax)

"""     Execution command:  
            manim -pql E01-02.Plotting_a_function.py pltExamp     """