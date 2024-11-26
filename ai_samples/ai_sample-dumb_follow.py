import math

n_a_players = 0
n_b_players = 0
self_team = ''

def explode_input(input_str:str) :
    input_type, input_content = input_str.split(':')
    input_comments = ''
    input_vars_str = ''

    if '--' in input_content :
        input_vars_str, input_comments = input_content.split('--')
    else :
        input_vars_str = input_content
    input_var_dict = {el.split('=')[0] : el.split('=')[1] for el in input_vars_str.split(',')}

    return input_type, input_var_dict, input_comments

def extract_game_state(inp_var) :
    ball_pos = (float(inp_var['ball_pos_x']), float(inp_var['ball_pos_y']))
    ball_vel = (float(inp_var['ball_vel_x']), float(inp_var['ball_vel_y']))
    players_pos_temp = {'A':{}, 'B':{}}
    for i in range(n_a_players) :
        key = 'a_p'+str(i)+'_pos'
        players_pos_temp['A'][i] = (float(inp_var[key+'_x']), float(inp_var[key+'_y']))
    for i in range(n_b_players) :
        key = 'b_p'+str(i)+'_pos'
        players_pos_temp['B'][i] = (float(inp_var[key+'_x']), float(inp_var[key+'_y']))
    players_pos = {
        'self' : players_pos_temp[self_team],
        'oppo' : players_pos_temp['AB'.replace(self_team, '')],
    }
    score = {'A':int(inp_var['a_score']), 'B':int(inp_var['b_score'])}
    return ball_pos, ball_vel, players_pos, score


def follow_directives(player_pos, ball_pos) :
    vect_to_ball = (ball_pos[0] - player_pos[0], ball_pos[1] - player_pos[1])
    norm_vect = math.sqrt(vect_to_ball[0]**2 + vect_to_ball[1]**2)
    vect_to_ball_normalized = (vect_to_ball[0]/norm_vect, vect_to_ball[1]/norm_vect)
    return vect_to_ball_normalized, 500.

def stringify_actions(actions) :
    action_str = ''
    for key, val in actions.items() :
        if action_str :
            action_str += ','
        action_str += str(key)+'='+str(val)
    return action_str

def play(input_vars) :
    ball_pos, ball_vel, players_pos, score = extract_game_state(inp_vars)
    players_actions = {}
    for ind, pos in players_pos['self'].items() :
        follow_dir, follow_speed = follow_directives(pos, ball_pos)
        players_actions['p'+str(ind)+'_dir_x'] = follow_dir[0]
        players_actions['p'+str(ind)+'_dir_y'] = follow_dir[1]
        players_actions['p'+str(ind)+'_speed'] = follow_speed
        players_actions['p'+str(ind)+'_shootdir_x'] = -1.
        players_actions['p'+str(ind)+'_shootdir_y'] = -0.
        players_actions['p'+str(ind)+'_shootpow'] = 1000.
    print('debug: actions {0}'.format(players_actions))
    print('action:'+stringify_actions(players_actions))


print('hi')

# Program will respond with an input of the formm :
# hi:your_team=B,n_a_players=1,n_b_players=1,field_type=standard--ready?
# input_content = input().split(':')[1].split('--')
# game_params_str = input_content[0]
# comment = input_content[1]
# game_params = {el.split('=')[0] : el.split('=')[1] for el in game_params_str.split(',')}

raw_input = input()

inp_t, inp_vars, inp_com = explode_input(raw_input)
print('debug:', inp_t, str(inp_vars), inp_com)

n_a_players = int(inp_vars['n_a_players'])
n_b_players = int(inp_vars['n_b_players'])
self_team = inp_vars['your_team']

print('ready')

while True :
    raw_input = input()
    inp_t, inp_vars, inp_com = explode_input(raw_input)
    
    if inp_t == 'goal' :
        print('ok:got it')
    elif inp_t == 'reseted' :
        print('debug:recieved')
        print('ok:got it')
    elif inp_t == 'playing' :
        play(inp_vars)
    elif inp_t == 'end' :
        print('debug:END!')
        break




