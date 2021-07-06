from manim import *
import math

class triangle(Scene):
    def construct(self):
        points = [
            [0,1.5,0],
            [math.sqrt(3),-1.5,0],
            [-math.sqrt(3),-1.5,0]
        ]
        tri = Polygon(*points)
        self.play(Create(tri))
        self.wait(1)


        height = DashedLine([0,-1.5,0],points[0])
        self.play(Create(height))
        self.wait(1)

        points = [
            [0,1.5,0],
            [math.sqrt(3),-1.5,0],
            [0,-1.5,0],
            [-math.sqrt(3),-1.5,0]
        ]
        new_tri0 = VGroup(
            Line(points[0],points[1]).set_color(BLUE),
            Line(points[1],points[2]).set_color(BLUE)
        )
        new_tri1 = VGroup(
            Line(points[0],points[3]).set_color(BLUE),
            Line(points[3],points[2]).set_color(BLUE)
        )
        self.add(new_tri0,new_tri1)
        self.remove(tri)
        self.play(FadeOut(new_tri1,shift=[-1,0,0]))
        self.wait(1)

        sideBrace = BraceBetweenPoints(points[1],points[0])
        labelS = sideBrace.get_text('s')
        baseOverTwoBrace = BraceBetweenPoints([0,-1.5,0],[math.sqrt(3),-1.5,0])
        baseOverTwoTex = baseOverTwoBrace.get_text(r'$\frac{s}{2}$')
        heightBrace = BraceBetweenPoints(points[0],[0,-1.5,0])
        hText = heightBrace.get_text("h")
        tri = VGroup(sideBrace,labelS,baseOverTwoBrace,baseOverTwoTex,heightBrace,hText)
        self.play(Create(tri))
        self.wait(1)

        a = MathTex('a^2').to_edge(LEFT).shift(2*RIGHT)
        plus = MathTex('+').next_to(a,RIGHT)
        b = MathTex('b^2').next_to(plus,RIGHT)
        equals = MathTex('=').next_to(b,RIGHT)
        c = MathTex('c^2').next_to(equals,RIGHT)

        area = MathTex(r'A=\frac{bh}{2}').to_edge(LEFT).shift(2*RIGHT)
        perimeter = MathTex('P=3s').align_to(area,LEFT).shift(DOWN)

        self.play(tri.animate.shift(2*RIGHT),Write(VGroup(a,plus,b,equals,c)),new_tri0.animate.shift(2*RIGHT),height.animate.shift(2*RIGHT))
        self.wait(1)
        self.play(Transform(a,MathTex('h^2').to_edge(LEFT).shift(2*RIGHT)))
        self.wait(1)
        self.play(Transform(b,MathTex(r'\frac{s^2}{4}').next_to(plus,RIGHT)),Transform(c,MathTex(r's^2').next_to(equals,RIGHT)))
        self.wait(1)

        ssquared = MathTex(r'3\frac{s^2}{4}').next_to(plus,RIGHT)

        self.play(ReplacementTransform(VGroup(b,c),ssquared),equals.animate.next_to(a,RIGHT),FadeOut(plus))
        self.wait(1)

        rooth = MathTex(r'\sqrt{h^2}').to_edge(LEFT).shift(2*RIGHT)
        rootequals = MathTex('=').next_to(rooth,RIGHT)
        roots = MathTex(r'\sqrt{3\frac{s^2}{4}}').next_to(rootequals,RIGHT)

        self.play(ReplacementTransform(a,rooth),ReplacementTransform(equals,rootequals),ReplacementTransform(ssquared,roots))
        self.wait(1)

        pmh = MathTex('\pm')
        pms = MathTex('\pm')
        norooth = MathTex('h').next_to(pmh,RIGHT)
        noroots = MathTex(r'\frac{s\sqrt{3}}{2}').next_to(pms,RIGHT)
        VGroup(pmh,norooth).move_to(rooth.get_center())
        VGroup(pms,noroots).move_to(roots.get_center())

        self.play(Transform(rooth,norooth),Transform(roots,noroots),FadeIn(pmh),FadeIn(pms))
        self.wait(1)
        self.play(FadeOut(pmh),FadeOut(pms))
        self.wait(1)
        self.play(roots.animate.next_to(rootequals,RIGHT))
        heighteq = VGroup(rooth,roots,rootequals)
        self.play(heighteq.animate.shift(UP))
        self.wait(1)

        areaA = MathTex('A').to_edge(LEFT).shift(2*RIGHT)
        areaeqhalf = MathTex(r'=\frac{1}{2}').next_to(areaA,RIGHT)
        areab = MathTex('s').next_to(areaeqhalf,RIGHT)
        areah = MathTex('h').next_to(areab)

        pereq = MathTex('P=').to_edge(LEFT).shift(2*RIGHT+DOWN)
        per3 = MathTex('3').next_to(pereq)
        pers = MathTex('s').next_to(per3)

        self.play(Write(VGroup(areaA,areaeqhalf,areah,areab)),Write(VGroup(pereq,per3,pers)))
        self.wait(1)

        self.play(FadeOut(rooth,shift=[0,1,0]),FadeOut(rootequals,shift=[0,1,0]),FadeOut(areah,shift=[0,-1,0]),roots.animate.next_to(areab,RIGHT))
        self.wait(1)

        self.play(Transform(VGroup(pers,areaA),MathTex('s').move_to(areaA.get_center())),per3.animate.next_to(areaA,LEFT),FadeOut(pereq,shift=[0,-1,0]))
        self.wait(1)

        self.play(FadeOut(pers),FadeOut(areab))
        self.wait(1)

        area = MathTex('6').next_to(per3,UP+DOWN)

        self.play(Transform(per3,area),Transform(areaeqhalf,MathTex('=').next_to(areaeqhalf,UP+DOWN)))
        self.wait(1)
        self.play(Transform(per3,MathTex(r'\frac{12}{\sqrt{3}}').next_to(per3,UP+DOWN)),Transform(roots,Tex(r's').next_to(roots,UP+DOWN)))
        self.wait(1)
        self.play(Transform(per3,MathTex('4\sqrt{3}').next_to(per3,UP+DOWN)))
        self.wait(1)

        finaleq = MathTex('s=4\sqrt{3}').to_edge(LEFT).shift(2*RIGHT+UP)
        area = MathTex('A=12\sqrt{3}').to_edge(LEFT).shift(2*RIGHT)
        per  = MathTex('P=12\sqrt{3}').to_edge(LEFT).shift(2*RIGHT+DOWN)

        self.play(Transform(VGroup(roots,areaeqhalf,per3),finaleq))
        self.wait(1)
        self.play(Write(area),Write(per))
        self.wait(1)

