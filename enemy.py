import arcade

class Enemy(arcade.SpriteSolidColor):
    def __init__(self, x, y):
        # Create a red 40x40 enemy square using SpriteSolidColor
        super().__init__(40, 40, (255, 0, 0))  # Using RGB values for red explicitly
        
        # Position the enemy
        self.center_x = x
        self.center_y = y
        
        # Set the speed and health of the enemy
        self.speed = 1.5
        self.health = 100

    def follow_player(self, player_sprite):
        """
        This function will move the enemy towards the player.
        """
        # Calculate movement
        if self.center_x < player_sprite.center_x:
            self.center_x += self.speed
        elif self.center_x > player_sprite.center_x:
            self.center_x -= self.speed

        if self.center_y < player_sprite.center_y:
            self.center_y += self.speed
        elif self.center_y > player_sprite.center_y:
            self.center_y -= self.speed
        
        # Keep enemy within screen bounds
        if self.left < 0:
            self.left = 0
        elif self.right > 800:  # SCREEN_WIDTH
            self.right = 800
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 600:  # SCREEN_HEIGHT
            self.top = 600
