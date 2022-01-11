


def value_iteration():
    washroom, kitchen, bedroom, diningroom, under_attack, dead = 0, 1, 2, 3, 4, 5
    H, V, S, D, SD = 0, 1, 2, 3, 4
    states = (washroom, kitchen, bedroom, diningroom, under_attack, dead)  # states (tiles)
    actions = (H, V, S, D, SD)  # actions (0=left, 1=right)
    rewards = [4, 10, 0, 2, -50, 0]  # Direct rewards per state
    gamma = 0.5  # discount factor

    # level 1 current state, level 2 potential state, level 3 action
    probs = [
        [[0, 0, 0.75, None, None], [0.6, 0.4, 0, None, None], [0.4, 0.6, 0, None, None], [0, 0, 0, None, None], [0, 0, 0.25, None, None], [0, 0, 0, None, None]],
        [[0.6, 0.4, 0, None, None], [0, 0, 0.75, None, None], [0, 0, 0, None, None], [0.4, 0.6, 0, None, None], [0, 0, 0.25, None, None], [0, 0, 0, None, None]],
        [[0.4, 0.6, 0, None, None], [0, 0, 0, None, None], [0, 0, 0.75, None, None], [0.6, 0.4, 0, None, None], [0, 0, 0.25, None, None], [0, 0, 0, None, None]],
        [[0, 0, 0, None, None], [0.6, 0.4, 0, None, None], [0.4, 0.6, 0, None, None], [0, 0, 0.75, None, None], [0, 0, 0.25, None, None], [0, 0, 0, None, None]],
        [[None, None, None, 0, None], [None, None, None, 0, None], [None, None, None, 0, None], [None, None, None, 0, None], [None, None, None, 0, None], [None, None, None, None, 1]],
        [[None, None, None, None, 0], [None, None, None, None, 0], [None, None, None, None, 0], [None, None, None, None, 0], [None, None, None, None, 0], [None, None, None, None, 1]]
    ]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hi")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
