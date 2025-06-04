from manim import *
import random
import numpy as np

# Helper function to create a consistent title
def create_title(scene, text):
    title = Text(text, font_size=36, weight=BOLD)
    title.to_edge(UP)
    scene.play(Write(title))
    scene.wait(0.5)
    return title

# Helper function for application text
def show_application(scene, app_text_str, position_relative_to=None, direction=DOWN, wait_time=2):
    app_text = Text(app_text_str, font_size=24, t2c={"EPFO": YELLOW, "Social Security": YELLOW})
    if position_relative_to:
        app_text.next_to(position_relative_to, direction, buff=0.5)
    else:
        app_text.center().shift(DOWN*1.5)
    scene.play(FadeIn(app_text, shift=UP*0.5))
    scene.wait(wait_time)
    return app_text

class IntroScene(Scene):  # <--- THIS IS THE CLASS
    def construct(self):
        main_title = Text("AI in Social Security", font_size=48, weight=BOLD)
        subtitle = Text("Visualizing Core Techniques & Applications", font_size=32).next_to(main_title, DOWN, buff=0.3)
        epfo_mention = Text("(Inspired by EPFO Use Cases)", font_size=24, slant=ITALIC).next_to(subtitle, DOWN, buff=0.5)

        self.play(Write(main_title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.play(FadeIn(epfo_mention, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(main_title), FadeOut(subtitle), FadeOut(epfo_mention))
        self.wait(0.5)

class LinearRegressionScene(Scene):
    def construct(self):
        title = create_title(self, "1. Linear Regression")
        
        axes = Axes(
            x_range=[0, 10, 2],    # x_min, x_max, x_step
            y_range=[0, 10, 2],    # y_min, y_max, y_step
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 20, "tip_shape": StealthTip}, # Added tip_shape for arrows
            # x_axis_config and y_axis_config can be used for more specific styling
            # e.g., x_axis_config={"label_direction": DOWN},
            # y_axis_config={"label_direction": LEFT}
        ).center().shift(UP*0.5)

        # Create and position axis labels manually
        x_label = axes.get_x_axis_label(
            Tex("Economic Indicators", font_size=24), 
            edge=DOWN, direction=DOWN, buff=0.4
        )
        y_label = axes.get_y_axis_label(
            Tex("PF Contributions", font_size=24).rotate(90 * DEGREES), 
            edge=LEFT, direction=LEFT, buff=0.4
        )
        
        # You can also create labels and position them relative to the axes:
        # x_label_tex = Tex("Economic Indicators", font_size=20).next_to(axes.x_axis, DOWN, buff=0.3)
        # y_label_tex = Tex("PF Contributions", font_size=20).next_to(axes.y_axis, LEFT, buff=0.3).rotate(PI/2)


        # Scatter plot data
        scatter_points_coords = [(1,1.5), (2,3), (3,2.5), (4,4.5), (5,4), (6,6.5), (7,5.5), (8,8), (9,7.5)]
        scatter_points = VGroup(*[Dot(axes.c2p(x,y), color=BLUE) for x,y in scatter_points_coords])

        # Regression line
        line = axes.plot(lambda x: 0.8 * x + 0.8, color=GREEN)
        line_label_text = Tex("Prediction Line", font_size=20, color=GREEN).next_to(line, UR, buff=0.1)

        self.play(Create(axes), Write(x_label), Write(y_label)) # Add labels to the scene with axes
        self.play(LaggedStart(*[Create(dot) for dot in scatter_points], lag_ratio=0.1))
        self.play(Create(line), Write(line_label_text))
        self.wait(1)

        # Group axes and labels for easier FadeOut if desired, or fade individually
        axes_and_labels = VGroup(axes, x_label, y_label)

        app_text = show_application(self, "• Forecasting Contribution Trends", position_relative_to=axes_and_labels)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(axes_and_labels), FadeOut(scatter_points), FadeOut(line), FadeOut(line_label_text), FadeOut(app_text))

class ClassificationScene(Scene):
    def construct(self):
        title = create_title(self, "2. Classification")

        # Data points for two classes
        class1_coords = [(1,1), (1.5,2), (2,1.2), (0.5, 1.8)]
        class2_coords = [(3,3), (3.5,2.5), (2.8,3.5), (4, 3.2)]
        
        class1_dots = VGroup(*[Dot(point=np.array([x-2,y-1,0]), color=BLUE) for x,y in class1_coords])
        class2_dots = VGroup(*[Dot(point=np.array([x-2,y-1,0]), color=RED) for x,y in class2_coords])
        all_dots = VGroup(class1_dots, class2_dots).center().shift(UP*0.5)

        self.play(LaggedStart(
            *[GrowFromCenter(dot) for dot in class1_dots],
            *[GrowFromCenter(dot) for dot in class2_dots],
            lag_ratio=0.1
        ))
        self.wait(0.5)

        # Classifier line
        line = Line(LEFT*1.5+DOWN*0.5, RIGHT*1.5+UP*0.5, color=GREEN, stroke_width=6).shift(UP*0.5)
        self.play(Create(line))
        self.wait(1)

        # Example application: Document Sorting
        doc_icons = VGroup()
        docs_data = [
            ("📄 Form 19", BLUE_C),
            ("📄 Aadhaar", GREEN_C),
            ("📄 PAN", ORANGE),
            ("📄 Bank Stmt.", PURPLE_A)
        ]
        for i, (text, color) in enumerate(docs_data):
            doc_icon = Text(text, font_size=20, color=color).shift(DOWN*1.5 + LEFT*3 + RIGHT*i*1.8)
            doc_icons.add(doc_icon)
        
        bins = VGroup()
        bin_labels_text = ["Withdrawal Docs", "KYC Docs"]
        for i in range(2):
            bin_rect = Rectangle(width=2.5, height=1, color=WHITE).shift(DOWN*2.5 + LEFT*1.5 + RIGHT*i*3)
            bin_label = Text(bin_labels_text[i], font_size=18).next_to(bin_rect, UP, buff=0.1)
            bins.add(VGroup(bin_rect, bin_label))

        app_title_doc_sort = Text("• Automated Document Sorting:", font_size=24).next_to(title, DOWN, buff=0.8).align_to(title, LEFT)
        self.play(FadeOut(all_dots), FadeOut(line))
        self.play(Write(app_title_doc_sort))
        self.play(FadeIn(doc_icons))
        self.play(Create(bins))
        
        self.play(
            doc_icons[0].animate.move_to(bins[0][0].get_center()+UP*0.1), # Form 19 to Withdrawal
            doc_icons[1].animate.move_to(bins[1][0].get_center()+UP*0.1), # Aadhaar to KYC
            doc_icons[2].animate.move_to(bins[1][0].get_center()+DOWN*0.1),# PAN to KYC
            doc_icons[3].animate.move_to(bins[0][0].get_center()+DOWN*0.1) # Bank Stmt might be for withdrawal proof
        )
        self.wait(2)
        self.play(FadeOut(title), FadeOut(app_title_doc_sort), FadeOut(doc_icons), FadeOut(bins))

class AnomalyDetectionScene(Scene):
    def construct(self):
        title = create_title(self, "3. Anomaly Detection")

        # Normal data points
        normal_points = VGroup()
        for _ in range(30):
            point = Dot(
                [random.uniform(-1,1), random.uniform(-0.5,0.5), 0], 
                color=BLUE_C, radius=0.05
            ).shift(UP*0.5)
            normal_points.add(point)
        
        # Anomalous points
        anomaly1 = Dot([2.5, 1.5, 0], color=RED, radius=0.1).shift(UP*0.5)
        anomaly2 = Dot([-2, -1.2, 0], color=RED, radius=0.1).shift(UP*0.5)
        anomalies = VGroup(anomaly1, anomaly2)

        self.play(LaggedStart(*[Create(p) for p in normal_points], lag_ratio=0.05))
        self.play(LaggedStart(*[GrowFromCenter(a) for a in anomalies], lag_ratio=0.5))
        
        highlight_circles = VGroup(*[Circle(radius=0.3, color=YELLOW, stroke_width=3).move_to(a.get_center()) for a in anomalies])
        self.play(LaggedStart(*[Create(c) for c in highlight_circles], lag_ratio=0.3))
        self.wait(1)

        app_text = show_application(self, "• Fraudulent Claim Detection (e.g., unusual patterns)", position_relative_to=normal_points)

        self.wait(2)
        self.play(FadeOut(title), FadeOut(normal_points), FadeOut(anomalies), FadeOut(highlight_circles), FadeOut(app_text))

class NLPScene(Scene):
    def construct(self):
        title = create_title(self, "4. Natural Language Processing (NLP)")

        # Chatbot visual
        user_bubble_text = Text("My PF Balance?", font_size=24)
        # Ensure "speech_bubble.svg" is in the same directory as your script,
        # or in an "assets" subdirectory (e.g., "assets/speech_bubble.svg")
        svg_path = "speech_bubble.svg" # or "scenes/speech_bubble.svg" if in scenes dir or "assets/speech_bubble.svg"
        try:
            user_bubble = SVGMobject(svg_path).stretch_to_fit_height(1).stretch_to_fit_width(2.5)
        except Exception as e:
            self.logger.warning(f"Could not load {svg_path}: {e}. Using fallback Rectangle.")
            user_bubble = Rectangle(width=3, height=1, color=BLUE_D).round_corners(0.2)
        
        user_bubble.next_to(ORIGIN, LEFT, buff=0.5).shift(UP*1)
        user_bubble_text.move_to(user_bubble.get_center())
        user_chat = VGroup(user_bubble, user_bubble_text)

        ai_bubble_text = Text("Your PF balance is ₹XXXXX.", font_size=24)
        try:
            ai_bubble = SVGMobject(svg_path).stretch_to_fit_height(1).stretch_to_fit_width(3.5)
        except Exception as e:
            self.logger.warning(f"Could not load {svg_path}: {e}. Using fallback Rectangle.")
            ai_bubble = Rectangle(width=4, height=1, color=GREEN_D).round_corners(0.2)

        ai_bubble.next_to(ORIGIN, RIGHT, buff=0.5).shift(DOWN*0.2)
        ai_bubble_text.move_to(ai_bubble.get_center())
        ai_chat = VGroup(ai_bubble, ai_bubble_text)

        chatbot_icon = Text("🤖", font_size=48).move_to(ORIGIN+UP*0.4)

        self.play(FadeIn(user_chat, shift=RIGHT))
        self.play(Write(chatbot_icon))
        self.wait(0.5)
        self.play(Transform(chatbot_icon, chatbot_icon.copy().set_color(YELLOW))) # Thinking
        self.play(Transform(chatbot_icon, chatbot_icon.copy().set_color(WHITE)))
        self.play(FadeIn(ai_chat, shift=LEFT))
        self.wait(1)
        
        all_chat_elements = VGroup(user_chat, chatbot_icon, ai_chat).move_to(ORIGIN+UP*0.5)

        app_text = show_application(self, "• AI Chatbots / Virtual Assistants for member queries", position_relative_to=all_chat_elements)

        self.wait(2)
        self.play(FadeOut(title), FadeOut(all_chat_elements), FadeOut(app_text))

class OCRScene(Scene):
    def construct(self):
        title = create_title(self, "6. Optical Character Recognition (OCR)")

        # Scanned document visual
        doc_image = Rectangle(width=3, height=4, color=GRAY, fill_opacity=0.2).shift(LEFT*2.5 + UP*0.3)
        doc_lines = VGroup()
        for i in range(5):
            line = Line(doc_image.get_corner(UL)+RIGHT*0.2+DOWN*(0.5+i*0.6), 
                        doc_image.get_corner(UR)+LEFT*0.2+DOWN*(0.5+i*0.6), 
                        color=DARK_GRAY, stroke_width=2)
            doc_lines.add(line)
        doc_visual = VGroup(doc_image, doc_lines)
        doc_label = Text("Scanned Form", font_size=20).next_to(doc_visual, UP)

        # Extracted text visual
        extracted_text_str = """Name: John Doe
UAN: 123456789012
Date: 01/01/2024""" # Using a more compact string for Text mobject
        
        extracted_text = Text(
            extracted_text_str, 
            font_size=18, 
            font="Monospace", # Try "DejaVu Sans Mono" if "Monospace" fails
            t2w={"Name:": BOLD, "UAN:": BOLD, "Date:": BOLD} # Use t2w for BOLD
        )
        extracted_text.next_to(doc_visual, RIGHT, buff=1).align_to(doc_visual, UP)
        text_label = Text("Extracted Data", font_size=20).next_to(extracted_text, UP)

        arrow = Arrow(doc_visual.get_right(), extracted_text.get_left(), buff=0.2, color=YELLOW)
        ocr_engine_text = Text("OCR Engine", font_size=18).next_to(arrow, UP, buff=0.1)

        self.play(FadeIn(doc_visual, doc_label))
        self.play(Create(arrow), Write(ocr_engine_text))
        self.play(Write(extracted_text), Write(text_label))
        self.wait(1)

        ocr_group = VGroup(doc_visual, doc_label, arrow, ocr_engine_text, extracted_text, text_label)
        app_text = show_application(self, "• Automated Data Entry from scanned KYC/Claim Forms", position_relative_to=ocr_group)

        self.wait(2)
        self.play(FadeOut(title), FadeOut(ocr_group), FadeOut(app_text))

class RAGScene(Scene):
    def construct(self):
        title = create_title(self, "10. Retrieval Augmented Generation (RAG)")

        # Components
        query_text = Text("User: Complex rule query?", font_size=20)
        query_box = SurroundingRectangle(query_text, buff=0.2, color=BLUE)
        query_group = VGroup(query_text, query_box).shift(LEFT*4 + UP*1.5)

        llm_icon = Text("🧠 LLM", font_size=28, color=PURPLE_A).shift(UP*1.5)
        
        db_icon = SVGMobject("database.svg").scale(0.5) # Or use a simple cylinder
        if not hasattr(db_icon, 'points'): # Fallback
            db_icon = VGroup(Ellipse(width=1, height=0.3, color=GRAY, fill_opacity=1).shift(UP*0.3),
                             Rectangle(width=1, height=0.6, color=GRAY, fill_opacity=1).shift(DOWN*0.0),
                             Ellipse(width=1, height=0.3, color=GRAY, fill_opacity=1).shift(DOWN*0.3)
                             ).scale(0.7)
        db_icon.shift(RIGHT*3.5 + UP*1.5)
        db_label = Text("EPFO Knowledge Base\n(Circulars, FAQs)", font_size=16).next_to(db_icon, DOWN)
        knowledge_base = VGroup(db_icon, db_label)

        response_text = Text("AI: Accurate, context-aware answer.", font_size=20)
        response_box = SurroundingRectangle(response_text, buff=0.2, color=GREEN)
        response_group = VGroup(response_text, response_box).shift(DOWN*1)

        # Arrows
        arrow_query_to_llm = Arrow(query_group.get_right(), llm_icon.get_left(), buff=0.2)
        arrow_llm_to_db = Arrow(llm_icon.get_right(), db_icon.get_left(), buff=0.2, path_arc=-0.5*PI)
        retrieved_info_text = Text("Retrieve relevant info", font_size=14).next_to(arrow_llm_to_db, DOWN, buff=0.05)
        arrow_db_to_llm = Arrow(db_icon.get_left(), llm_icon.get_right(), buff=0.2, path_arc=-0.5*PI) # conceptually info goes back
        
        arrow_llm_to_response = Arrow(llm_icon.get_bottom(), response_group.get_top(), buff=0.2)
        generate_text = Text("Generate contextual response", font_size=14).next_to(arrow_llm_to_response, RIGHT, buff=0.05)

        self.play(FadeIn(query_group))
        self.play(Write(llm_icon))
        self.play(Create(arrow_query_to_llm))
        self.wait(0.5)
        self.play(FadeIn(knowledge_base))
        self.play(Create(arrow_llm_to_db), Write(retrieved_info_text))
        self.wait(0.5)
        # Show info going back to LLM (can be same arrow animated or conceptual)
        self.play(Indicate(db_icon, color=YELLOW), Indicate(llm_icon, color=YELLOW)) # Simple indication
        self.wait(0.5)
        self.play(FadeIn(response_group, shift=UP*0.5), Create(arrow_llm_to_response), Write(generate_text))
        self.wait(1)

        rag_group = VGroup(query_group, llm_icon, knowledge_base, retrieved_info_text, response_group, generate_text,
                           arrow_query_to_llm, arrow_llm_to_db, arrow_llm_to_response)
        app_text = show_application(self, "• Context-Aware Chatbots using EPFO knowledge", position_relative_to=response_group, direction=DOWN*1.5)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(rag_group), FadeOut(app_text))


