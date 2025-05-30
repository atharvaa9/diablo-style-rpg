import arcade
from enemy import Enemy

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Diablo Style ARPG Starter"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.player_sprite = None
        self.player_list = None
        self.enemy_list = None
        self.bullet_list = None
        self.wall_list = None
        self.player_health = 100
        self.physics_engine = None  # ✅ NEW: physics engine

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        self.player_sprite = arcade.SpriteSolidColor(40, 40, arcade.color.BLUE)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        enemy = Enemy(100, 100)
        self.enemy_list.append(enemy)

        for x in range(0, SCREEN_WIDTH, 40):
            wall = arcade.SpriteSolidColor(40, 40, arcade.color.GRAY)
            wall.center_x = x
            wall.center_y = 20
            self.wall_list.append(wall)

            wall_top = arcade.SpriteSolidColor(40, 40, arcade.color.GRAY)
            wall_top.center_x = x
            wall_top.center_y = SCREEN_HEIGHT - 20
            self.wall_list.append(wall_top)

        for y in range(40, SCREEN_HEIGHT - 40, 40):
            wall_left = arcade.SpriteSolidColor(40, 40, arcade.color.GRAY)
            wall_left.center_x = 20
            wall_left.center_y = y
            self.wall_list.append(wall_left)

            wall_right = arcade.SpriteSolidColor(40, 40, arcade.color.GRAY)
            wall_right.center_x = SCREEN_WIDTH - 20
            wall_right.center_y = y
            self.wall_list.append(wall_right)

        # ✅ Initialize physics engine with walls
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.wall_list.draw()

    def on_update(self, delta_time):
        # ✅ Update using physics engine
        self.physics_engine.update()
        self.bullet_list.update()

        for enemy in self.enemy_list:
            enemy.follow_player(self.player_sprite)

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.player_sprite, enemy):
                self.player_health -= 1
                if self.player_health < 0:
                    self.player_health = 0

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if hit_list:
                bullet.remove_from_sprite_lists()
                for enemy in hit_list:
                    enemy.health -= 25
                    if enemy.health <= 0:
                        enemy.remove_from_sprite_lists()

        # 🆕 Update window title with health
        self.set_caption(f"{SCREEN_TITLE} | Player HP: {self.player_health}")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.change_y = 10 if modifiers & arcade.key.MOD_SHIFT else 5
        elif key == arcade.key.S:
            self.player_sprite.change_y = -10 if modifiers & arcade.key.MOD_SHIFT else -5
        elif key == arcade.key.A:
            self.player_sprite.change_x = -10 if modifiers & arcade.key.MOD_SHIFT else -5
        elif key == arcade.key.D:
            self.player_sprite.change_x = 10 if modifiers & arcade.key.MOD_SHIFT else 5
        elif key == arcade.key.SPACE:
            self.fire_bullet()

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.W, arcade.key.S):
            self.player_sprite.change_y = 0
        elif key in (arcade.key.A, arcade.key.D):
            self.player_sprite.change_x = 0

    def fire_bullet(self):
        bullet = arcade.SpriteSolidColor(8, 8, arcade.color.YELLOW)
        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y
        bullet.change_y = 10  # Fires upward
        self.bullet_list.append(bullet)

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
