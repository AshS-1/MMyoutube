# -*- coding: utf-8 -*-
"""YS03

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mVEoITloA3omPHRF0EewLEKgfRI8h3fn
"""

from manim import *

class YS03(Scene):
    def construct(self):
        # title text
        
        titleText = Text("""
            Mustang Math Tournament 2022:
            Pressure Round Problem 4
            """
        )
        descriptionText = Tex(r"""
        \text{Owen selects an ordered quadruplet of (not necessarily distinct) positive integers $a, b, c, d$ uniformly} 
        \text{ at random such that $a\cdot b \cdot c \cdot d=336.$ If the probability that at least one of $a,b,c,d$}
        \text{is divisible by $14$ can be expressed as a reduced common fraction $\frac{a}{b},$ compute $a + b$.}""", font_size=24).next_to(titleText, DOWN)

        mustangMathLogo = ImageMobject('logo.png').next_to(titleText, UP)
        self.play(FadeIn(mustangMathLogo), Write(
            titleText), Write(descriptionText))
        self.wait(27)

        self.play(FadeOut(titleText), FadeOut(
            descriptionText), FadeOut(mustangMathLogo))
        

        # problem text here

        # self.play(Write(tex))
        # # self.wait(4)
        # #move it up and shrink
        # self.play(tex.animate.shift(UP*3).scale(0.7))

        #factor tree
        num336 = Tex('336').shift(UP*2)
        num16 = Tex('16').shift(LEFT*2+UP)
        num21 = Tex('21').shift(RIGHT*2+UP)
        num2_1 = Tex('2').shift(LEFT*3.5)
        num2_2 = Tex('2').shift(LEFT*2.5)
        num2_3 = Tex('2').shift(LEFT*1.5)
        num2_4 = Tex('2').shift(LEFT*0.5)
        num3 = Tex('3').shift(RIGHT*3)
        num7 = Tex('7').shift(RIGHT)


        #arrows
        arrow1 = Arrow(buff=0.15, start=num336, end=num16, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        arrow2 = Arrow(buff=0.15, start=num336, end=num21, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        arrow3 = Arrow(buff=0.15, start=num21, end=num3, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        arrow4 = Arrow(buff=0.15, start=num21, end=num7, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        arrow5 = Arrow(buff=0.15, start=num16, end=num2_1, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        arrow6 = Arrow(buff=0.15, start=num16, end=num2_2, stroke_width=6, max_tip_length_to_length_ratio=0.15).shift(RIGHT*0.1)
        arrow7 = Arrow(buff=0.15, start=num16, end=num2_3, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        arrow8 = Arrow(buff=0.15, start=num16, end=num2_4, stroke_width=6, max_tip_length_to_length_ratio=0.15)

        #factor tree creation
        factor_tree = VGroup()
        factor_tree.add(arrow1)
        factor_tree.add(arrow2)
        factor_tree.add(arrow3)
        factor_tree.add(arrow4)
        factor_tree.add(arrow5)
        factor_tree.add(arrow6)
        factor_tree.add(arrow6)
        factor_tree.add(arrow7)
        factor_tree.add(arrow8)
        factor_tree.add(num336)
        factor_tree.add(num16)
        factor_tree.add(num21)
        factor_tree.add(num3)
        factor_tree.add(num7)
        factor_tree.add(num2_1)
        factor_tree.add(num2_2)
        factor_tree.add(num2_3)
        factor_tree.add(num2_4)



        self.play(FadeIn(num336))
        self.wait(3)
        self.play(LaggedStart(Create(arrow1),FadeIn(num16),Create(arrow2),FadeIn(num21),Create(arrow3),FadeIn(num3),Create(arrow4),FadeIn(num7),Create(arrow5),FadeIn(num2_1),Create(arrow6),FadeIn(num2_2),Create(arrow7),FadeIn(num2_3),Create(arrow8),FadeIn(num2_4),run_time=6))
        # self.play(Create(arrow1),FadeIn(num16))
        # self.play(Create(arrow2),FadeIn(num21))
        # self.play(Create(arrow3),FadeIn(num3))
        # self.play(Create(arrow4),FadeIn(num7))
        # self.play(Create(arrow5),FadeIn(num2_1))
        # self.play(Create(arrow6),FadeIn(num2_2))
        # self.play(Create(arrow7),FadeIn(num2_3))
        # self.play(Create(arrow8),FadeIn(num2_4))
        self.wait(5)
        
        #remove all but the question
        self.play(FadeOut(factor_tree))
        

        factor_table_1 = Table(
            [["2","3","2","7"],["3","","2",""]],
            col_labels=[Text("a"), Text("b"), Text("c"),Text("d")],

        ).scale(0.5)
        factor_table_2 = Table(
            [["3","2","2","2"],["","7","","2"]],
            col_labels=[Text("a"), Text("b"), Text("c"),Text("d")],

        ).scale(0.5)
        factor_table_3 = Table(
            [["2","2","2","2"],["3","","","7"]],
            col_labels=[Text("a"), Text("b"), Text("c"),Text("d")],

        ).scale(0.5)
        factor_table_4 = Table(
            [["2","7","3","2"],["","2","2",""]],
            col_labels=[Text("a"), Text("b"), Text("c"),Text("d")],

        ).scale(0.5)
        factor_table_5 = Table(
            [["2","2","3","7"],["","","2","2"]],
            col_labels=[Text("a"), Text("b"), Text("c"),Text("d")],

        ).scale(0.5)
        rec = factor_table_5.get_highlighted_cell((2, 3), color=GREY)
        recA = factor_table_5.get_highlighted_cell((2, 4), color=GREEN).set_z_index(-11000)
        recB = factor_table_5.get_highlighted_cell((3, 4), color=GREEN).set_z_index(-11000)
        factor_table_6 = Table(
            [["2","2","3","7"],["","","2","2"],["X","","",""],["X","","",""],["X","","",""]],
            col_labels=[Text("a"), Text("b"), Text("c"),Text("d")],

        ).scale(0.5)

        factor_table_6.add_highlighted_cell((2,3), color=GREY)
        ent = factor_table_6.get_entries_without_labels()
        ent[8].set_color(BLACK)
        ent[12].set_color(BLACK)
        ent[16].set_color(BLACK)
        ent[0].set_color(BLACK)
        ent[1].set_color(BLACK)
        ent[6].set_color(BLACK)
        print(ent[0].get_center())
        two_1 = Text("2").set_z_index(1000).scale(0.5).move_to(factor_table_6.get_cell(pos=(2,1)).get_center())
        two_2 = Text("2").set_z_index(1000).scale(0.5).move_to(factor_table_6.get_cell(pos=(2,2)).get_center())
        two_3 = Text("2").set_z_index(1000).scale(0.5).move_to(factor_table_6.get_cell(pos=(3,3)).get_center())




        self.play(Create(factor_table_1))
        self.wait(1)
        self.play(Transform(factor_table_1,factor_table_2))
        self.wait(1)
        self.remove(factor_table_1)
        
        self.play(Transform(factor_table_2,factor_table_3))
        self.wait(1)
        self.remove(factor_table_2)
        
        self.play(Transform(factor_table_3,factor_table_4))
        self.wait(1)
        self.remove(factor_table_3)

        self.play(Transform(factor_table_4,factor_table_5))
        self.wait(2)
        
        
        self.play(FadeIn(recA,recB))
        self.wait(2.4)
        self.play(Create(rec))
        self.wait(1)
        self.remove(factor_table_4)


        self.play(FadeIn(VGroup(two_1,two_2,two_3)),Transform(factor_table_5,factor_table_6),*[FadeOut(x) for x in [recA,recB,rec]])
        self.wait(14)
        self.play(two_1.animate.move_to(factor_table_6.get_cell(pos=(4,4)).get_center()))
        self.wait(0.2)
        self.play(two_2.animate.move_to(factor_table_6.get_cell(pos=(5,4)).get_center()))
        self.wait(0.2)
        self.play(two_3.animate.move_to(factor_table_6.get_cell(pos=(6,4)).get_center()))
        self.wait(8.4)
        self.play(*[FadeOut(*self.mobjects)])
        
        

        #stars and bars

        sB_2_1 = Tex("2").shift(LEFT*1.5)
        sB_2_2 = Tex("2").shift(LEFT*0.5)
        sB_2_3 = Tex("2").shift(RIGHT*0.5)
        sB_2_4 = Tex("2").shift(RIGHT*1.5)
        bar_1 = MathTex("|").shift(LEFT)
        bar_2 = MathTex("|")
        bar_3 = MathTex("|").shift(RIGHT)

        
        
        #braces
        brA = always_redraw(lambda: BraceBetweenPoints((sB_2_1.get_corner(DOWN+LEFT)+UP*0.02+LEFT*0.2), (bar_1.get_corner(DOWN+RIGHT)+LEFT*0.2+UP*0.1),sharpness=0.8))
        
        texta = Tex("a").scale(0.5).next_to(brA,DOWN*0.7)
        
        texta.add_updater(lambda m: texta.next_to(brA,DOWN*0.7))

        brB = always_redraw(lambda: BraceBetweenPoints((bar_1.get_corner(DOWN+RIGHT)+UP*0.1), (bar_2.get_corner(DOWN+LEFT)+UP*0.1),sharpness=0.8))

        textb = Tex("b").scale(0.5).next_to(brB,DOWN*0.7)

        textb.add_updater(lambda m: textb.next_to(brB,DOWN*0.7))
        

        brC = always_redraw(lambda: BraceBetweenPoints((bar_2.get_corner(DOWN+RIGHT)+UP*0.1), (bar_3.get_corner(DOWN+LEFT)+UP*0.1),sharpness=0.8))
        textc = Tex("c").scale(0.5).next_to(brC,DOWN*0.7)

        textc.add_updater(lambda m: textc.next_to(brC,DOWN*0.7))
        

        brD = always_redraw(lambda: BraceBetweenPoints((bar_3.get_corner(DOWN+RIGHT)+UP*0.1+RIGHT*0.2), (sB_2_4.get_corner(DOWN+RIGHT)+RIGHT*0.2+UP*0.02),sharpness=0.8))

        textd = Tex("d").scale(0.5).next_to(brD,DOWN*0.7)

        textd.add_updater(lambda m: textd.next_to(brD,DOWN*0.7))
        self.play(FadeIn(VGroup(sB_2_1,sB_2_2,sB_2_3,sB_2_4,bar_1,bar_2,bar_3)))
        self.play(
            FadeIn(VGroup(brA,texta)),
            FadeIn(VGroup(brB,textb)),
            FadeIn(VGroup(brC,textc)),
            FadeIn(VGroup(brD,textd)),

        )
        

        
        #combos of numbers for stars and bars
        self.play(
            sB_2_3.animate.move_to([0,0,0]),
            bar_2.animate.move_to([0.5,0,0]),
        )

        self.play(
            sB_2_2.animate.move_to([0.5,0,0]),
            sB_2_3.animate.move_to([1,0,0]),
            bar_1.animate.move_to([-1,0,0]),
            bar_2.animate.move_to([-0.5,0,0]),
            bar_3.animate.move_to([0,0,0]),
        )

        self.play(
            sB_2_2.animate.move_to([0,0,0]),
            sB_2_3.animate.move_to([0.5,0,0]),
            bar_3.animate.move_to([1,0,0]),
        )
        self.remove(brA,brB,brC,brD)
        self.remove(texta,textb,textc,textd)
        self.play(
            sB_2_1.animate.move_to([0,0,0]),
            sB_2_2.animate.move_to([0.5,0,0]),
            sB_2_3.animate.move_to([1,0,0]),
            bar_1.animate.move_to([-1.5,0,0]),
            bar_2.animate.move_to([-1,0,0]),
            bar_3.animate.move_to([-0.5,0,0]),
        )
        
        #7 choose 4 part
        br3 = BraceBetweenPoints((bar_1.get_corner(UP)+DOWN*0.07), (bar_3.get_corner(UP)+DOWN*0.07),direction=UP,sharpness=0.8)
        br4 = BraceBetweenPoints((sB_2_1.get_corner(UP+LEFT)), (sB_2_4.get_corner(UP+RIGHT)),direction=UP,sharpness=0.8)
        text3 = Tex("3").scale(0.5).next_to(br3,UP*0.7)
        text4 = Tex("4").scale(0.5).next_to(br4,UP*0.7)
        self.play(FadeIn(br3),FadeIn(text3),FadeIn(br4),FadeIn(text4))
        self.wait(0.5)

        text3_4 = Tex("4+3").shift(UP*2)
        text3_backup = text3.copy()
        text7 = Tex("7").next_to(text3_4,RIGHT)
        text4_backup = text4.copy()
        binom = MathTex(r"\binom{4+3}{}").shift(UP*2)
        binom2 = MathTex(r"4").shift(UP*1.7)
        self.add(text3_backup,text4_backup)
        self.play(ReplacementTransform(VGroup(text3,text4),binom,))

        highlight = BackgroundRectangle(VGroup(sB_2_1,sB_2_2,sB_2_3,sB_2_4),color=GREEN,fill_opacity=0.7,buff=0.15).set_z_index(-100)
        self.play(FadeIn(highlight))
        self.play(ReplacementTransform(highlight,binom2))
        self.wait(2)
        binom7_4 = VGroup(binom,binom2)
        self.play(binom7_4.animate.shift(LEFT*4),*[FadeOut(m) for m in [br3,br4,text3,text4,text4_backup,text3_backup]])
        
        #6 choose 4
        br2 = BraceBetweenPoints((bar_2.get_corner(UP)+DOWN*0.07), (bar_3.get_corner(UP)+DOWN*0.07),direction=UP,sharpness=0.8)
        br4_2 = BraceBetweenPoints((sB_2_1.get_corner(UP+LEFT)), (sB_2_4.get_corner(UP+RIGHT)),direction=UP,sharpness=0.8)
        text2 = Tex("2").scale(0.5).next_to(br2,UP*0.7)
        text4_2 = Tex("4").scale(0.5).next_to(br4_2,UP*0.7)

        self.play(FadeIn(br2),FadeIn(text2),FadeIn(br4_2),FadeIn(text4_2))
        self.wait(0.5)

        text2_4 = Tex("4+2").shift(UP*2)
        text2_backup = text2.copy()

        text4_2_backup = text4_2.copy()
        binom3 = MathTex(r"\binom{4+2}{}").shift(UP*2)
        binom4 = MathTex(r"4").shift(UP*1.7)
        self.add(text2_backup,text4_2_backup)
        self.play(ReplacementTransform(VGroup(text2,text4_2),binom3,))

        highlight = BackgroundRectangle(VGroup(sB_2_1,sB_2_2,sB_2_3,sB_2_4),color=GREEN,fill_opacity=0.7,buff=0.15).set_z_index(-100)
        self.play(FadeIn(highlight))
        self.play(ReplacementTransform(highlight,binom4))
        self.wait(14.6)
        binom6_4 = VGroup(binom3,binom4)
        
        #clear stuff
        self.play(binom7_4.animate.shift(RIGHT*2.8),binom6_4.animate.shift(RIGHT*1.2),*[FadeOut(m) for m in [br2,br4_2,text2,text4_2,text2_backup,text4_2_backup,sB_2_1,sB_2_2,sB_2_3,sB_2_4,bar_1,bar_2,bar_3]])
        sub = Tex("-").shift(UP*2)
        self.play(FadeIn(sub))
        denom = binom7_4.copy().shift(DOWN*1.8+RIGHT*1.2)
        twenty = Tex("= 20").next_to(binom6_4)
        newTwenty = Tex("20").shift(UP*1.4)
        self.wait(8)
        self.play(FadeIn(twenty))
        self.wait(11)
        
        #simplify  
        self.play(*[FadeOut(m) for m in [binom7_4,binom6_4,sub]],Transform(twenty,newTwenty))
        l = Line((UP+LEFT),(UP+RIGHT),stroke_width=2)
        self.play(FadeIn(denom),FadeIn(l))
        self.wait(3.5)
        # frac = VGroup(binom7_4,binom6_4,denom,l,sub)
        # self.play(frac.animate.shift(LEFT*2))
        self.play(FadeIn(MathTex(r"= \frac{20}{35}").shift(UP*1.05+RIGHT*1.7)))
        self.wait(0.3)

        #final

        frac4_7 = MathTex(r"= \frac{4}{7}").shift(DOWN*2)
        dup = frac4_7.copy()
        self.play(FadeIn(frac4_7))
        self.wait(2)
        self.add(dup)
        sum4_7 = Tex("4+7").shift(DOWN*2+RIGHT*2)
        self.wait(0.9)
        self.play(Transform(frac4_7, sum4_7))
        finalAns = Tex("= 11").next_to(sum4_7)
        self.play(FadeIn(finalAns))
        s=Square().scale(0.3).move_to(finalAns).shift(RIGHT*0.28)
        self.play(Create(s))


        


        self.wait(6)