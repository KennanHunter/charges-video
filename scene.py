from manim import *

from shared.charge_point import PositiveCharge, NegativeCharge
from shared.electrostatic_scene import ElectrostaticScene


class IntroduceCharges(ElectrostaticScene):
    def construct(self):
        positive = PositiveCharge()
        negative = NegativeCharge()

        self.add_rigid_charge(positive)
        self.add_floating_charge(negative)

        positive.generate_target()
        positive.target.move_to(LEFT*2.5)

        self.play(Create(positive))
        self.play(MoveToTarget(positive))

        negative.generate_target()

        negative.target.move_to(RIGHT*2.5)

        self.play(Create(negative))
        self.play(MoveToTarget(negative))

        negative.generate_target()
        negative.target.text.set_opacity(0)
        negative.target.scale(0.5)

        positive.generate_target()
        positive.target.text.set_opacity(0)
        positive.target.scale(0.5)

        for point, force in self.compute_forces():
            print(point, force)

            force = np.multiply(force, 10)

            start = point.get_center()
            end = np.add(start, [force[0], force[1], 0])

            vector = Arrow(start, end)
            point.set_vector(vector)

            self.bring_to_front(point)

            self.play(GrowArrow(vector))


class Point(MovingCameraScene):
    def construct(self):
        positive = PositiveCharge()

        self.play(Create(positive))

        positive.generate_target()

        positive.target.move_to(LEFT*2.5)

        self.play(MoveToTarget(positive))

        negative = NegativeCharge()

        negative.generate_target()

        negative.target.move_to(RIGHT*2.5)

        self.play(Create(negative))
        self.play(MoveToTarget(negative))

        negative.generate_target()
        negative.target.text.set_opacity(0)
        negative.target.scale(0.25)

        positive.generate_target()
        positive.target.text.set_opacity(0)
        positive.target.scale(0.25)

        self.play(MoveToTarget(negative), MoveToTarget(positive))

        positive.generate_target()
        positive.target.move_to(ORIGIN)

        grid = Axes(
            x_range=(-4, 4, 0.5),
            y_range=(-4, 4, 0.5),
            x_length=8,
            y_length=8,
        )

        self.add_foreground_mobjects(positive, negative)
        self.play(Create(grid), MoveToTarget(positive))


class CulombsLaw(Scene):
    def construct(self):
        axes = Axes(
            x_range=(0, 11, 1),
            y_range=(0, 4, 1),
            x_length=11,
            y_length=4,
            y_axis_config={
                "include_numbers": True,
            },
        ).move_to(LEFT*1.1)

        labels = axes.get_axis_labels(
            Text("Displacement").scale(0.45), Text("Force").scale(0.45)
        )

        self.play(Create(axes))
        self.play(Create(labels))

        plot = axes.plot(
            lambda x: 1 / x ** 2,
            x_range=[0.5, 10.7],
            color=RED,
        )

        self.play(Create(plot))
        # self.play(FadeIn(d1))
        # self.play(MoveAlongPath(d1, plot))

        inverted_plot = axes.plot(
            lambda x: 0.01 * x ** 2,
            x_range=[0.5, 10.7],
            color=RED,
        )

        inverted_labels = axes.get_axis_labels(
            Text("Inverse of Displacement").scale(
                0.45), Text("Force").scale(0.45)
        )

        self.play(Wait(1))

        self.play(Transform(plot, inverted_plot),
                  Transform(labels, inverted_labels))

        linearized_plot = axes.plot(
            lambda x: 0.1 * x,
            x_range=[0.5, 10.7],
            color=RED,
        )

        linearized_labels = axes.get_axis_labels(
            Tex(r"$\frac{1}{\sqrt{x}}$").scale(
                1), Text("Force (N)").scale(0.45)
        )

        self.play(Transform(plot, linearized_plot),
                  Transform(labels, linearized_labels))

        self.play(Wait(1))
