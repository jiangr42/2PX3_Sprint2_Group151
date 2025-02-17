
from trafficSimulator import *
import numpy as np


class Intersection:
    def __init__(self):
        self.sim = Simulation()
        lane_space = 3.5
        intersection_size = 24
        island_width = 2
        length = 100


#---------------------------------------------------------------Variables----------------------------------------------------------------------------#
        self.vehicle_rate = 50
        self.v = 17
        self.speed_variance = 0
        self.self_driving_vehicle_proportion = 0 #number between 0 and 1, 0 means no self driving vehicles, 1 means entirely self driving vehicles
        if self.self_driving_vehicle_proportion == 1:
            self.v = self.v * 1.5
#----------------------------------------------------------------------------------------------------------------------------------------------------#
    #this section defines all the paths that a vehicle can take
    # SOUTH, EAST, NORTH, WEST
        #INNER, OUTER
        # Intersection in
            #paths 0-7
        #self.sim.create_segment((lane_space/2 + island_width/2, length + intersection_size/2), (lane_space/2 + island_width/2, intersection_size/2)) 
        self.sim.create_segment((lane_space*3/2 + island_width/2, length+intersection_size/2), (lane_space*3/2+island_width/2, intersection_size/2)) 
        #self.sim.create_segment((length + intersection_size/2, -lane_space/2 - island_width/2), (intersection_size/2, -lane_space/2 - island_width/2)) 
        self.sim.create_segment((length + intersection_size/2, -lane_space*3/2 - island_width/2), (intersection_size/2, - lane_space*3/2 - island_width/2)) 
        #self.sim.create_segment((-lane_space/2 - island_width/2, -length - intersection_size/2), (-lane_space/2 - island_width/2, - intersection_size/2)) 
        self.sim.create_segment((-lane_space*3/2 - island_width/2, -length - intersection_size/2), (-lane_space*3/2 - island_width/2, -intersection_size/2)) 
        #self.sim.create_segment((-length - intersection_size/2, lane_space/2 + island_width/2), (-intersection_size/2, lane_space/2 + island_width/2)) 
        self.sim.create_segment((-length - intersection_size/2, lane_space*3/2 + island_width/2), (-intersection_size/2, lane_space*3/2 + island_width/2))
        # Intersection out
            #paths 8-15
        #self.sim.create_segment((-lane_space/2 - island_width/2, intersection_size/2), (-lane_space/2 - island_width/2, length + intersection_size/2))
        self.sim.create_segment((-lane_space*3/2 - island_width/2, intersection_size/2), (-lane_space*3/2 - island_width/2, length + intersection_size/2))
        #self.sim.create_segment((intersection_size/2, lane_space/2 + island_width/2), (length+intersection_size/2, lane_space/2 + island_width/2))
        self.sim.create_segment((intersection_size/2, lane_space*3/2 + island_width/2), (length+intersection_size/2, lane_space*3/2 + island_width/2))
        #self.sim.create_segment((lane_space/2 + island_width/2, -intersection_size/2), (lane_space/2 + island_width/2, -length - intersection_size/2))
        self.sim.create_segment((lane_space*3/2 + island_width/2, -intersection_size/2), (lane_space*3/2 + island_width/2, -length-intersection_size/2))
        #self.sim.create_segment((-intersection_size/2, -lane_space/2 - island_width/2), (-length-intersection_size/2, -lane_space/2 - island_width/2))
        self.sim.create_segment((-intersection_size/2, -lane_space*3/2 - island_width/2), (-length - intersection_size/2, -lane_space*3/2 - island_width/2))

        # Straight
            #paths 16-23
        self.sim.create_segment((intersection_size/2, lane_space + island_width/2), (intersection_size/2, -lane_space - island_width/2))
        #self.sim.create_segment((lane_space*3/2 + island_width/2, intersection_size/2), (lane_space*3/2 + island_width/2, -intersection_size/2))
        self.sim.create_segment((lane_space + island_width/2, -intersection_size/2), (-lane_space - island_width/2, -intersection_size/2))
        #self.sim.create_segment((intersection_size/2, -lane_space*3/2 - island_width/2), (-intersection_size/2, -lane_space*3/2 - island_width/2))
        self.sim.create_segment((-intersection_size/2, -lane_space - island_width/2), (-intersection_size/2, lane_space + island_width/2))
        #self.sim.create_segment((-lane_space*3/2 - island_width/2, -intersection_size/2), (-lane_space*3/2 - island_width/2, intersection_size/2))
        self.sim.create_segment((-lane_space - island_width/2, intersection_size/2), (lane_space + island_width/2, intersection_size/2))
        #self.sim.create_segment((-intersection_size/2, lane_space*3/2 + island_width/2), (intersection_size/2, lane_space*3/2 + island_width/2))
    
    # SOUTH, EAST, NORTH, WEST
        #Right turn
            #paths 24-27 
        self.sim.create_quadratic_bezier_curve((lane_space + island_width/2, intersection_size/2), (lane_space*3 + island_width, lane_space*3 + island_width), (intersection_size/2, lane_space + island_width/2))
        self.sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space - island_width/2), (lane_space*3 + island_width, -lane_space*3 - island_width), (lane_space + island_width/2, -intersection_size/2))
        self.sim.create_quadratic_bezier_curve((-lane_space - island_width/2, -intersection_size/2), (-lane_space*3 - island_width/2, -lane_space*3 - island_width/2), (-intersection_size/2, -lane_space - island_width/2))
        self.sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space + island_width/2), (-lane_space*3 - island_width/2, lane_space*3 + island_width/2), (-lane_space - island_width/2, intersection_size/2))

        # Left turn
            #paths 28-31
        #self.sim.create_quadratic_bezier_curve((lane_space/2 + island_width/2, intersection_size/2), (lane_space/2 + island_width/2, -lane_space/2 - island_width/2), (-intersection_size/2, -lane_space/2 - island_width/2))
        #self.sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2 - island_width/2), (-lane_space/2 - island_width/2, -lane_space/2 - island_width/2), (-lane_space/2 - island_width/2, intersection_size/2))
        #self.sim.create_quadratic_bezier_curve((-lane_space/2 - island_width/2, -intersection_size/2), (-lane_space/2 - island_width/2, lane_space/2 + island_width/2), (intersection_size/2, lane_space/2 + island_width/2))
        #self.sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2 + island_width/2), (lane_space/2 + island_width/2, lane_space/2 + island_width/2), (lane_space/2 + island_width/2, -intersection_size/2))
        
    #all interfearing paths


    #Second roundabout 

     # Intersection in
            #paths 0-7
        #self.sim.create_segment((lane_space/2 + island_width/2, length + intersection_size/2), (lane_space/2 + island_width/2, intersection_size/2)) 
        self.sim.create_segment((lane_space*3/2 + island_width/2, length+intersection_size/2), (lane_space*3/2+island_width/2, intersection_size/2)) 
        #self.sim.create_segment((length + intersection_size/2, -lane_space/2 - island_width/2), (intersection_size/2, -lane_space/2 - island_width/2)) 
        self.sim.create_segment((length + intersection_size/2, -lane_space*3/2 - island_width/2), (intersection_size/2, - lane_space*3/2 - island_width/2)) 
        #self.sim.create_segment((-lane_space/2 - island_width/2, -length - intersection_size/2), (-lane_space/2 - island_width/2, - intersection_size/2)) 
        self.sim.create_segment((-lane_space*3/2 - island_width/2, -length - intersection_size/2), (-lane_space*3/2 - island_width/2, -intersection_size/2)) 
        #self.sim.create_segment((-length - intersection_size/2, lane_space/2 + island_width/2), (-intersection_size/2, lane_space/2 + island_width/2)) 
        self.sim.create_segment((-length - intersection_size/2, lane_space*3/2 + island_width/2), (-intersection_size/2, lane_space*3/2 + island_width/2))
        # Intersection out
            #paths 8-15
        #self.sim.create_segment((-lane_space/2 - island_width/2, intersection_size/2), (-lane_space/2 - island_width/2, length + intersection_size/2))
        self.sim.create_segment((-lane_space*3/2 - island_width/2, intersection_size/2), (-lane_space*3/2 - island_width/2, length + intersection_size/2))
        #self.sim.create_segment((intersection_size/2, lane_space/2 + island_width/2), (length+intersection_size/2, lane_space/2 + island_width/2))
        self.sim.create_segment((intersection_size/2, lane_space*3/2 + island_width/2), (length+intersection_size/2, lane_space*3/2 + island_width/2))
        #self.sim.create_segment((lane_space/2 + island_width/2, -intersection_size/2), (lane_space/2 + island_width/2, -length - intersection_size/2))
        self.sim.create_segment((lane_space*3/2 + island_width/2, -intersection_size/2), (lane_space*3/2 + island_width/2, -length-intersection_size/2))
        #self.sim.create_segment((-intersection_size/2, -lane_space/2 - island_width/2), (-length-intersection_size/2, -lane_space/2 - island_width/2))
        self.sim.create_segment((-intersection_size/2, -lane_space*3/2 - island_width/2), (-length - intersection_size/2, -lane_space*3/2 - island_width/2))

        # Straight
            #paths 16-23
        self.sim.create_segment((intersection_size/2, lane_space + island_width/2), (intersection_size/2, -lane_space - island_width/2))
        #self.sim.create_segment((lane_space*3/2 + island_width/2, intersection_size/2), (lane_space*3/2 + island_width/2, -intersection_size/2))
        self.sim.create_segment((lane_space + island_width/2, -intersection_size/2), (-lane_space - island_width/2, -intersection_size/2))
        #self.sim.create_segment((intersection_size/2, -lane_space*3/2 - island_width/2), (-intersection_size/2, -lane_space*3/2 - island_width/2))
        self.sim.create_segment((-intersection_size/2, -lane_space - island_width/2), (-intersection_size/2, lane_space + island_width/2))
        #self.sim.create_segment((-lane_space*3/2 - island_width/2, -intersection_size/2), (-lane_space*3/2 - island_width/2, intersection_size/2))
        self.sim.create_segment((-lane_space - island_width/2, intersection_size/2), (lane_space + island_width/2, intersection_size/2))
        #self.sim.create_segment((-intersection_size/2, lane_space*3/2 + island_width/2), (intersection_size/2, lane_space*3/2 + island_width/2))
    
    # SOUTH, EAST, NORTH, WEST
        #Right turn
            #paths 24-27 
        self.sim.create_quadratic_bezier_curve((lane_space + island_width/2, intersection_size/2), (lane_space*3 + island_width, lane_space*3 + island_width), (intersection_size/2, lane_space + island_width/2))
        self.sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space - island_width/2), (lane_space*3 + island_width, -lane_space*3 - island_width), (lane_space + island_width/2, -intersection_size/2))
        self.sim.create_quadratic_bezier_curve((-lane_space - island_width/2, -intersection_size/2), (-lane_space*3 - island_width/2, -lane_space*3 - island_width/2), (-intersection_size/2, -lane_space - island_width/2))
        self.sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space + island_width/2), (-lane_space*3 - island_width/2, lane_space*3 + island_width/2), (-lane_space - island_width/2, intersection_size/2))


        '''
        this section creates vehicle generators, we have two vehicle generators one; that creates regular vehicles (self.vg)
        and one that creates self-driving vehicles (self.sdvg)
        '''
        #regular vehicle generator
        layer2SpeedMod = 1.5
        self.vg = VehicleGenerator({
            #The first variable: 1 defines the weight if the vehicle; the higher the weight the more likely that type of vehicle will generate
            # 'path' defines the order of segments the vehicle will drive over
            #'v_max' defines the fastest speed a vehicle can drive at

            'vehicles': [
                #South [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [0, 12, 5], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [0, 12, 8, 13, 6], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [0, 12, 8, 13, 9, 14, 7], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [0, 12, 8, 13, 9, 14, 10, 15, 4], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),

                #East [1st exit 2nd exit 3rd exit 4th exit]
                (1, {'path': [3, 15, 4], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [3, 15, 11, 12 ,5], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [3, 15, 11, 12 ,8, 13, 6], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [3, 15, 11, 12 ,8, 13, 9, 14, 7], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),

                #North [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [2, 14, 7], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [2, 14, 10, 15, 4], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [2, 14, 10, 15, 11, 12 ,5], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [2, 14, 10, 15, 11, 12 ,8, 13, 6], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),

           
                #West [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [1, 13, 6], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [1, 13, 9, 14, 7], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [1, 13, 9, 14, 10, 15, 4], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [1, 13, 9, 14, 10, 15, 11, 12, 5], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),

                #Second layer
                #South [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [16, 28, 21], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [16, 28, 24, 29, 22], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [16, 28, 24, 29, 25, 30, 23], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [16, 28, 24, 29, 25, 30, 26, 31, 20], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),

                #East [1st exit 2nd exit 3rd exit 4th exit]
                (1, {'path': [19, 31, 20], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [19, 31, 27, 28 ,21], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [19, 31, 27, 28 ,24, 29, 22], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [19, 31, 27, 28 ,24, 29, 25, 30, 23], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),

                #North [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [18, 30, 23], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [18, 30, 26, 31, 20], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [18, 30, 26, 31, 27, 28 ,21], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [18, 30, 26, 31, 27, 28 ,24, 29, 22], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),

           
                #West [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [17, 29, 22], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [17, 29, 25, 30, 23], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [17, 29, 25, 30, 26, 31, 20], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [17, 29, 25, 30, 26, 31, 27, 28, 21], 'v_max': layer2SpeedMod*self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                ], 'vehicle_rate' : self.vehicle_rate*(1-self.self_driving_vehicle_proportion)

            })
        
        
        #self-driving vehicle generator
        self.sdvg = VehicleGenerator({
 
            #The first variable: 1 defines the weight if the vehicle; the higher the weight the more likely that type of vehicle will generate
            # 'path' defines the order of segments the vehicle will drive over
            #'v_max' defines the fastest speed a vehicle can drive at
            #'T' defines the raction time of the vehicle, the base is 1
            #'s0' defines the shortest distance a vehicle is able to drive behind another vehicle
            'vehicles': [
                #South [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [0, 16, 12], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [1, 17, 13], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [1, 24, 11], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [0, 28, 14], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),

                #East [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [2, 18, 14], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [3, 19, 15], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [3, 25, 13], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [2, 29, 8], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),

                #North [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [4, 20, 8], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [5, 21, 9], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [5, 26, 15], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [4, 30, 10], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
           
                #West [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [6, 22, 10], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [7, 23, 11], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [7, 27, 9], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [6, 31, 12], 'v_max': self.v ,'T' : 0.1,'s0' : 4}),
                ], 'vehicle_rate' : self.vehicle_rate*self.self_driving_vehicle_proportion 
            })
        
        #adding both vehicle generators
        self.sim.add_vehicle_generator(self.vg)
        self.sim.add_vehicle_generator(self.sdvg)

    

        #adding the traffic signal
        #self.sim.create_traffic_signal([self.sim.segments[0],self.sim.segments[1], self.sim.segments[4], self.sim.segments[5]],[self.sim.segments[2],self.sim.segments[3],self.sim.segments[6], self.sim.segments[7]])

    
    #this function returns an instance of the simulation defined above
    def get_sim(self):
        return self.sim