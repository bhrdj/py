# story_program-2024_06_05.py

characters = ['Geronimo','Violdelsia','Zayrakoro']
ages = {'Geronimo':38,'Violdelsia':13,'Zayrakoro':26}
genders = {'Geronimo':'M','Violdelsia':'F','Zayrakoro':'F'}
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

print(*['\n']*40)  
madlib_list = []
madlib_list.append(input('Type something that would have a key and press ENTER: '))
madlib_list.append(input('Type a "color" and press ENTER: '))
madlib_list.append(input('Type something that she could be holding and press ENTER: '))

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

