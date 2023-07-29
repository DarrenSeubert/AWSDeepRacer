class Reward:
    def __init__(self):
        self.prevProgress = 0.0
    
    def rewardFunction(self, params):
        # Read input parameters
        allWheelsOnTrack = params['all_wheels_on_track']
        distanceFromCenter = params['distance_from_center']
        trackWidth = params['track_width']
        steeringAngle = params['steering_angle']
        progress = params['progress']
        speed = min(params['speed'], 1)

        wheelsOnTrackReward = allWheelsOnTrack * 15 # Max Reward = 15
        centerReward = 25 * ((1 - distanceFromCenter / trackWidth * 2) ** 2) # Max Reward = 25
        steeringReward = max(0, -0.025 * (steeringAngle ** 2) + 10) # Max Reward = 10
        progressReward = max(0, (progress - self.prevProgress) * 4) # Max Reward = 400 (Not Realistic)
        speedReward = 20 * (speed ** 91) # Max Reward = 20

        return float(wheelsOnTrackReward + centerReward + steeringReward + progressReward + speedReward)

rewardObject = Reward()

def reward_function(params):
    return rewardObject.rewardFunction(params)
