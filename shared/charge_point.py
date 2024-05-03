from typing import Any
from manim import *
from manim import Tex
from numpy import dtype, floating, ndarray


class Charge(VGroup):
    def __init__(self, magnitude: float, color: ManimColor, ** kwargs):
        super().__init__(**kwargs)

        self.circle = Circle(1, color, fill_opacity=1).scale(abs(magnitude))
        self.text = Tex(
            f"{"+" if magnitude > 0 else ""}{magnitude}C", stroke_width=1)
        self.magnitude = magnitude

        self.add(self.circle, self.text)

    def get_center(self) -> ndarray[Any, dtype[floating[Any]]] | tuple[float, float, float]:
        return self.circle.get_center()


class PositiveCharge(Charge):
    def __init__(self, **kwargs):
        super().__init__(1, RED, **kwargs)


class NegativeCharge(Charge):
    def __init__(self, **kwargs):
        super().__init__(-1, BLUE, **kwargs)
