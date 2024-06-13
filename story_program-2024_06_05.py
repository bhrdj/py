# story_program-2024_06_05.py

chars = ['Geronimo','Violdelsia','Zayrakoro'] # watch the index
ages = {0:38, 1:13, 2:26} # key:value ~ chars_index:age
genders = {0:'Male', 1:'Female', 2:'Female'} # key:value ~ chars_index:gender

adventures = ['a','b','c']
key_challenges = {
        'a':'climbing a mountain',
        'b':'swimming across a lake',
        'c':'escaping from a cave',
        }
challenge_experts = {
        'a':'Zayrakoro',
        'b':'Violdelsia',
        'c':'Geronimo'
        }
stories = {}
stories['a'] = [
    'Long long ago, a young woman named {2} lost her necklace locket pendant in the woods.',
    'So she called out to her neighbors {1} and {0}.',
    '"Come, come, I need your help!" {2} yelled! "{3}"',
    '"Help, I lost my precious locket that has the key to my {4} inside!"',
    "Almost instantly, the neighbor's door opened and {1} came running down the dusty farm path, carrying a {5}-colored {6} in her hand."
    ]

input_prompts = {
    3:f'Type something that a {ages[2]}-year old {genders[2]} would yell: ',
    4:'Type something that would have a key and press ENTER: ',
    5:'Type a color and press ENTER: ',
    6:'Type something that it could be holding and press ENTER: ',
    }

default_fillers = {
    0:chars[0],
    1:chars[1],
    2:chars[2],
    3:'QUICK PLEASE!',
    4:'door',
    5:'blue',
    6:'bowl'
    }

print(*['\n']*40)  
madlib_dict = default_fillers
for i in input_prompts: # get the non-empty inputs
    new_input = input(input_prompts[i])
    if new_input!='':
        madlib_dict[i] = new_input

madlib_list = [madlib_dict[i] for i in sorted(madlib_dict.keys())]

print(*['\n']*5)  
print(*[i.format(*madlib_list) for i in stories['a']])
print(*['\n']*5)  

def user_def_vars():
    return [i for i in globals() if (
        i[0]!='_' 
        and 
        i not in ['In','Out','get_ipython','exit','quit','open']
        )
     ]

