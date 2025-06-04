from manim import *

# Color Palette
TITLE_COLOR = WHITE
TEXT_COLOR = GREY_B  # For annotations and general text
LABEL_COLOR = WHITE # For C, B, E labels, +/- on battery etc.
NPN_SYMBOL_COLOR = BLUE_D
WIRE_COLOR = GREY_A
LED_OFF_COLOR = GREY_C
LED_ON_COLOR = GREEN_C
LED_BORDER_COLOR = WHITE
LED_INTERNAL_SYMBOL_COLOR = GREY_A # Color for the diode symbol inside LED

BATTERY_PLATE_COLOR = WHITE
RESISTOR_COLOR = WHITE # Color for resistor symbol

CURRENT_BLOCKED_COLOR = RED_D
BASE_CURRENT_COLOR = YELLOW_C
MAIN_CURRENT_COLOR = GREEN_B # Collector-Emitter current


class TransistorSwitchExplanation(Scene):
    def construct(self):
        self.camera.background_color = "#2E2E2E" # Dark grey background

        # Scene 1: Title
        scene1_bundle = self._animate_scene1_title()
        self.wait(1.5)

        # Transition from Title to Scene 2
        self.play(FadeOut(scene1_bundle["all_elements"]))
        self.wait(0.5)

        # Scene 2: Intro NPN & OFF State
        scene2_bundle = self._animate_scene2_intro_off_state()
        self.wait(3) # Time to absorb OFF state

        # Scene 3: Turning Transistor ON
        scene3_bundle = self._animate_scene3_on_state(scene2_bundle)
        self.wait(3) # Time to absorb ON state

        # Transition from Scene 3 to Scene 4 (Amplification Text)
        elements_to_fade_s3 = VGroup(
            scene3_bundle["base_current_control_text"],
            scene3_bundle["main_current_text"],
            scene3_bundle["led_on_text"]
        )
        self.play(FadeOut(elements_to_fade_s3))
        self.wait(0.5)
        
        # Scene 4: Amplification (Simplified)
        scene4_bundle = self._animate_scene4_amplification(scene3_bundle)
        self.wait(2)

        # Transition to Summary
        circuit_elements_to_fade = VGroup(
            scene2_bundle["npn_bjt"], scene2_bundle["led"], scene2_bundle["battery"],
            scene2_bundle["resistor_led"], scene2_bundle["wires"], scene2_bundle["component_labels"],
            scene3_bundle["base_current_switch_group"], # Switch and base resistor
            scene4_bundle["all_elements"] # Amplification text and current labels
        )
        # Note: Current flashes are transient animations, not persistent Mobjects unless explicitly made so.
        # If current paths (like base_current_path_highlight) were added to scene, include them too.
        self.play(FadeOut(circuit_elements_to_fade))
        self.wait(0.5)

        # Scene 5: Summary/Outro
        self._animate_scene5_summary()
        self.wait(3) # End scene wait

    def _animate_scene1_title(self):
        title = Text("How a Transistor Works as a Switch", font_size=48, color=TITLE_COLOR)
        subtitle = Text("A Visual Explanation", font_size=28, color=GREY_B).next_to(title, DOWN, buff=0.3)

        bg_npn_symbol = self._create_npn_bjt_symbol(scale=2.5, colors={"npn": GREY_D, "text": GREY_D})
        bg_npn_symbol.set_opacity(0.15).to_corner(DR, buff=-0.5)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.5), run_time=1.5)
        self.play(FadeIn(bg_npn_symbol), run_time=1)
        
        return {"all_elements": VGroup(title, subtitle, bg_npn_symbol)}

    def _animate_scene2_intro_off_state(self):
        npn_bjt = self._create_npn_bjt_symbol(scale=1.2, label_scale=0.6).move_to(ORIGIN + RIGHT*0.5)
        battery_obj = self._create_battery_symbol(scale=0.8, label_scale=0.5).move_to(LEFT * 4.5 + DOWN * 0.5)
        
        # Position LED relative to NPN collector
        led_pos = npn_bjt.get_collector_terminal() + UP * 2.0 + LEFT*0.2
        led_obj = self._create_led_symbol(scale=0.7, is_on=False).move_to(led_pos)
        resistor_led = self._create_resistor_symbol(scale=0.6).next_to(led_obj, LEFT, buff=0.5)

        power_source_label = Text("Power Source", font_size=20, color=TEXT_COLOR).next_to(battery_obj, DOWN, buff=0.3)
        load_label = Text("Load (LED)", font_size=20, color=TEXT_COLOR).next_to(VGroup(led_obj, resistor_led), UP, buff=0.3)
        
        wire_bat_pos_to_res = Line(battery_obj.get_positive_terminal_attach_point(), resistor_led.get_left_terminal(), color=WIRE_COLOR)
        wire_res_to_led = Line(resistor_led.get_right_terminal(), led_obj.get_left_terminal(), color=WIRE_COLOR)
        wire_led_to_C = Line(led_obj.get_right_terminal(), npn_bjt.get_collector_terminal(), color=WIRE_COLOR)
        wire_E_to_bat_neg = Line(npn_bjt.get_emitter_terminal(), battery_obj.get_negative_terminal_attach_point(), color=WIRE_COLOR)

        wires = VGroup(wire_bat_pos_to_res, wire_res_to_led, wire_led_to_C, wire_E_to_bat_neg)
        component_labels = VGroup(power_source_label, load_label)

        self.play(
            Create(npn_bjt.symbol_only), 
            LaggedStart(*[Write(label) for label in npn_bjt.submobjects[1:]]), # Labels C, B, E
            run_time=2
        )
        self.play(
            LaggedStart(
                FadeIn(battery_obj), FadeIn(led_obj), FadeIn(resistor_led),
                Create(wires), Write(component_labels),
            ),
            run_time=3
        )
        
        off_state_text = Text("No Base Current (OFF State)", font_size=24, color=YELLOW_C).to_corner(UL, buff=0.5)
        blocked_X = Cross(npn_bjt.symbol_only[1]).scale(0.8).set_color(CURRENT_BLOCKED_COLOR) # X on the NPN bar

        self.play(Write(off_state_text), FadeIn(blocked_X), run_time=1.5)
        
        return {
            "npn_bjt": npn_bjt, "led": led_obj, "battery": battery_obj, 
            "resistor_led": resistor_led, "wires": wires, "component_labels": component_labels,
            "off_state_text": off_state_text, "blocked_X": blocked_X
        }

    def _animate_scene3_on_state(self, scene2_bundle):
        # Unpack needed elements from scene2
        npn_bjt, led, battery, resistor_led, wires = \
            scene2_bundle["npn_bjt"], scene2_bundle["led"], scene2_bundle["battery"], \
            scene2_bundle["resistor_led"], scene2_bundle["wires"]
        
        self.play(FadeOut(scene2_bundle["off_state_text"]), FadeOut(scene2_bundle["blocked_X"]))

        base_control_label = Text("Small Base Current Applied", font_size=24, color=YELLOW_C).to_corner(UL, buff=0.5)
        
        base_switch_origin = npn_bjt.get_base_terminal() + LEFT * 2.5 + UP * 0.3
        base_resistor_obj = self._create_resistor_symbol(scale=0.4).move_to(npn_bjt.get_base_terminal() + LEFT*1.2)
        wire_sw_to_res = Line(base_switch_origin, base_resistor_obj.get_left_terminal(), color=WIRE_COLOR)
        wire_res_to_B = Line(base_resistor_obj.get_right_terminal(), npn_bjt.get_base_terminal(), color=WIRE_COLOR)
        
        sw_dot1 = Dot(base_switch_origin + LEFT*0.2, radius=0.05, color=WIRE_COLOR)
        sw_dot2 = Dot(base_switch_origin + RIGHT*0.2, radius=0.05, color=WIRE_COLOR)
        sw_lever = Line(sw_dot1.get_center(), base_switch_origin + LEFT*0.2 + UP*0.2, color=WIRE_COLOR) # Open
        
        base_current_switch_group = VGroup(base_resistor_obj, wire_sw_to_res, wire_res_to_B, sw_dot1, sw_dot2, sw_lever)
        
        self.play(Write(base_control_label), FadeIn(base_current_switch_group))
        self.play(sw_lever.animate.put_start_and_end_on(sw_dot1.get_center(), sw_dot2.get_center()), run_time=0.5) # Close switch

        base_current_path = VGroup(wire_sw_to_res, base_resistor_obj.get_wire_path_representation(), wire_res_to_B)
        base_current_flash_anim = ShowPassingFlash(
            base_current_path.copy().set_stroke(color=BASE_CURRENT_COLOR, width=5),
            time_width=0.4, run_time=1.5
        )
        self.play(base_current_flash_anim)

        self.play(npn_bjt.symbol_only[1].animate.set_stroke(color=GREEN_C, opacity=0.7), run_time=0.5) # NPN bar 'opens'

        main_current_text = Text("Collector-Emitter Current Flows (ON State)", font_size=22, color=GREEN_C).next_to(base_control_label, DOWN, buff=0.3, aligned_edge=LEFT)
        
        path_bat_to_res = wires[0]
        path_res_internal = resistor_led.get_wire_path_representation()
        path_res_to_led = wires[1]
        path_led_internal = led.get_internal_path_representation()
        path_led_to_C = wires[2]
        path_npn_internal = Line(npn_bjt.get_collector_terminal(), npn_bjt.get_emitter_terminal(), stroke_opacity=0) # Simple internal path
        path_E_to_bat = wires[3]

        main_current_flash_anims = Succession(
            ShowPassingFlash(path_bat_to_res.copy().set_stroke(color=MAIN_CURRENT_COLOR, width=7), time_width=0.3, run_time=0.4),
            ShowPassingFlash(path_res_internal.copy().set_stroke(color=MAIN_CURRENT_COLOR, width=7), time_width=0.2, run_time=0.3),
            ShowPassingFlash(path_res_to_led.copy().set_stroke(color=MAIN_CURRENT_COLOR, width=7), time_width=0.3, run_time=0.4),
            ShowPassingFlash(path_led_internal.copy().set_stroke(color=MAIN_CURRENT_COLOR, width=7), time_width=0.2, run_time=0.3),
            ShowPassingFlash(path_led_to_C.copy().set_stroke(color=MAIN_CURRENT_COLOR, width=7), time_width=0.3, run_time=0.4),
            ShowPassingFlash(path_npn_internal.copy().set_stroke(color=MAIN_CURRENT_COLOR, width=7), time_width=0.2, run_time=0.3),
            ShowPassingFlash(path_E_to_bat.copy().set_stroke(color=MAIN_CURRENT_COLOR, width=7), time_width=0.4, run_time=0.5),
        )
        
        led_on_text = Text("LED Lights Up!", font_size=22, color=LED_ON_COLOR).next_to(led, UP, buff=0.3)
        anim_led_on = led.fill_circle.animate.set_fill(color=LED_ON_COLOR, opacity=0.8)

        self.play(Write(main_current_text))
        self.play(main_current_flash_anims, anim_led_on, Write(led_on_text), run_time=2.6)

        # For Scene 4 and fading out:
        # The actual paths (not animations) that were highlighted
        base_current_path_highlight = base_current_path.copy() # Store for Scene 4
        main_circuit_path_highlight = VGroup(path_bat_to_res, path_res_internal, path_res_to_led, path_led_internal, path_led_to_C, path_npn_internal, path_E_to_bat).copy()

        return {
            "base_current_control_text": base_control_label, "main_current_text": main_current_text,
            "led_on_text": led_on_text, "base_current_switch_group": base_current_switch_group,
            "base_current_path_obj": base_current_path_highlight, 
            "main_current_path_obj": main_circuit_path_highlight
        }

    def _animate_scene4_amplification(self, scene3_bundle):
        base_current_path_obj = scene3_bundle["base_current_path_obj"]
        main_current_path_obj = scene3_bundle["main_current_path_obj"]

        amplification_text = Text("Small Base signal controls large C-E current", font_size=28, color=TEXT_COLOR).to_edge(UP)
        self.play(Write(amplification_text))

        # Re-run flashes for emphasis, or use Indicate on the path objects if they were made persistent.
        # Assuming ShowPassingFlash is transient, we re-animate.
        base_flash = ShowPassingFlash(
            base_current_path_obj.copy().set_stroke(color=BASE_CURRENT_COLOR, width=5),
            time_width=0.4, run_time=1.5,
        )
        main_flash = ShowPassingFlash(
            main_current_path_obj.copy().set_stroke(color=MAIN_CURRENT_COLOR, width=8), # Thicker for "large"
            time_width=0.5, run_time=2.0,
        )
        
        label_small_current = Text("Small Input", font_size=20, color=BASE_CURRENT_COLOR).next_to(base_current_path_obj, UP, buff=0.2)
        # Find a good spot for large current label, e.g. near collector part of main path
        main_path_sample_point = main_current_path_obj.submobjects[4].get_center() # path_led_to_C
        label_large_current = Text("Large Output", font_size=20, color=MAIN_CURRENT_COLOR).next_to(main_path_sample_point, DOWN, buff=0.3)

        self.play(
            AnimationGroup(base_flash, FadeIn(label_small_current, shift=RIGHT*0.2), lag_ratio=0.5),
            AnimationGroup(main_flash, FadeIn(label_large_current, shift=UP*0.2), lag_ratio=0.7),
            run_time=2.5
        )
        
        return {"all_elements": VGroup(amplification_text, label_small_current, label_large_current)}

    def _animate_scene5_summary(self):
        summary_text1 = Text("Key Takeaway:", font_size=32, color=TITLE_COLOR).to_edge(UP, buff=1.0)
        summary_text2 = Text("Transistor acts as an electrically controlled switch.", font_size=28, color=GREY_A).next_to(summary_text1, DOWN, buff=0.4)
        summary_text3 = Text("Tiny signal, big control!", font_size=28, color=YELLOW_C).next_to(summary_text2, DOWN, buff=0.4)

        self.play(Write(summary_text1))
        self.play(FadeIn(summary_text2, shift=UP*0.2))
        self.play(FadeIn(summary_text3, shift=UP*0.2))
        self.wait(1)
        
        quick_npn = self._create_npn_bjt_symbol(scale=0.8).move_to(LEFT*1.5)
        quick_led = self._create_led_symbol(scale=0.5, is_on=False).move_to(RIGHT*1.5)
        loop_elements = VGroup(quick_npn, quick_led).next_to(summary_text3, DOWN, buff=1.0)
        self.play(FadeIn(loop_elements))

        for _ in range(2):
            self.play(
                Indicate(quick_npn.get_base_terminal_obj(), color=YELLOW_C, scale_factor=1.2),
                quick_led.fill_circle.animate.set_fill(color=LED_ON_COLOR, opacity=0.8),
                run_time=0.6
            )
            self.wait(0.2)
            self.play(
                quick_led.fill_circle.animate.set_fill(color=LED_OFF_COLOR, opacity=0.7),
                run_time=0.6
            )
            self.wait(0.2)
        
        self.play(FadeOut(VGroup(summary_text1, summary_text2, summary_text3, loop_elements)), run_time=1)

    # Helper Mobject Creation Methods
    def _create_npn_bjt_symbol(self, scale=1.0, label_scale=0.5, colors=None):
        c = colors if colors else {"npn": NPN_SYMBOL_COLOR, "text": LABEL_COLOR}
        s_parts = VGroup()
        circle = Circle(radius=0.7*scale, color=c["npn"], stroke_width=3)
        bar_cx = -0.1*scale 
        bar = Line([bar_cx, 0.4*scale, 0], [bar_cx, -0.4*scale, 0], color=c["npn"], stroke_width=3)
        b_s, b_e = bar.get_center(), bar.get_center() + LEFT*0.6*scale
        b_line = Line(b_s, b_e, color=c["npn"], stroke_width=3)
        c_s, c_e = bar.get_top(), bar.get_top() + normalize(UR)*0.7*scale
        c_line = Line(c_s, c_e, color=c["npn"], stroke_width=3)
        e_s, e_e = bar.get_bottom(), bar.get_bottom() + normalize(DR)*0.7*scale
        e_line = Arrow(e_s, e_e, buff=0, tip_length=0.2*scale, color=c["npn"], stroke_width=3)
        s_parts.add(circle, bar, b_line, c_line, e_line)

        cl = MathTex("C",color=c["text"]).scale(label_scale).next_to(c_e,UR,buff=0.1*scale)
        bl = MathTex("B",color=c["text"]).scale(label_scale).next_to(b_e,LEFT,buff=0.1*scale)
        el = MathTex("E",color=c["text"]).scale(label_scale).next_to(e_e,DR,buff=0.1*scale)
        
        group = VGroup(s_parts, cl, bl, el)
        group.symbol_only = s_parts
        group.get_collector_terminal = lambda: c_line.get_end()
        group.get_base_terminal = lambda: b_line.get_end()
        group.get_base_terminal_obj = lambda: b_line # For Indicate target
        group.get_emitter_terminal = lambda: e_line.get_end()
        return group

    def _create_led_symbol(self, scale=1.0, is_on=False, colors=None):
        c = colors if colors else {"on": LED_ON_COLOR, "off": LED_OFF_COLOR, "border": LED_BORDER_COLOR, "symbol": LED_INTERNAL_SYMBOL_COLOR}
        fill_clr = c["on"] if is_on else c["off"]
        outer_c = Circle(radius=0.5*scale, color=c["border"], stroke_width=2)
        fill_c = Circle(radius=0.48*scale, stroke_width=0, fill_color=fill_clr, fill_opacity=0.7)
        tri_pts = [[-0.2*scale,0.2*scale,0],[-0.2*scale,-0.2*scale,0],[0.1*scale,0,0]]
        tri = Polygon(*tri_pts, stroke_width=0, fill_color=c["symbol"], fill_opacity=1)
        cath_line = Line([0.1*scale,0.2*scale,0],[0.1*scale,-0.2*scale,0],color=c["symbol"],stroke_width=max(1,2*scale/0.7)) # Scale stroke width
        diode_s = VGroup(tri, cath_line).move_to(outer_c.get_center())

        group = VGroup(fill_c, outer_c, diode_s)
        group.fill_circle = fill_c
        group.get_left_terminal = lambda: group.get_center() + LEFT*0.5*scale
        group.get_right_terminal = lambda: group.get_center() + RIGHT*0.5*scale
        group.get_internal_path_representation = lambda: Line(group.get_left_terminal(), group.get_right_terminal(), stroke_opacity=0)
        return group

    def _create_battery_symbol(self, scale=1.0, label_scale=0.5, colors=None):
        c = colors if colors else {"plate": BATTERY_PLATE_COLOR, "text": LABEL_COLOR}
        sep, lph, sph = 0.2*scale, 0.5*scale, 0.3*scale
        l_plate = Line(UP*lph/2, DOWN*lph/2, stroke_width=max(1.5,2.5*scale/0.8)).shift(LEFT*sep/2)
        s_plate = Line(UP*sph/2, DOWN*sph/2, stroke_width=max(3,5*scale/0.8)).shift(RIGHT*sep/2)
        l_plate.set_color(c["plate"]); s_plate.set_color(c["plate"])
        plus = Tex("+",color=c["text"]).scale(label_scale).next_to(l_plate,LEFT,buff=0.1*scale)
        minus = Tex("-",color=c["text"]).scale(label_scale).next_to(s_plate,RIGHT,buff=0.1*scale)
        group = VGroup(l_plate, s_plate, plus, minus)
        group.get_positive_terminal_attach_point = lambda: l_plate.get_center()
        group.get_negative_terminal_attach_point = lambda: s_plate.get_center()
        return group

    def _create_resistor_symbol(self, scale=1.0, color=RESISTOR_COLOR):
        w, h, wl = 0.6*scale, 0.25*scale, 0.3*scale
        body = Rectangle(width=w, height=h, color=color, stroke_width=max(1,2*scale/0.6))
        win = Line(LEFT*(w/2+wl), LEFT*w/2, color=color, stroke_width=max(1,2*scale/0.6))
        wout = Line(RIGHT*w/2, RIGHT*(w/2+wl), color=color, stroke_width=max(1,2*scale/0.6))
        group = VGroup(body, win, wout)
        group.get_left_terminal = lambda: win.get_start()
        group.get_right_terminal = lambda: wout.get_end()
        group.get_wire_path_representation = lambda: Line(win.get_start(), wout.get_end(), stroke_opacity=0) # For flash path
        return group