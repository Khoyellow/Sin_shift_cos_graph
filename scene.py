from manim import *
from math import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class GraphScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="vi"))
        plane = NumberPlane(x_range=[-10,10], y_range=[-10,10],  x_length=10, y_length=10).add_coordinates()
        graph = plane.plot(lambda x : sin(x), x_range=[-10,10], color=GREEN)
        graph2 = plane.plot(lambda x : cos(x), x_range=[-10,10], color=RED)
        x_label = plane.get_x_axis_label("radian")
        sinx_label = plane.get_y_axis_label(label="sin(x)")
        cosx_label = plane.get_y_axis_label(label="cos(x)")

        self.play(DrawBorderThenFill(plane))
        self.wait()

        with self.voiceover(text="Đây là đồ thị của hàm số sin(x)") as tracker:
            self.play(Create(graph), FadeIn(x_label), FadeIn(sinx_label))
        self.wait()

        with self.voiceover(text="Khi dịch sang trái pi/4 radian, ta thu được đồ thị của hàm số cos(x)") as tracker:
            self.play(FadeOut(sinx_label), Transform(graph, graph2), FadeIn(cosx_label))
        self.wait()