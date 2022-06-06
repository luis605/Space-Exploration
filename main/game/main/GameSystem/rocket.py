from ursina import *



class Rocket(Entity):
    def __init__(self, rocket, **kwargs):
        super().__init__()
        self.speed = 5
        self.height = 40
        self.acceleration = 1
        self.rocket = rocket

        self.gravity = 1
        self.grounded = False
        self.jump_height = 99999999999
        self.jump_up_duration = 9
        self.fall_after = .35 # will interrupt jump up
        self.jumping = False
        self.air_time = 0

        for key, value in kwargs.items():
            setattr(self, key ,value)


        # make sure we don't fall through the ground if we start inside it
        if self.gravity:
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            if ray.hit:
                self.y = ray.world_point.y
                    
        self.go_up()

    def update(self):



            # gravity
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            # ray = boxcast(self.world_position+(0,2,0), self.down, ignore=(self,))

            if ray.distance <= self.height+.1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False

            # if not on ground and not on way up in jump, fall
            self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
            self.air_time += time.dt * .25 * self.gravity



    def go_up(self):

##        self.rocket.shake(duration=.2, magnitude=.001, speed=.01, direction=(1,1))


        self.grounded = False
        self.rocket.animate_y(self.rocket.y+self.jump_height*self.acceleration, self.jump_up_duration*self.acceleration, resolution=int(1*self.acceleration//time.dt), curve=curve.out_expo)
        invoke(self.start_fall, delay=self.fall_after)



    def start_fall(self):
        self.rocket.y_animator.pause()
        self.jumping = False


    def land(self):
        # print('land')
        self.air_time = 0
        self.grounded = True










            
