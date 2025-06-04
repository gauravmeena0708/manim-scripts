from manim import *
import numpy as np
from sklearn.linear_model import LinearRegression

class LinearRegressionScene(Scene):
    def construct(self):
        # Configuration
        axes_color = WHITE
        data_point_color = BLUE
        line_color = YELLOW
        forecast_color = GREEN
        prediction_point_color = RED

        # Sample Data (Time, Contribution Amount)
        raw_data = np.array([
            [1, 10], [2, 15], [3, 13], [4, 18], [5, 22],
            [6, 20], [7, 25], [8, 23]
        ])

        x_data = raw_data[:, 0].reshape(-1, 1)
        y_data = raw_data[:, 1]

        # Perform linear regression
        model = LinearRegression()
        model.fit(x_data, y_data)
        # y_pred_initial = model.predict(x_data) # Not used currently

        # Title
        title = Text("Linear Regression Visualization").to_edge(UP)
        self.play(Write(title))

        # Create Axes
        ax = Axes(
            x_range=[0, 12, 2],  # Extended for forecast
            y_range=[0, 40, 5],
            x_length=10,
            y_length=6,
            axis_config={"color": axes_color, "include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT},
        ).add_coordinates()

        x_axis_label = ax.get_x_axis_label(Text("Time", font_size=24))
        y_axis_label = ax.get_y_axis_label(Text("Contribution Amount", font_size=24).rotate(90 * DEGREES, axis=OUT))

        axes_group = VGroup(ax, x_axis_label, y_axis_label).scale(0.8).to_edge(DOWN, buff=1)
        self.play(Create(axes_group))

        # Historical Data Label
        historical_data_label = Text("Historical Data", font_size=24).next_to(ax, UP, buff=0.2, aligned_edge=LEFT)
        self.play(Write(historical_data_label))

        # Create data points
        dots = VGroup()
        for x_val, y_val in raw_data:
            dot = Dot(ax.coords_to_point(x_val, y_val), color=data_point_color, radius=0.08)
            dots.add(dot)
        self.play(LaggedStart(*[Create(d) for d in dots], lag_ratio=0.2))
        self.wait(0.5)

        # Regression Line Label
        regression_line_label = Text("Regression Line", font_size=24).next_to(historical_data_label, RIGHT, buff=1.0)
        self.play(Write(regression_line_label))

        initial_slope = (y_data[1] - y_data[0]) / (x_data[1,0] - x_data[0,0]) if len(x_data)>1 else 0
        initial_intercept = y_data[0] - initial_slope * x_data[0,0] if len(x_data)>0 else np.mean(y_data)

        slope_tracker = ValueTracker(initial_slope if len(x_data)>0 else 0) # Ensure non-empty data for initial slope/intercept
        intercept_tracker = ValueTracker(initial_intercept if len(x_data)>0 else np.mean(y_data) if len(y_data)>0 else 0)


        line_graph = always_redraw(
            lambda: ax.plot(
                lambda x: slope_tracker.get_value() * x + intercept_tracker.get_value(),
                x_range=[float(ax.x_range[0]), float(ax.x_range[1])],
                color=line_color
            )
        )

        self.play(Create(line_graph))
        self.wait(0.5)

        # Animate to the actual regression line
        self.play(
            slope_tracker.animate.set_value(model.coef_[0]),
            intercept_tracker.animate.set_value(model.intercept_),
            run_time=2
        )
        self.wait(1)

        # Forecast
        forecast_label = Text("Forecasted Value", font_size=24).next_to(regression_line_label, RIGHT, buff=1.0)
        self.play(Write(forecast_label))

        forecast_x = 10  # Example forecast time point
        forecast_y = model.predict(np.array([[forecast_x]]))[0]

        forecast_dot = Dot(ax.coords_to_point(forecast_x, forecast_y), color=prediction_point_color, radius=0.1)
        # Ensure label text is a string
        forecast_dot_label_text = f"Pred: ({forecast_x}, {forecast_y:.1f})"
        forecast_dot_label = Text(forecast_dot_label_text, font_size=20)
        forecast_dot_label.next_to(forecast_dot, RIGHT, buff=0.2)

        h_line = DashedLine(
            ax.coords_to_point(ax.x_range[0], forecast_y), # Start from y-axis
            ax.coords_to_point(forecast_x, forecast_y),
            color=GREY
        )
        v_line = DashedLine(
            ax.coords_to_point(forecast_x, ax.y_range[0]), # Start from x-axis
            ax.coords_to_point(forecast_x, forecast_y),
            color=GREY
        )

        self.play(Create(h_line), Create(v_line))
        self.play(Create(forecast_dot), Write(forecast_dot_label))

        self.play(Flash(forecast_dot, color=WHITE, line_length=0.2, num_lines=10, flash_radius=0.2, time_width=0.3, run_time=1.5))

        self.wait(3)
# End of script - removed the erroneous triple backticks
