from build.game import is_movable_up_left_down_right
from build.game import get_board
import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import numpy as np
import random

# explorer用のランダム関数オブジェクト
class RandomActor:
    def __init__(self, n_actions):
        self.random_count = 0
        self.n_actions = 4

    def random_action_func(self):
        # no need for "quit"
        movable = [i for i, elem in enumerate(is_movable_up_left_down_right()) if elem]
        if not movable:
            return random.choice(range(self.n_actions))
        self.random_count += 1
        return random.choice(movable)


# Q関数
class QFunction(chainer.Chain):
    def __init__(self, obs_size, n_actions, n_hidden_channels=100):
        super().__init__(
            l0=L.Linear(obs_size, n_hidden_channels),
            l1=L.Linear(n_hidden_channels, n_hidden_channels),
            l2=L.Linear(n_hidden_channels, n_hidden_channels),
            l3=L.Linear(n_hidden_channels, n_actions))
    def __call__(self, x, test=False):
        h = F.relu(self.l0(x))
        h = F.relu(self.l1(h))
        h = F.relu(self.l2(h))
        return chainerrl.action_value.DiscreteActionValue(self.l3(h))


class AI:
    def __init__(self):
        self.reward = None
        obs_size = 16
        n_actions = 4 # no need for "quit"
        self.ra = RandomActor(n_actions)
        q_func = QFunction(obs_size, n_actions)
        q_func.to_gpu()
        optimizer = chainer.optimizers.RMSprop(eps=1e-2)
        optimizer.setup(q_func)
# 報酬の割引率(今回は長ければ長いほどよい)
        gamma = 1.000
# Epsilon-greedyを使ってたまに冒険。5000000ステップでend_epsilonとなる
        explorer = chainerrl.explorers.LinearDecayEpsilonGreedy(
            start_epsilon=1.0, end_epsilon=0.0, decay_steps=5000000, random_action_func=self.ra.random_action_func)
# Experience ReplayというDQNで用いる学習手法で使うバッファ
        replay_buffer = chainerrl.replay_buffer.ReplayBuffer(capacity=10 ** 6)
        phi = lambda x: x.astype(np.float32, copy=False)
# Agentの生成
        self.agent = chainerrl.agents.DoubleDQN(
            q_func, optimizer, replay_buffer, gamma, explorer,
            replay_start_size=500, update_interval=1,
            target_update_interval=100, phi=phi)

    def initialize(self):
        self.reward = 0.0
        last_state = np.array(get_board(), dtype='float32')

    def move(self):
        movable = [not elem for elem in is_movable_up_left_down_right()]
        if not movable:
            return "quit"
        board = np.array(get_board(), dtype='float32')
        actions = ["up", "left", "down", "right"]
        action = self.agent.act_and_train(board, self.reward)
        self.reward += 1.0
        return actions[action]

    def finalize(self):
        board = np.array(get_board(), dtype='float32')
        self.agent.stop_episode_and_train(board, self.reward, True)
        self.agent.save("result")
