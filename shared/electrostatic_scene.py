from manim import *
import math
from shared.charge_point import *


class ElectrostaticScene(Scene):
    def __init__(self, **kwargs):
        """An Abstract object for gravity.

        Parameters
        ----------
        gravity
            The direction and strength of gravity.
        """
        super().__init__(**kwargs)

        self.rigid_charges: List[Charge] = []
        self.floating_charges: List[Charge] = []

    def add_rigid_charge(self, charge: Charge):
        self.rigid_charges.append(charge)

    def add_floating_charge(self, charge: Charge):
        self.floating_charges.append(charge)

    def simulate():
        pass

    def get_charges(self) -> list[Charge]:
        return self.rigid_charges + self.floating_charges

    def compute_forces(self):
        charge_forces = []

        for charge in self.get_charges():
            # x, y
            force = [0.0, 0.0]
            for factor_charge in self.get_charges():
                delta_x = charge.get_x() - factor_charge.get_x()
                delta_y = charge.get_y() - factor_charge.get_y()

                if delta_x:
                    force_x = abs(charge.magnitude *
                                  factor_charge.magnitude) / delta_x ** 2
                else:
                    force_x = 0

                if delta_y:
                    force_y = abs(charge.magnitude *
                                  factor_charge.magnitude) / delta_y ** 2
                else:
                    force_y = 0

                force[0] += force_x
                force[1] += force_y

            charge_forces.append(force)

        return zip(self.get_charges(), charge_forces)
