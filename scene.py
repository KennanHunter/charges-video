from manim import *


class CulombsLaw(MovingCameraScene):
    def construct(self):
        d1 = Dot().set_color(BLUE)

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
            Text("Displacement (m)").scale(0.45), Text("Force (N)").scale(0.45)
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
            Text("Inverse of Displacement (m)").scale(
                0.45), Text("Force (N)").scale(0.45)
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