class square(Scene):
    def construct(self):
        points = [
            [ 2, 2,0],
            [ 2,-2,0],
            [-2,-2,0],
            [-2, 2,0]
        ]
        square = Polygon(*points)
        self.play(Create(square))
        self.wait(1)

        areaA = MathTex('A').to_edge(LEFT).shift(2*RIGHT+.5*UP)
        areaEq = MathTex('=').next_to(areaA,RIGHT)
        areaS = MathTex('s^2').next_to(areaEq,RIGHT)

        perP = MathTex('P=').to_edge(LEFT).shift(2*RIGHT+.5*DOWN)
        per4 = MathTex('4').next_to(perP,RIGHT)
        perS = MathTex('s').next_to(per4,RIGHT)

        self.play(Write(VGroup(areaA,areaEq,areaS)),Write(VGroup(perP,per4,perS)),square.animate.shift(2*RIGHT))
        self.wait(1)

        self.play(per4.animate.next_to(areaA,LEFT),perS.animate.align_to(areaA,DOWN+LEFT),FadeOut(areaA),FadeOut(perP))
        self.wait(1)

        self.play(FadeOut(perS),Transform(areaS,MathTex('s').next_to(areaEq,RIGHT)))
        self.wait(1)

        side = MathTex('s=4').to_edge(LEFT).shift(2*RIGHT+UP)
        per = MathTex('P=16').to_edge(LEFT).shift(2*RIGHT)
        area = MathTex('A=16').to_edge(LEFT).shift(2*RIGHT+DOWN)

        self.play(Transform(VGroup(areaEq,areaS,per4),side),Write(VGroup(per,area)))
        self.wait(1)

