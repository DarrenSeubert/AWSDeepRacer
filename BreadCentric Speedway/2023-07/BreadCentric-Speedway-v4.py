class Reward:
    def __init__(self):
        self.prevProgress = 0.0
    
    def reward_function(self, params):
        # Example of penalize steering, which helps mitigate zig-zag behaviors

        # Read input parameters
        all_wheels_on_track = params['all_wheels_on_track']
        distance_from_center = params['distance_from_center']
        track_width = params['track_width']
        abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
        progress = params['progress']
        speed = params['speed']

        # Calculate 2 marks that are farther and father away from the center line
        marker_1 = 0.1 * track_width
        marker_2 = 0.25 * track_width

        # Give higher reward if the car is closer to center line and vice versa
        if distance_from_center <= marker_1:
            reward = 3.0
        elif distance_from_center <= marker_2:
            reward = 2.0
        else:
            reward = 1e-3  # likely crashed/close to off track

        if progress > self.prevProgress + 2.0:
            reward += 2.0 
        elif progress > self.prevProgress:
            reward += 1.0
        self.prevProgress = progress

        # Steering penalty threshold, change the number based on your action space setting
        ABS_STEERING_THRESHOLD = 45

        # Penalize reward if the car is steering too much
        if abs_steering > ABS_STEERING_THRESHOLD:
            reward *= 0.8

        # Penalize reward if the car is not fully on track
        if not all_wheels_on_track:
            reward *= 0.5

        # Penalize reward if the car is too slow
        if speed < 1.25:
            reward *= 0.75

        return float(reward)

reward_object = Reward()

def reward_function(params):
    return reward_object.reward_function(params)
