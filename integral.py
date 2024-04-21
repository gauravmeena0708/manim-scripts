from manim import *

class IntegralSolution(Scene):
    def construct(self):
        # Define the integral expression
        integral_expression = MathTex(r"\int \frac{1}{x^2 - x + 1} \, dx")
        self.play(FadeIn(integral_expression))
        self.wait(2)

        # Show completing the square process
        square_part = MathTex(r" + \frac{1}{4}")
        completed_square = MathTex(r"\left(x - \frac{1}{2}\right)^2 + \frac{3}{4}")

        integral_expression.to_edge(LEFT)
        self.play(Write(square_part.next_to(integral_expression, RIGHT)))
        self.wait(1)
        self.play(FadeOut(square_part), integral_expression.animate.to_corner(UL))
        self.play(Write(completed_square))
        self.wait(2)

        # Introduce arctan function
        arctan_func = MathTex(r"\arctan \left( \sqrt{\frac{3}{4}} \left(x - \frac{1}{2}\right) \right)")
        arctan_func_mob = arctan_func.next_to(integral_expression, DOWN)
        integral_result = MathTex(r"\frac{2}{3} \sqrt{3} \arctan \left( \frac{2}{3} \sqrt{3} \cdot x - \frac{1}{3} \sqrt{3} \right) + C")
        integral_result_mob = integral_result.scale(0.8).to_corner(UR)

        self.play(FadeOut(completed_square), integral_expression.animate.scale(0.8).to_corner(UL))
        self.play(Write(arctan_func), Write(arctan_func_mob))
        self.wait(2)
        self.play(FadeOut(arctan_func), FadeOut(arctan_func_mob), Write(integral_result), Write(integral_result_mob))
        self.wait(2)

"""
# Run the animation
if __name__ == "__main__":
    integral_animation = IntegralSolution()
    integral_animation.render()

"""

class IntegralSolution2(Scene):
    def construct(self):
        # Define the integral expression
        integral_expression = MathTex(r"\int \frac{1}{x^2 - x + 1} \, dx")
        self.play(FadeIn(integral_expression))
        self.wait(2)

        # Show completing the square process (unchanged)
        square_part = MathTex(r" + \frac{1}{4}")
        completed_square = MathTex(r"\left(x - \frac{1}{2}\right)^2 + \frac{3}{4}")

        integral_expression.to_edge(LEFT)
        self.play(Write(square_part.next_to(integral_expression, RIGHT)))
        self.wait(1)
        self.play(FadeOut(square_part), integral_expression.animate.to_corner(UL))
        self.play(Write(completed_square))
        self.wait(2)

        # Decompose the integral
        decomposed_integral = MathTex(r"\int \frac{1}{(x - \frac{1}{2})^2 + (\frac{\sqrt{3}}{2})^2} \, dx")
        self.play(FadeOut(completed_square), integral_expression.animate.scale(0.8).shift(DOWN))
        self.play(Write(decomposed_integral.next_to(integral_expression, DOWN)))
        self.wait(2)

        # Introduce arctan function (unchanged)
        arctan_func = MathTex(r"\arctan \left( \sqrt{\frac{3}{4}} \left(x - \frac{1}{2}\right) \right)")
        arctan_func_mob = arctan_func.next_to(integral_expression, DOWN)
        integral_result = MathTex(r"\frac{2}{3} \sqrt{3} \arctan \left( \frac{2}{3} \sqrt{3} \cdot x - \frac{1}{3} \sqrt{3} \right) + C")
        integral_result_mob = integral_result.scale(0.8).to_corner(UR)

        self.play(FadeOut(decomposed_integral), Write(arctan_func), Write(arctan_func_mob))
        self.wait(2)

        # Antiderivative
        antiderivative = MathTex(r"\frac{1}{\sqrt{3}} \arctan \left( \frac{x - \frac{1}{2}}{\frac{\sqrt{3}}{2}} \right) + C")
        self.play(FadeOut(arctan_func, arctan_func_mob), Write(antiderivative.next_to(integral_expression, DOWN)))
        self.wait(2)

        # Substitute back
        temp_substitution = MathTex(r"\frac{1}{\sqrt{3}} \arctan \left( \frac{u}{\frac{\sqrt{3}}{2}} \right) + C")
        substitute_text = MathTex(r"{where} \quad u = x - \frac{1}{2}")
        temp_substitution_mob = temp_substitution.next_to(integral_expression, DOWN)
        substitute_text_mob = substitute_text.scale(0.7).next_to(temp_substitution_mob, DOWN)

        self.play(FadeOut(antiderivative), Write(temp_substitution), Write(substitute_text), Write(substitute_text_mob))
        self.wait(2)

        # Final result
        self.play(FadeOut(temp_substitution, substitute_text, substitute_text_mob), Write(integral_result), Write(integral_result_mob))
        self.wait(2)