class hexagon(Scene):
    def construct(self):
        points = [
            [ 2,0,0],
            [ 2*math.cos(math.tau/6), 2*math.sin(math.tau/6),0],
            [-2*math.cos(math.tau/6), 2*math.sin(math.tau/6),0],
            [-2,0,0],
            [-2*math.cos(math.tau/6),-2*math.sin(math.tau/6),0],
            [ 2*math.cos(math.tau/6),-2*math.sin(math.tau/6),0]
        ]
        hexagon = Polygon(*points)
        self.play(Create(hexagon))
        self.wait(1)
        self.play(hexagon.animate.shift(2*RIGHT))
        lines = VGroup
        for i in points:
            line = Line([2,0,0],[i[0]+2,i[1],0])
            self.play(GrowFromCenter(line),run_time=.125)
        self.wait(1)

        area = MathTex('A','=','6',r'\frac{s^2\sqrt{3}}{4}').to_edge(LEFT).shift(2*RIGHT+.5*UP)
        per = MathTex('P','=','6','s').to_edge(LEFT).shift(2*RIGHT-.5*UP)
        self.play(Write(area),Write(per))
        self.wait(1)
        self.play(FadeOut(area[0]),per[2:].animate.move_to(area[0].get_center()))
        self.wait(1)
        self.play(FadeOut(per[:2],shift=DOWN))
        self.wait(1)
        self.play(FadeOut(area[2]),FadeOut(per[2]))
        self.wait(1)
        self.play(FadeOut(area[3][1],shift=UP),Transform(per[3],MathTex('1').align_to(per[3],LEFT+DOWN)))
        self.wait()
        self.play(FadeOut(per[3]),FadeOut(area[3][5]),area[3][6].animate.align_to(per[3],LEFT+DOWN))
        ssqrt3 = MathTex('s',r'\sqrt{3}').next_to(area[1],RIGHT)
        self.play(ReplacementTransform(VGroup(area[3][0],area[3][2],area[3][3],area[3][4]),ssqrt3))
        self.wait(1)
        fouroverthree = MathTex(r'\frac{4}{\sqrt{3}}').next_to(area[1],LEFT)
        self.play(Transform(area[3][6],fouroverthree[0][0]),Create(fouroverthree[0][1]),Transform(ssqrt3[1],fouroverthree[0][2:]))
        self.wait(1)
        area      = MathTex('A=8\sqrt{3}').to_edge(LEFT).shift(1.5*RIGHT+  UP*1.5)
        perimeter = MathTex('P=8\sqrt{3}').to_edge(LEFT).shift(1.5*RIGHT+DOWN*0.5)
        self.play(Write(VGroup(area,perimeter)))
        self.wait(1)

class pentagon(Scene):
    def construct(self):
        points = [
            [2*math.sin(1*math.tau/5),2*math.cos(1*math.tau/5),0],
            [2*math.sin(2*math.tau/5),2*math.cos(2*math.tau/5),0],
            [2*math.sin(3*math.tau/5),2*math.cos(3*math.tau/5),0],
            [2*math.sin(4*math.tau/5),2*math.cos(4*math.tau/5),0],
            [2*math.sin(5*math.tau/5),2*math.cos(5*math.tau/5),0]
        ]
        pentagon = Polygon(*points)
        self.play(Create(pentagon))
        self.wait(1)
        lines = VGroup(
            Line(points[0],[0,0,0]),
            Line(points[1],[0,0,0]),
            Line(points[2],[0,0,0]),
            Line(points[3],[0,0,0]),
            Line(points[4],[0,0,0]),
        )
        self.play(Create(lines))
        self.wait(1)

