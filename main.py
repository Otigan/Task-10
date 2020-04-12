from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label


class CustomLayout(FloatLayout):

    def __init__(self,image, text1, text2, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        self.image = image
        self.title = text1
        self.subtitle = text2

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .7},
                background_normal='',
                background_color=(1, .3, .4, .85),
                disabled=True))


        self.add_widget(AsyncImage(source=self.image,
                                   size_hint=(.3, .3),
                                   pos_hint={'center_x': .5, 'center_y': .75}))

        self.add_widget(Label(text=self.title,
                              size_hint=(.5, .5),
                              pos_hint={'center_x': .5, 'center_y': .55}))

        self.add_widget(Label(text=self.subtitle,
                              size_hint=(.5, .5),
                              pos_hint={'center_x': .5, 'center_y': .5}))

        with self.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)


        self.bind(size=self._update_rect, pos=self._update_rect)


    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


listOfModels = [
    CustomLayout(image="https://sun9-24.userapi.com/c205716/v205716966/a5cdf/pdBiJiHmbgA.jpg", text1="Title 1",
                 text2="Subtitle 2"),
    CustomLayout(image="https://sun9-62.userapi.com/c543108/v543108742/6511d/dF8rXJdaI2Y.jpg", text1="Title 2",
                 text2="Subtitle 2"),
    CustomLayout(image="https://sun1-94.userapi.com/NuCBUBOkhhHBPHCwjmBNQzfAOUNvikkiApepLg/Vzuo5DP2zIc.jpg",
                 text1="Title 3", text2="Subtitle 3")]


class MainApp(App):

    def build(self):

        carousel = Carousel(direction='right')

        for item in listOfModels:
            self.root = root = item

            carousel.add_widget(item)

        return carousel


if __name__ == '__main__':
    MainApp().run()