class IntegralSolution3(Scene):
    def construct(self):
        # Define the integral expression
        integral_expression = MathTex(r"\int \frac{1}{x^2 - x + 1} \, dx")
        self.play(FadeIn(integral_expression))
        self.wait(2)

        # Show completing the square process
        square_part = MathTex(r" + \frac{1}{4}")
        completed_square = MathTex(r"\left(x - \frac{1}{2}\right)^2 + \frac{3}{4}")

        # Show adding and subtracting 1/4 inside the integral
        integral_expression_copy = integral_expression.copy()
        self.play(integral_expression_copy.animate.scale(0.8).to_corner(UL))
        self.play(Write(square_part.next_to(integral_expression_copy, RIGHT)))
        self.wait(2)
        
        # Combine expressions and show final form
        self.play(FadeOut(integral_expression_copy), integral_expression.animate.scale(1).move_to(ORIGIN))
        self.play(Write(completed_square.next_to(integral_expression, RIGHT)))
        self.wait(2)

        # Decompose the integral
        decomposed_integral = MathTex(r"\int \frac{1}{(x - \frac{1}{2})^2 + (\frac{\sqrt{3}}{2})^2} \, dx")
        self.play(FadeOut(completed_square), integral_expression.animate.scale(0.8).shift(DOWN))
        self.play(Write(decomposed_integral.next_to(integral_expression, DOWN)))
        self.wait(2)

        # Introduce arctan function (unchanged)
        arctan_func = MathTex(r"\arctan \left( \sqrt{\frac{3}{4}} \left(x - \frac{1}{2}\right) \right)")
        arctan_func_mob = arctan_func.next_to(integral_expression, DOWN)
        integral_result = MathTex(r"\frac{2}{3} \sqrt{3} \arctan \left( \frac{2}{3} \sqrt{3} \cdot x - \frac{1}{3} \sqrt{3} \right) + C")
        integral_result_mob = integral_result.scale(0.8).to_corner(UR)

        self.play(FadeOut(decomposed_integral), Write(arctan_func), Write(arctan_func_mob))
        self.wait(2)

        # Antiderivative
        antiderivative = MathTex(r"\frac{1}{\sqrt{3}} \arctan \left( \frac{x - \frac{1}{2}}{\frac{\sqrt{3}}{2}} \right) + C")
        self.play(FadeOut(arctan_func, arctan_func_mob), Write(antiderivative.next_to(integral_expression, DOWN)))
        self.wait(2)

        # Substitute back
        temp_substitution = MathTex(r"\frac{1}{\sqrt{3}} \arctan \left( \frac{u}{\frac{\sqrt{3}}{2}} \right) + C")
        substitute_text = MathTex(r"{where} \quad u = x - \frac{1}{2}")
        temp_substitution_mob = temp_substitution.next_to(integral_expression, DOWN)
        substitute_text_mob = substitute_text.scale(0.7).next_to(temp_substitution_mob, DOWN)

        self.play(FadeOut(antiderivative), Write(temp_substitution), Write(substitute_text), Write(substitute_text_mob))
        self.wait(2)

        # Final result
        self.play(FadeOut(temp_substitution, substitute_text, substitute_text_mob), Write(integral_result), Write(integral_result_mob))
        self.wait(2)

