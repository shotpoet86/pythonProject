#
# personIKnow = {'first_name': 'mike',
#                'last_name': 'jones',
#                'age': '34',
#                'city': 'atlanta'
#                }
# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'usa',
#     'chatahooche': 'usa'
# }
#
#
#
# # loops thru the rivers dict and prints a message if rivers keys are included in the us_rivers list,
# # otherwise prints the egypt_rivers message
# us_rivers = ['chatahooche', 'mississippi']
# egypt_rivers = ['nile']
#
# for key in rivers.keys():
#     if key in us_rivers:
#         print(f'{str(us_rivers)[1:-2]} is a river in the usa')
#     else:
#         print(f'{str(egypt_rivers)[2:-2]} is a river in egypt')
#
# friends = ['mike', 'jones', 'atlanta']
# for names in personIKnow.keys():
#     if names in friends:
#         my_friend = personIKnow[names]
#         print(f'{names}, you are my friend')
#     else:
#         print(f'{personIKnow}  you are not my friend')
#
#
#
# # this prints the value of the dictionary which is
# # stored in results in the loop
# for results in personIKnow.values():
#     print(results.title())
#
#
#
# # this is the default looping thru a dict. It prints the key by default
# # without adding a specific function after personIKnow
# for name in personIKnow:
#     print(name)

#
# # creates three dict of different aliens
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# # creates list with all three alien dict in the list
# aliens = [alien_0, alien_1, alien_2]
# # loops thru the aliens list and prints to screen
# for alien in aliens:
#     print(alien)


aliens = []
# makes 30 green aliens
for alien_number in range(30):
    # this creates the standard attributes for new aliens
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # appends or adds the thirty new aliens to aliens list
    aliens.append(new_alien)

# loops and prints the first five aliens of aliens list
for alien in aliens[:5]:
    print(alien)
print('...')

# prints total number of aliens in list
print(f'total number on aliens  : {len(aliens)}')
