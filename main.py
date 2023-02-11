import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class MenuScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set the orientation of the BoxLayout
        self.orientation = "vertical"

        # Add a Label widget to display the prompt
        label = Label(text="Enter the number of players:")
        self.add_widget(label)

        # Add a TextInput widget for the user to enter the number of players
        self.text_input = TextInput(multiline=False, font_size=200, halign="center")
        self.add_widget(self.text_input)

        # Add a Button widget to start the game
        button = Button(text="Start Game")
        button.bind(on_press=self.start_game)
        self.add_widget(button)

    def start_game(self, instance):
        # Get the number of players from the TextInput widget
        num_players = int(self.text_input.text)

        # Validate the number of players
        if num_players < 2:
            popup = Popup(title="Error", content=Label(text="At least 2 players are required to start the game."), size_hint=(0.5, 0.5))
            popup.open()
        else:
            # Start the game with the specified number of players
            # ...

            # Close the menu
            App.get_running_app().stop()

class ArtilleryGame(App):
    def build(self):
        # Create the menu screen
        menu = MenuScreen()
        self.size = (500, 500)

        # Return the menu screen as the root widget
        return menu

if __name__ == '__main__':
    ArtilleryGame().run()
