import arcade

class Enemy(arcade.Sprite):
    def __init__(self, x, y):
        # Create a red 40x40 enemy square
        super().__init__()
        self.texture = arcade.make_soft_square_texture(40, arcade.color.RED)

        # Position the enemy
        self.center_x = x
        self.center_y = y

        # Set the speed of the enemy
        self.speed = 1.5

    def follow_player(self, player_sprite):
        """
        This function will move the enemy towards the player.
        """
        if self.center_x < player_sprite.center_x:
            self.center_x += self.speed
        elif self.center_x > player_sprite.center_x:
            self.center_x -= self.speed

        if self.center_y < player_sprite.center_y:
            self.center_y += self.speed
        elif self.center_y > player_sprite.center_y:
            self.center_y -= self.speed    
