from envs.JSBSim.envs.self_play_env import JSBSimSelfPlayEnv
import numpy as np
import pdb
from envs.env_wrappers import SubprocVecEnv, DummyVecEnv


env = JSBSimSelfPlayEnv()
# aileron  elevator  rudder  throttle
env.reset()
cur_step = -1
reward_blue, reward_red = 0., 0.
while True:
    cur_step += 1
    actions = {"red_fighter": np.array([20., 18.6, 20., 0.]), 'blue_fighter': np.array([20., 18.6, 20., 0.])}
    next_obs, reward, done, env_info = env.step(actions)
    reward_blue += reward['blue_fighter']
    reward_red += reward['red_fighter']
    print(reward_blue, reward_red)
    if done:
        print(env_info)
        break


# def make_train_env(num_env):
#     return SubprocVecEnv([JSBSimSelfPlayEnv for _ in range(num_env)])

# if __name__ == '__main__':
#     num_env = 4
#     envs = make_train_env(num_env)
#     envs.reset()
#     n_rollout = 0
#     while n_rollout < 20:
#         n_rollout += 1
#         while True:
#             actions = {"red_fighter": np.array([20., 18.6, 20., 0.]), 'blue_fighter': np.array([20., 18.6, 20., 0.])}
#             next_obs, reward, done, env_info = envs.step([actions for _ in range(num_env)])
#             if np.all(done):
#                 print(env_info)
#                 break
#     envs.close()
