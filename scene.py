from manim import *

from shared.charge_point import PositiveCharge, NegativeCharge
from shared.electrostatic_scene import ElectrostaticScene

config.frame_size = (1080,1920) 

class IntroduceCharges(ElectrostaticScene):
    def construct(self):
        positive = PositiveCharge()
        negative = NegativeCharge()

        self.add_rigid_charge(positive)
        self.add_floating_charge(negative)

        positive.generate_target()
        positive.target.move_to(LEFT*3)

        self.play(Create(positive))
        self.play(MoveToTarget(positive))

        negative.generate_target()

        negative.target.move_to(RIGHT*3)

        self.play(Create(negative))
        self.play(MoveToTarget(negative))


class CulombsLaw(Scene):
    def construct(self):
        axes = Axes(
            x_range=(0, 11, 1),
            y_range=(0, 8, 1),
            x_length=11,
            y_length=8,
            # y_axis_config={
            #     "include_numbers": True,
            # },
        ).move_to(LEFT*1.1)

        displacement_label = Text("d = displacement").scale(1.5).move_to(DOWN * 7)

        labels = axes.get_axis_labels(
            Text("d").scale(1.5), Text("Force").scale(1.5).shift(RIGHT*3)
        )

        self.play(Create(axes))

        self.play(Create(displacement_label))

        self.play(Create(labels))

        plot = axes.plot(
            lambda x: 1 / x ** 2,
            x_range=[0.368, 10.0],
            color=RED,
        )

        self.play(Create(plot))

        inverted_plot = axes.plot(
            lambda x: 0.05 * x ** 2,
            x_range=[0.5, 10.7],
            color=RED,
        )

        inverted_labels = axes.get_axis_labels(
            Tex(r"$\frac{1}{d}$").scale(2.5),
            Text("Force").scale(1.5).shift(RIGHT*3)
        )

        question = Text("How do we relate these values?").move_to(UP*5)

        self.play(Wait(4))
        self.play(Create(question))
        self.play(Wait(12))

        self.play(Transform(plot, inverted_plot),
            Transform(labels, inverted_labels), 
            Uncreate(question))

        linearized_plot = axes.plot(
            lambda x: 0.25 * x,
            x_range=[0.5, 10.7],
            color=RED,
        )

        linearized_labels = axes.get_axis_labels(
            Tex(r"$\frac{1}{\sqrt{d}}$").scale(2.5),
            Text("Force").scale(1.5).move_to(RIGHT*3)
        )


        self.play(Wait(5))

        self.play(Transform(plot, linearized_plot),
                  Transform(labels, linearized_labels))

        self.play(Wait(2))

        slope_form = Tex(r"$y=kx+b$").scale(1.5).move_to(UP * 10)
        y_label = Tex(r"$y = F$").scale(1.5).move_to(UP*9)
        x_label = Tex(r"$x = \frac{1}{\sqrt{d}}$").scale(1.5).move_to(UP*8)
        slope_label = Tex(r"$k = 9\times10^9$""").scale(1.5).move_to(UP*7)

        self.play(Create(slope_form))
        self.play(Create(x_label), Create(y_label))
        self.play(Create(slope_label))

        self.play(Uncreate(axes), 
                  Uncreate(displacement_label), 
                  Uncreate(labels), 
                  Uncreate(plot))
        
        simple_culombs_law = Tex(r"$F = k\frac{1}{d^2}$").scale(4)
        full_culombs_law = Tex(r"$F = k|\frac{q_1q_2}{d^2}|$").scale(4)

        slope_label.generate_target()
        slope_label.target.scale(2.5)
        slope_label.target.move_to(UP*5)

        self.play(Create(simple_culombs_law))
        self.play(Transform(simple_culombs_law, full_culombs_law))

        self.play(Uncreate(slope_form), Uncreate(x_label), Uncreate(y_label), MoveToTarget(slope_label))

        self.play(Wait(5))