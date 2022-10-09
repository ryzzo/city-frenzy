import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

answer = []

class MainPage(GridLayout):
    """First page of the App"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.add_widget(Label(text="CAPITAL\nFRENZY", color='red'))
        
        introduction = "Guess the capital city"
        self.add_widget(Label(text=introduction))

        # play button to proceed to game
        self.play = Button(text="play")
        self.add_widget(self.play)
        self.play.bind(on_press=self.play_button)

    # function that direct to game page on pressing button
    def play_button(self, instance):
        game_app.screen_manager.current = 'game'


class GamePage(GridLayout):
    """Page that display's the game"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        self.add_widget(Label(text="What is the capital city of"))
        self.add_widget(Label(text="KENYA"))

        self.display = Label(text = "_____",halign='center', valign='middle', font_size=30)
        self.add_widget(self.display)

        input_area = GridLayout(cols=3)
        input_area.add_widget(Label(text="Enter a letter"))
        self.user_input = TextInput(multiline=False)
        input_area.add_widget(self.user_input)

        # Check button
        self.check = Button(text="Check")
        self.check.bind(on_press=self.checkButton)
        input_area.add_widget(self.check)
        
        self.add_widget(input_area)

    def checkButton(self, instance):
        letter = self.user_input.text

        answer.append(letter)

        # join the contents of the list
        dis = ''.join(answer)

        self.display.text = dis


class CapitalApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Main page
        self.main_page = MainPage()
        screen = Screen(name = 'main')
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)

        # Game page
        self.game_page = GamePage()
        screen = Screen(name = 'game')
        screen.add_widget(self.game_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    game_app = CapitalApp()
    game_app.run()
