import random

N_USERS = 2000
USERS = ["user" + str(i) for i in range(N_USERS)]

def _random_users_index():
    return random.randint(0, N_USERS - 1)

def get_random_user_id():
    return USERS[_random_users_index()]

def get_random_users(p_user_selected: float):
    return list(filter(lambda select: random.random() < p_user_selected, USERS))
