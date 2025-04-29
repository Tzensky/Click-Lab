import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "ArbreCompetence - ClickLab"

class GameView(arcade.Window):
    
    def __init__(self):

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.background_color = arcade.csscolor.BLACK
    
    def setup(self):
         pass
        
    def on_draw(self):
       
       self.clear()
       
    def main():
        window = GameView()
        window.setup()
        arcade.run()
        
if __name__ == "__main__":
    main()