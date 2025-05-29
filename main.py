import arcade
from enemy import Enemy
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Diablo Style ARPG Starter"

class MyGame(arcade.Window):
    def __init__(self):
        # Call the parent class constructor with window dimensions and title        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background color of the game window
        arcade.set_background_color(arcade.color.BLACK)

        # Variables to store player and sprite list
        self.player_sprite = None
        self.player_list = None
        self.enemy_list = None

    def setup(self):
        """
        This method is called once at the beginning to set up the game state.
        It can also be called again to restart the game.
        """
        # Create a list to hold all sprites (only the player for now)
        self.player_list = arcade.SpriteList()
        # Create the enemy list
        self.enemy_list = arcade.SpriteList()

        # Create the player sprite: a simple blue square (40x40)
        self.player_sprite = arcade.SpriteSolidColor(40, 40, arcade.color.BLUE)

        # Set the starting position of the player at the center of the screen
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300

        # Add the player sprite to the player_list
        self.player_list.append(self.player_sprite)

        # Create an enemy at a corner
        enemy = Enemy(100, 100)
        self.enemy_list.append(enemy)

    def on_draw(self):
        """
        Called automatically by Arcade to draw everything on screen.
        This runs ~60 times per second.
        """
        # Clear the screen to the background color
        self.clear()

        # Draw all sprites
        self.player_list.draw()
        self.enemy_list.draw()

    def on_update(self, delta_time):
        """
        Called automatically to update the game state.
        `delta_time` is the time passed since the last frame (in seconds).
        """
        # Update all sprites (e.g., for movement, physics)
        self.player_list.update()
        # Enemy AI: move toward player
        for enemy in self.enemy_list:
            enemy.follow_player(self.player_sprite)


    def on_key_press(self, key, modifiers):
        """
        Called when a key is pressed down.
        Used to move the player or trigger actions.
        """
        if key == arcade.key.W:
            if modifiers & arcade.key.MOD_SHIFT:
                self.player_sprite.change_y = 10
                print("Shift is pressed: Moving up faster")
            else:
                self.player_sprite.change_y = 5
                print("Moving up")
        elif key == arcade.key.S:
            if modifiers & arcade.key.MOD_SHIFT:
                self.player_sprite.change_y = -10
                print("Shift is pressed: Moving down faster")
            else:
                self.player_sprite.change_y = -5
                print("Moving down")
        elif key == arcade.key.A:
            if modifiers & arcade.key.MOD_SHIFT:
                self.player_sprite.change_x = -10
                print("Shift is pressed: Moving left faster")
            else:
                self.player_sprite.change_x = -5
                print("Moving left")
        elif key == arcade.key.D:
            if modifiers & arcade.key.MOD_SHIFT:
                self.player_sprite.change_x = 10
                print("Shift is pressed: Moving right faster")
            else:
                self.player_sprite.change_x = 5
                print("Moving right")

    def on_key_release(self, key, modifiers):
        """
        Called when a key is released.
        Used to stop movement when movement keys are released.
        """
        if key in (arcade.key.W, arcade.key.S):
            self.player_sprite.change_y = 0
            print("Stopping vertical movement")
        elif key in (arcade.key.A, arcade.key.D):
            self.player_sprite.change_x = 0
            print("Stopping horizontal movement")

# Run the game if this script is executed directly
if __name__ == "__main__":
    game = MyGame()  # Create a game instance
    game.setup()     # Set up the game (load sprites, state)
    arcade.run()     # Start the game loop

        
