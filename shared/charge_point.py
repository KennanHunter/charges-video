from typing import Any
from manim import *
from manim import Tex
from numpy import dtype, floating, ndarray


class Charge(VDict):
    def __init__(self, magnitude: float, color: ManimColor, ** kwargs):
        super().__init__(**kwargs)

        self.circle = Circle(1.5, color, fill_opacity=1).scale(abs(magnitude))
        self.text = Tex(
            ("+" if magnitude > 0 else "") + str(magnitude) + "C", stroke_width=1).scale(1.5)
        self.magnitude = magnitude

        self.add_key_value_pair("base", self.circle)
        self.add_key_value_pair("text", self.text)

    def get_center(self) -> ndarray[Any, dtype[floating[Any]]] | tuple[float, float, float]:
        return self.circle.get_center()

    def set_vector(self, vector: Arrow):
        self.add_key_value_pair("vector", vector)

    def get_vector(self) -> Arrow:
        return self["vector"]


class PositiveCharge(Charge):
    def __init__(self, **kwargs):
        super().__init__(1, RED, **kwargs)


class NegativeCharge(Charge):
    def __init__(self, **kwargs):
        super().__init__(-1, BLUE, **kwargs)