class GraphModelsScene(Scene):
    def construct(self):
        title = create_title(self, "11. Graph Models (GNNs)")

        # Define nodes (entities)
        # Members (M), Employers (E), Bank Accounts (B), Addresses (A)
        nodes_data = {
            "M1": {"pos": [-3, 1, 0], "color": BLUE_C, "label": "M1"},
            "M2": {"pos": [-3, -1, 0], "color": BLUE_C, "label": "M2"},
            "M3": {"pos": [0, 2, 0], "color": RED_C, "label": "M3 (Fraud)"}, # Part of fraud ring
            "M4": {"pos": [3, 1.5, 0], "color": BLUE_C, "label": "M4"},
            
            "E1": {"pos": [-1, 0, 0], "color": GREEN_C, "label": "E1"},
            "E2": {"pos": [1.5, -1.5, 0], "color": RED_C, "label": "E2 (Shell)"}, # Part of fraud ring
            
            "B1": {"pos": [-0.5, -2, 0], "color": ORANGE, "label": "B1"},
            "B2": {"pos": [1, 0.5, 0], "color": RED_C, "label": "B2 (Shared)"}, # Part of fraud ring
            
            "A1": {"pos": [2.5, -0.5, 0], "color": PURPLE_A, "label": "A1 (Shared)"} # Part of fraud ring
        }

        vertices = list(nodes_data.keys())
        edges = [
            ("M1", "E1"), ("M2", "E1"), ("M1", "B1"),
            ("M3", "E1"), ("M3", "B2"), # M3 linked to E1 (legit) and B2 (fraud)
            ("M4", "E2"), # M4 linked to shell company
            ("E2", "B2"), ("E2", "A1"), # Shell E2 linked to shared B2 and A1
            ("M3", "A1")  # M3 also linked to shared A1
        ]
        
        layout = {node: data["pos"] for node, data in nodes_data.items()}
        
        graph = Graph(
            vertices,
            edges,
            layout=layout,
            labels=True,
            vertex_config={v: {"fill_color": nodes_data[v]["color"], "radius": 0.3} for v in vertices},
            edge_config={"stroke_width": 2}
        )
        graph.scale(0.9).shift(UP*0.2)

        # Adjust label positions to avoid overlap if needed
        for i, v_name in enumerate(vertices):
            graph.vertices[v_name].label = Text(nodes_data[v_name]["label"], font_size=18).move_to(graph.vertices[v_name].get_center())


        self.play(Create(graph))
        self.wait(1)

        # Highlight the fraud ring
        fraud_ring_nodes = ["M3", "E2", "B2", "A1"]
        fraud_ring_edges_tuples = [("M3", "B2"), ("M3", "A1"), ("E2", "B2"), ("E2", "A1"), ("M4", "E2")] # M4 is victim/pawn
        
        highlight_anims = []
        for node_key in fraud_ring_nodes:
            highlight_anims.append(Indicate(graph.vertices[node_key], color=RED, scale_factor=1.5))
        
        # Get edge mobjects to highlight
        # Note: Manim's graph edge access might require specific tuple order or use graph.edges
        # This is a robust way to get the mobject for an edge
        edge_mobjects_to_highlight = []
        for u, v in fraud_ring_edges_tuples:
            if (u,v) in graph.edges:
                edge_mobjects_to_highlight.append(graph.edges[(u,v)])
            elif (v,u) in graph.edges:
                edge_mobjects_to_highlight.append(graph.edges[(v,u)])

        for edge_mob in edge_mobjects_to_highlight:
            highlight_anims.append(Indicate(edge_mob, color=RED, scale_factor=1.2))

        if highlight_anims:
            self.play(AnimationGroup(*highlight_anims, lag_ratio=0.1))
        self.wait(1)
        
        app_text_str = "• Advanced Fraud Detection: Identifying collusive fraud rings"
        app_text = show_application(self, app_text_str, position_relative_to=graph)

        self.wait(2)
        self.play(FadeOut(title), FadeOut(graph), FadeOut(app_text))

# To render specific scenes:
# manim -pql your_script_name.py LinearRegressionScene NLPScene
# To render all scenes in order:
# manim -pql your_script_name.py IntroScene LinearRegressionScene ClassificationScene AnomalyDetectionScene NLPScene OCRScene RAGScene GraphModelsScene