from manim import *
import random

class ClassificationScene(Scene):
    def construct(self):
        # Title
        title = Text("Classification Demonstration").to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Define categories and their properties
        categories = {
            "Category A (Circles)": {"shape": Circle, "color": BLUE, "items": []},
            "Category B (Squares)": {"shape": Square, "color": GREEN, "items": []},
            "Category C (Triangles)": {"shape": Triangle, "color": YELLOW, "items": []},
        }
        category_keys = list(categories.keys())

        num_items_per_category = 4
        item_scale = 0.5

        # Central area for unsorted items
        unsorted_area_center = ORIGIN + DOWN * 0.5
        unsorted_label = Text("Unsorted Items", font_size=24).next_to(unsorted_area_center, UP, buff=1.5).shift(LEFT*4)
        self.play(Write(unsorted_label))

        # Create and place unsorted items
        unsorted_items_group = VGroup()
        for cat_key in category_keys:
            details = categories[cat_key]
            for _ in range(num_items_per_category):
                item = details["shape"](color=details["color"]).scale(item_scale)
                # Randomly position in a small area
                item.move_to(unsorted_area_center + np.array([random.uniform(-1, 1), random.uniform(-0.5, 0.5), 0]))
                details["items"].append(item) # Keep track of items per category
                unsorted_items_group.add(item)

        # Shuffle for visual randomness before initial display
        unsorted_items_group.shuffle()
        self.play(LaggedStart(*[Create(item) for item in unsorted_items_group], lag_ratio=0.1))
        self.wait(1)

        # Create Bins (Categories)
        bin_width = 3
        bin_height = 2
        bin_spacing = 0.5
        total_bins_width = len(categories) * bin_width + (len(categories) - 1) * bin_spacing

        bins_group = VGroup()
        bin_labels_group = VGroup()

        start_x = -total_bins_width / 2 + bin_width / 2

        for i, cat_key in enumerate(category_keys):
            bin_center_x = start_x + i * (bin_width + bin_spacing)
            bin_rect = Rectangle(
                width=bin_width,
                height=bin_height,
                color=WHITE
            ).move_to(np.array([bin_center_x, -2.5, 0])) # Position bins lower

            bin_label = Text(cat_key, font_size=20).next_to(bin_rect, DOWN, buff=0.2)

            categories[cat_key]["bin_rect"] = bin_rect
            categories[cat_key]["bin_center"] = bin_rect.get_center()

            bins_group.add(bin_rect)
            bin_labels_group.add(bin_label)

        self.play(Create(bins_group), Write(bin_labels_group))
        self.wait(0.5)

        # Categorizing label
        categorizing_label = Text("Categorizing Items...", font_size=24).move_to(unsorted_label)
        self.play(ReplacementTransform(unsorted_label, categorizing_label))

        # Animate items moving to bins
        animations = []

        # Store items that belong to each category, to be placed in bins
        # This is done by checking the type of the shape, which is a simple classification rule.

        classified_items_for_bins = {key: [] for key in category_keys}
        for item in unsorted_items_group:
            if isinstance(item, Circle):
                classified_items_for_bins["Category A (Circles)"].append(item)
            elif isinstance(item, Square):
                classified_items_for_bins["Category B (Squares)"].append(item)
            elif isinstance(item, Triangle): # Check for Triangle
                classified_items_for_bins["Category C (Triangles)"].append(item)

        # Calculate target positions within each bin to avoid overlap
        item_padding = 0.2
        items_per_row_in_bin = int(bin_width / (item_scale * 2 + item_padding))
        if items_per_row_in_bin == 0: items_per_row_in_bin = 1 # Ensure at least 1 item per row

        for cat_key, items_in_cat in classified_items_for_bins.items():
            details = categories[cat_key]
            bin_c = details["bin_center"]

            for i, item_to_move in enumerate(items_in_cat):
                row = i // items_per_row_in_bin
                col = i % items_per_row_in_bin

                x_offset = (col - (items_per_row_in_bin -1) / 2.0) * (item_scale * 2 + item_padding)
                # Adjust y_offset to place items from top to bottom
                y_offset = (bin_height / 2.0 - item_scale - item_padding / 2.0) - (row * (item_scale * 2 + item_padding))

                target_pos = bin_c + np.array([x_offset, y_offset, 0])
                animations.append(item_to_move.animate.move_to(target_pos))

        if animations:
             self.play(LaggedStart(*animations, lag_ratio=0.1, run_time=max(1, num_items_per_category * 0.5)))

        categorized_label = Text("Items Categorized", font_size=24).move_to(categorizing_label)
        self.play(ReplacementTransform(categorizing_label, categorized_label))

        self.wait(3)
# Removed offending backticks