class circle(Scene):
    def construct(self):
        circle = Circle(2).set_color(BLUE)
        radii = Line([2,0,0],[0,0,0])
        self.play(Create(circle))
        self.wait(1)
        self.play(Create(radii))
        self.wait(1)

        circle = VGroup(circle,radii)
        self.play(circle.animate.shift(2*RIGHT))

        area = MathTex('A','=','\pi r^2').to_edge(LEFT).shift(2*RIGHT).shift(.5*UP)
        perimeter = MathTex('P','=','2\pi r').to_edge(LEFT).shift(2*RIGHT).shift(-.5*UP)
        self.play(Write(area),Write(perimeter))
        self.wait(1)

        self.play(perimeter[2].animate.align_to(area[0],RIGHT+DOWN),FadeOut(area[0]),FadeOut(perimeter[:2]))
        self.wait(1)

        self.play(FadeOut(perimeter[2][1]),FadeOut(area[2][0]))
        self.wait(1)
        self.play(FadeOut(perimeter[2][2]),FadeOut(area[2][2]))
        self.wait(1)

        final = MathTex('r=2').to_edge(LEFT).shift(2*RIGHT)

        self.play(ReplacementTransform(VGroup(area[1],area[2][1],perimeter[2][0]),final))

        area = MathTex('A=4\pi').to_edge(LEFT).shift(2*RIGHT)
        perimeter = MathTex('P=4\pi').to_edge(LEFT).shift(2*RIGHT+DOWN)
        self.wait(2)
        self.play(final.animate.shift(UP))
        self.wait(1)
        self.play(Write(area),Write(perimeter))
        self.wait(1)

class general_to_triangle(Scene):
    def construct(self):
        points = [
            [2*math.sin(1*math.tau/5),2*math.cos(1*math.tau/5),0],
            [2*math.sin(2*math.tau/5),2*math.cos(2*math.tau/5),0],
            [2*math.sin(3*math.tau/5),2*math.cos(3*math.tau/5),0],
            [2*math.sin(4*math.tau/5),2*math.cos(4*math.tau/5),0],
            [2*math.sin(5*math.tau/5),2*math.cos(5*math.tau/5),0]
        ]
        pentagon = Polygon(*points)
        self.play(Create(pentagon))
        self.wait(1)
        lines = VGroup(
            Line([2*math.sin(2*math.tau/5),2*math.cos(2*math.tau/5),0],[0,0,0]),
            Line([2*math.sin(3*math.tau/5),2*math.cos(3*math.tau/5),0],[0,0,0])
        )
        dotted = VGroup(
            DashedLine([2*math.sin(1*math.tau/5),2*math.cos(1*math.tau/5),0],[0,0,0]),
            DashedLine([2*math.sin(4*math.tau/5),2*math.cos(4*math.tau/5),0],[0,0,0]),
            DashedLine([2*math.sin(5*math.tau/5),2*math.cos(5*math.tau/5),0],[0,0,0]),
        )
        self.play(Create(lines),Create(dotted))
        self.wait(1)

        triangle = VGroup(
            Line(points[1],[0,0,0]),
            Line(points[2],[0,0,0]),
            Line(points[1],points[2]),
        )

        self.play(FadeOut(lines),FadeOut(dotted),FadeOut(pentagon),FadeIn(triangle))
        self.wait(1)
        baseBrace = BraceBetweenPoints(points[2],points[1])
        baseBraceLabel = baseBrace.get_text('b')
        heightBrace = BraceBetweenPoints([points[2][0],0,0],points[2])
        heightBraceLabel = heightBrace.get_text('h')
        self.play(Create(baseBrace),Create(baseBraceLabel),Create(heightBrace),Create(heightBraceLabel))
        self.wait(1)
        area      = MathTex('A','=',r'\frac{bh}{2}').shift(2*RIGHT+2*UP)
        perimeter = MathTex('P','=','b')            .shift(2*LEFT +2*UP)
        self.play(Write(area),Write(perimeter))
        self.wait(1)

        self.play(Transform(area[2][1],MathTex('2').move_to(area[2][1].get_center())))
        self.wait(1)
        self.play(Transform(area,MathTex('A','=','b').move_to(area.get_center())))
        self.wait(1)

        self.play(Transform(heightBraceLabel,MathTex('2').move_to(heightBraceLabel.get_center())))
        self.wait(1)

