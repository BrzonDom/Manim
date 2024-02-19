from manim import *
"""     Importing the manim library     """


class frstExamp(Scene):
    """     Object class, manim animations are on basis of classes
                Scene, provided canvas-like structure       """

    def construct(self):
        """     Construct method, provided method    """

        bl_Circ = Circle(color=BLUE, fill_opacity=0.5)

        gr_Sqr = Square(color=GREEN, fill_opacity=0.8)
        gr_Sqr.next_to(bl_Circ, RIGHT)

        self.add(bl_Circ, gr_Sqr)


"""     Execution command:
            manim -pql {file_name}.py {class_name}    """
