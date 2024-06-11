# story_program-2024_06_05.py

chars = ['Geronimo','Violdelsia','Zayrakoro']
ages = {chars[0]:38,chars[1]:13,chars[2]:26}
genders = {chars[0]:'M',chars[1]:'F',chars[2]:'F'}
adventures = [1,2,3]
key_challenges = {
        1:'climbing a mountain',
        2:'swimming across a lake',
        3:'escaping from a cave',
        }
challenge_experts = {
        1:'Zayrakoro',
        2:'Violdelsia',
        3:'Geronimo'
        }
stories = {}
stories[1] = [
    'Long long ago, a young woman named Zayrakoro lost her necklace locket pendant in the woods.',
    'So she called out to her neighbors Violdelsia and Geronimo.',
    '"Come, come, I need your help!" Zayrakoro yelled!',
    '"Help, I lost my precious locket that has the key to my {0} inside!"',
    "Almost instantly, the neighbor's door opened and Violdelsia came running down the dusty farm path, carrying a {1}-colored {2} in her hand."
    ]

input_prompts = {
    0:'Type something that would have a key and press ENTER: ',
    1:'Type a color and press ENTER: ',
    2:'Type something that it could be holding and press ENTER: ',
    }

default_fillers = {
    0:'door',
    1:'blue',
    2:'bowl'
    }

print(*['\n']*40)  
madlib_list = []
for i in input_prompts:
    new_input = input(input_prompts[i]) 
    edited_input = new_input if new_input!='' else default_fillers[i]
    madlib_list.append(edited_input)

print(*['\n']*5)  
print(*[i.format(*madlib_list) for i in stories[1]])
print(*['\n']*5)  

def user_def_vars():
    return [i for i in globals() if (
        i[0]!='_' 
        and 
        i not in ['In','Out','get_ipython','exit','quit','open']
        )
     ]