class general_triangle_trig(MovingCameraScene):
    def construct(self):
        points = [
            [0,1.5,0],
            [2.5,-1.5,0],
            [-2.5,-1.5,0]
        ]
        tri = Polygon(*points)
        self.play(Create(tri))
        self.wait(1)


        height = DashedLine([0,-1.5,0],points[0])
        self.play(Create(height))

        points = [
            [0,1.5,0],
            [2.5,-1.5,0],
            [0,-1.5,0],
            [-2.5,-1.5,0]
        ]
        new_tri0 = VGroup(
            Line(points[0],points[1]).set_color(BLUE),
            Line(points[1],points[2]).set_color(BLUE)
        )
        new_tri1 = VGroup(
            Line(points[0],points[3]).set_color(BLUE),
            Line(points[3],points[2]).set_color(BLUE)
        )

        self.wait(1)

        self.add(new_tri0,new_tri1)
        self.remove(tri)
        self.play(FadeOut(new_tri1,shift=[-1,0,0]))
        self.wait(1)

        heightBrace = BraceBetweenPoints(points[0],points[2])
        heightBraceLabel = heightBrace.get_text('2')

        baseBrace = BraceBetweenPoints(points[2],points[1])
        baseBraceLabel = baseBrace.get_tex(r'\frac{b}{2}')

        angleLabel = MathTex(r'\theta').move_to(points[0]).shift(RIGHT)
        angleArc = Arc(arc_center=points[0], start_angle=3*math.tau/4, angle=math.tau/9)

        self.play(Create(heightBrace),Create(heightBraceLabel))
        self.wait(.2)
        self.play(Create(baseBrace),Create(baseBraceLabel))
        self.wait(.2)
        self.play(Create(angleLabel),Create(angleArc))
        self.wait(1)

        triangle = VGroup(
            new_tri0,
            height,
            angleLabel,
            heightBraceLabel,
            heightBrace,
            baseBraceLabel,
            baseBrace,
            angleArc,
        )

        trig_eq = MathTex(r'tan(\theta)','=',r'\frac{O}{A}').shift(2*LEFT)
        self.play(triangle.animate.shift(2*RIGHT),Write(trig_eq))
        self.wait(1)
        new_tri1.shift(2*RIGHT)

        self.play(Transform(trig_eq[2][2],MathTex('2').move_to(trig_eq[2][2].get_center())))
        self.wait(1)
        self.play(
            Transform(trig_eq[2][0],MathTex('b').move_to(trig_eq[2][0].get_center())),
            Transform(trig_eq[2][2],MathTex('4').move_to(trig_eq[2][2].get_center())),
        )
        self.wait(1)

        new_trig_eq = MathTex('4',r'tan(\theta)','=','b').shift(2*LEFT)

        self.play(
            FadeOut(trig_eq[2][1:]),
            trig_eq[0].animate.move_to(new_trig_eq[1].get_center()),
            trig_eq[1].animate.move_to(new_trig_eq[2].get_center()),
            trig_eq[2][0].animate.move_to(new_trig_eq[3].get_center()),
            Write(new_trig_eq[0])
        )
        self.wait(1)

        self.play(
            FadeIn(new_tri1),
            FadeOut(heightBrace),
            FadeOut(heightBraceLabel),
            FadeOut(baseBrace),
            FadeOut(baseBraceLabel),
        )
        self.wait(1)

        other_arc = Arc(arc_center=points[0], start_angle=3*math.tau/4, angle=-math.tau/9).shift(2*RIGHT)
        self.play(Create(other_arc))
        self.wait(1)

        final_eq_for_s = MathTex('s','=','4',r'tan\bigg(',r'\frac{\tau}{2n}',r'\bigg)').shift(10*UP)
        self.play(self.camera.frame.animate.move_to(final_eq_for_s))
        self.wait(1)
        self.play(Write(final_eq_for_s))
        self.wait(1)
