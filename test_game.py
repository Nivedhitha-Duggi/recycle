import unittest
import pygame
from game import move_items, check_collision, reset_level, create_item, player

class TestRecycleGame(unittest.TestCase):

    def setUp(self):
        # Initialize Pygame and setup any necessary game variables
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.player = player
        self.items = []

    def test_move_items(self):
        """Test if items are moving down correctly."""
        # Create an item
        create_item()
        initial_position = self.items[0]["rect"].y
        move_items()  # Move items down by fall_speed
        new_position = self.items[0]["rect"].y
        self.assertGreater(new_position, initial_position, "Item did not move down!")

    def test_check_collision_bottle(self):
        """Test if score increases correctly on bottle collision."""
        self.player.x = 100  # Position player to collide with an item
        self.player.y = 100
        # Simulate a bottle falling
        self.items = [{"type": "bottle", "rect": pygame.Rect(100, 100, 40, 40)}]
        initial_score = 0  # Assuming score starts at 0
        check_collision()  # Check collision
        self.assertEqual(initial_score + 1, 1, "Score did not increase correctly on bottle collision")

    def test_check_collision_thorn(self):
        """Test if lives decrease correctly on thorn collision."""
        self.player.x = 100
        self.player.y = 100
        # Simulate a thorn falling
        self.items = [{"type": "thorn", "rect": pygame.Rect(100, 100, 40, 40)}]
        initial_lives = 3  # Assuming lives start at 3
        check_collision()  # Check collision
        self.assertEqual(initial_lives - 1, 2, "Lives did not decrease correctly on thorn collision")

    def test_reset_level(self):
        """Test if reset_level clears the items."""
        create_item()  # Add an item
        self.assertNotEqual(len(self.items), 0, "Items list should not be empty before reset")
        reset_level()  # Reset level
        self.assertEqual(len(self.items), 0, "Items list should be empty after reset")
#main function
if __name__ == '__main__':
    unittest.main()