class IntegralSolution4(Scene):
    def construct(self):
        # Define integral expressions
        integral_expression1 = MathTex(r"\int \frac{1}{x^2 - x + 1} \, dx")
        integral_expression2 = MathTex(r"\int \frac{1}{x^2 - x + \frac{1}{4} + \frac{3}{4}} \, dx")
        integral_expression3 = MathTex(r"\int \frac{1}{(x - \frac{1}{2})^2 + (\frac{\sqrt{3}}{2})^2} \, dx")
        integral_expression4 = MathTex(r"\frac{2}{3} \sqrt{3} \arctan \left( \frac{2}{3} \sqrt{3} \cdot x - \frac{1}{3} \sqrt{3} \right) + C")

        # Show integral expressions with writing animation
        self.play(Write(integral_expression1))
        self.wait(2)
        self.play(FadeOut(integral_expression1), Write(integral_expression2))
        self.wait(2)
        self.play(FadeOut(integral_expression2), Write(integral_expression3))
        self.wait(2)
        self.play(FadeOut(integral_expression3), Write(integral_expression4))
        self.wait(2)

class IntegralSolution5(Scene):
    def construct(self):
        # Latex expressions
        exp1 = MathTex(r" \int \frac{1}{x^2 - x + 1} \, dx")
        exp2 = MathTex(r" \int \frac{1}{x^2 - x + \frac{1}{4} + \frac{3}{4}} \, dx")
        exp3 = MathTex(r" \int \frac{1}{x^2 - 2 (\frac{1}{2}) x + \frac{1}{4} + \frac{3}{4}} \, dx")
        exp4 = MathTex(r" \int \frac{1}{(x - \frac{1}{2})^2 + (\frac{\sqrt{3}}{2})^2} \, dx")
        
        sub1 = MathTex(r"\text{Let } x - \frac{1}{2} = u ")
        sub2 = MathTex(r"\Rightarrow dx = du")
        exp5 = MathTex(r"\Rightarrow \int \frac{1}{(u)^2 + (\frac{\sqrt{3}}{2})^2} \, du")
        
        sub3 = MathTex(r"\text{When } \int \frac{1}{a^2+u^2} \, du")
        sub4 = MathTex(r"\Rightarrow \frac{1}{a} \cdot \arctan\left(\frac{u}{a}\right)")
        
        exp6 = MathTex(r"\Rightarrow \frac{1}{\frac{\sqrt(3)}{2}} \cdot \arctan\left(\frac{(x - \frac{1}{2})}{\frac{\sqrt(3)}{2}}\right)")
        exp7 = MathTex(r"\Rightarrow \frac{2}{\sqrt(3)} \cdot \arctan\left(\frac{2(x - \frac{1}{2})}{\sqrt(3)}\right)")
                       
        #sub1 = MathTex(r"\text{Let } x - \frac{1}{2} = \tan(\theta)")
        #sub2 = MathTex(r"\text{Why? } (x - \frac{1}{2})^2 + \left( \frac{\sqrt{3}}{2} \right)^2 = \sec^2(\theta)", font_size=24)
        #exp5 = MathTex(r" \int \frac{1}{\sec^2(\theta)} \, d\theta")
        #solution = MathTex(r"\frac{2}{3} \sqrt{3} \arctan \left( \frac{2}{3} \sqrt{3} \cdot x - \frac{1}{3} \sqrt{3} \right) + C")

        # Arrange expressions
        exp1.to_edge(UP)
        exp2.to_edge(LEFT)
        exp3.next_to(exp2, DOWN)
        exp4.to_edge(LEFT)
        sub1.next_to(exp4, DOWN, buff=1)
        sub2.next_to(sub1, RIGHT)
        
        sub3.next_to(exp4, DOWN, buff=1)
        sub4.next_to(sub3, RIGHT)
        exp5.next_to(exp4, RIGHT)
        exp6.next_to(exp4, RIGHT)
        exp7.next_to(exp4, RIGHT)
        #exp5.next_to(sub2, LEFT)
        #solution.next_to(exp5, LEFT)

        # Show expressions
        #self.play(Write(integral))
        #self.play(Write(integral_comp1))
        #self.play(Write(integral_comp2))
        self.play(Write(exp1))
        self.wait(2)
        self.play(Write(exp1))
        self.wait(2)
        self.play(Write(exp2))
        self.wait(2)
        
        self.play(TransformMatchingTex(exp1, exp3))
        self.wait(2)
        
        self.play(TransformMatchingTex(exp1, exp4))
        self.wait(2)

        # Explain substitution
        self.play(Write(sub1))
        self.wait(1)
        self.play(Write(sub2))
        self.wait(2)
        
        self.play(Write(exp5))
        self.wait(2)
        
        self.play(FadeOut(sub2))
        self.wait(2)
        
        self.play(Transform(sub1,sub3))
        self.wait(2)
        
        self.play(Write(sub4))
        self.wait(2)
        
        self.play(FadeOut(exp5))
        self.play(FadeOut(sub1))
        self.play(Transform(sub4,exp6))
        self.wait(2)
        
        #FadeOut(exp6)
        self.play(Transform(sub4,exp7))
        self.wait(2)



        self.wait(2)  # Wait for 2 seconds at the end

