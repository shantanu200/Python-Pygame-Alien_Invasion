from sys import path


class settings:
     
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
    
        self.ship_speed = 1.0
        
        self.bullet_speed = 1.5
        self.bullet_width =3
        self.bullet_height=15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        
        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        
        self.ship_limit = 3
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.intialise_dynamic_settings()
        
        
    def intialise_dynamic_settings(self):
     self.ship_speed = 1.5
     self.bullet_speed =3.0
     self.alien_speed = 1.0
    
     self.fleet_direction = 1
     self.aliens_points = 50
     
    def increase_speed(self):
     self.ship_speed *= self.speedup_scale
     self.bullet_speed *= self.speedup_scale
     self.alien_speed *= self.speedup_scale
     self.aliens_points = int(self.aliens_points * self.score_scale)
     print(self.aliens_points)