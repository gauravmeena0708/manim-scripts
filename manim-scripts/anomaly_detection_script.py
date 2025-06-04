from manim import *

class AnomalyScene(Scene):
    def construct(self):
        # Configuration
        normal_color = GREEN
        anomaly_color = RED
        detection_color = YELLOW
        n_normal_points = 20
        n_anomalies = 3
        animation_run_time = 5  # Shorter for faster rendering in this context

        # Title
        title = Text("Anomaly Detection Visualization").to_edge(UP)
        self.play(Write(title))

        # Label for normal data stream
        normal_stream_label = Text("Normal Data Stream", font_size=30).next_to(title, DOWN, buff=0.5)
        self.play(Write(normal_stream_label))

        # Create normal data points
        normal_points_group = VGroup()
        for i in range(n_normal_points):
            point = Dot(radius=0.1, color=normal_color)
            point.move_to(np.array([-7 + 0.7 * i, 0, 0])) # Spread them out initially
            normal_points_group.add(point)

        self.play(LaggedStart(*[Create(p) for p in normal_points_group], lag_ratio=0.1))

        # Animate normal data points moving like a stream
        self.play(normal_points_group.animate.shift(RIGHT * 14), run_time=animation_run_time, rate_func=linear)
        self.remove(*normal_points_group) # Remove points that moved off screen

        # Introduce anomalies
        anomaly_stream_label = Text("Introducing Anomalies...", font_size=30).move_to(normal_stream_label)
        self.play(ReplacementTransform(normal_stream_label, anomaly_stream_label))

        data_points_mixed = VGroup()
        # Ensure anomaly_indices are within the bounds of n_normal_points
        anomaly_indices = np.random.choice(range(n_normal_points), min(n_anomalies, n_normal_points), replace=False)

        anomaly_objects = []

        for i in range(n_normal_points):
            if i in anomaly_indices:
                point = Dot(radius=0.2, color=anomaly_color) # Larger and red
                anomaly_objects.append(point)
            else:
                point = Dot(radius=0.1, color=normal_color)
            point.move_to(np.array([-7 + 0.7 * i, 0, 0]))
            data_points_mixed.add(point)

        self.play(LaggedStart(*[Create(p) for p in data_points_mixed], lag_ratio=0.1))

        # Animate mixed data points
        self.play(data_points_mixed.animate.shift(RIGHT * 14), run_time=animation_run_time, rate_func=linear)

        # Highlight anomalies after the stream has passed
        # This is a simplified visualization of detection
        highlight_label = Text("Highlighting Anomalies", font_size=30)
        if hasattr(anomaly_stream_label, 'get_center'): # Check if previous label exists
             highlight_label.move_to(anomaly_stream_label)
        else: # Fallback position
            highlight_label.next_to(title, DOWN, buff=0.5)

        self.play(ReplacementTransform(anomaly_stream_label, highlight_label))

        flash_animations = []
        box_animations = []

        # Iterate through the points AT THEIR CURRENT (FINAL) POSITIONS
        for point in data_points_mixed:
            # A simple way to check if a point is an anomaly is by its color.
            # This assumes only anomalies have anomaly_color.
            if point.get_color() == anomaly_color:
                # Flashing effect
                flash_animations.append(Flash(point, color=YELLOW, line_length=0.3, num_lines=12, flash_radius=0.3, time_width=0.3, run_time=1.5))
                # Surrounding box
                box = SurroundingRectangle(point, color=detection_color, buff=0.1)
                box_animations.append(Create(box))

        if flash_animations: # If there are anomalies to highlight
            self.play(LaggedStart(*flash_animations, lag_ratio=0.2), LaggedStart(*box_animations, lag_ratio=0.2))
        else:
            no_anomalies_text = Text("No anomalies to highlight in this pass.", font_size=24).next_to(highlight_label, DOWN)
            self.play(Write(no_anomalies_text))

        self.wait(2)
