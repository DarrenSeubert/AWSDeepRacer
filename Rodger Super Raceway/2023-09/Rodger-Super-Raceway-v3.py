class Reward:
    def __init__(self):
        self.prevPosition = 0.0
    
    def rewardFunction(self, params):
        # Read input parameters
        allWheelsOnTrack = params['all_wheels_on_track']
        distanceFromCenter = params['distance_from_center']
        trackWidth = params['track_width']
        steeringAngle = params['steering_angle']
        progress = params['progress']
        trackLength = params['track_length']
        speed = min(params['speed'], 1)
        currentPosition = progress * 0.01 * trackLength
        distanceTraveled = min(0.0667, max(0, currentPosition - self.prevPosition)) # Car max distance traveled @1 m/s = 0.0667 m 

        wheelsOnTrackReward = allWheelsOnTrack * 12 # Max Reward = 12
        centerReward = 25 * ((1 - distanceFromCenter / trackWidth * 2) ** 2) # Max Reward = 25
        steeringReward = max(0, -0.016 * (steeringAngle ** 2) + 10) # Max Reward = 10
        progressReward = 113565128.5 * (distanceTraveled ** 6) # Max Reward = 10
        speedReward = 35 * (speed ** 19) # Max Reward = 35

        self.prevPosition = currentPosition
        return float(wheelsOnTrackReward + centerReward + steeringReward + progressReward + speedReward)

rewardObject = Reward()

def reward_function(params):
    return rewardObject.rewardFunction(params)