from manim import *

class IISC2(Scene):
    def construct(self):
        # Set a maximum width for text to prevent overflow
        MAX_WIDTH = 9  # Adjust this value based on your screen size

        # Introductory text with line breaks for wrapping
        text1 = Text("This was a problem of probability in IISC interview!", color=WHITE).scale(0.8)  # Scale down to fit
        text2 = Text("Problem: 100 Dice are thrown at once, what is the probability of getting", t2c={'Problem':YELLOW}).scale(0.5)
        #text4 = Text("Hello world", t2w={'Problem':YELLOW})
        text3 = Text("1. Exactly one 4.").scale(0.5)
        text4 = Text("2. At most one 4.").scale(0.5)

        text1.move_to(UP * 3.5)  # Adjust vertical position of text1
        text2.next_to(text1, DOWN)
        text3.next_to(text2, DOWN)
        text4.next_to(text3, DOWN)
        
        self.play(Write(text1))
        self.wait(2)
        
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(FadeOut(text2), FadeOut(text4), text3.animate.next_to(text1, DOWN))
        self.wait(2)  # Wait for 2 seconds after intro text
        
        # Create MathTex object with the formula
        formula1 = MathTex(
            r"P(\text{Exactly one 4}) = ",
            r"{100 \choose 1}",  # Binomial coefficient
            r"\left(\frac{1}{6}\right)^1",  # Probability of getting 4
            r"\left(\frac{5}{6}\right)^{99}"  # Probability of not getting 4 for the remaining rolls
        )

        # Align the parts of the formula
        formula1.arrange(direction=RIGHT)

        # Add the formula to the scene
        self.play(Write(formula1))

        # Add a wait time
        self.wait(3)
        
        self.remove(formula1,text3)
        self.play(Write(text4))
        self.play(text4.animate.next_to(text1, DOWN))
        # Create MathTex object with the formula
        formula2 = MathTex(
            r"P(\text{At most one 4}) = ",
            r"\sum_{k=0}^{1} {100 \choose k}",  # Binomial coefficient
            r"\left(\frac{1}{6}\right)^k",  # Probability of getting k 4s
            r"\left(\frac{5}{6}\right)^{100-k}"  # Probability of not getting 4 for the remaining rolls
        )

        # Align the parts of the formula
        formula2.arrange(direction=RIGHT)

        # Add the formula to the scene
        self.play(Write(formula2))

        # Add a wait time
        self.wait(3)