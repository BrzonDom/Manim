from manim import *

class frstExamp(Scene):
    def construct(self):
        bl_Circ = Circle(color=BLUE, fill_opacity=0.5)

        gr_Sqr = Square(color=GREEN, fill_opacity=0.8)
        gr_Sqr.next_to(bl_Circ, RIGHT)

        self.add(bl_Circ, gr_Sqr)