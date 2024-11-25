import json
shorts = {
    'short_cut': 'long_cut'
}
with open('shorts.json', 'w') as f:
    json.dump(shorts, f, indent=4, ensure_ascii=False)
# import json
# try:
#     with open('shorts.json', 'r') as f:
#         data = json.load(f)

# except:
#     print('shorts.json is empty')
#     data = {}

# def save_data():
#     with open('shorts.json', 'w') as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)


# def short_cut_creator():
#     while True:
#         print('Hello! My name is short-cut creator\n'
#               '1.Create short-cut\n'
#               '2.View all short-cuts\n'
#               '3.Delete short-cut\n'
#               'q.Exit')
#         choice = input('Enter your choice: ')
#         if choice == 'q':
#             break
#         elif choice == '1':
#             long_data = input('Please enter your http:')
#             short_data = input('Please enter your short-cut:')
#             data[short_data] = long_data
#             print(f'Short-cut {short_data} has been created successfully!')
#             save_data()
#         elif choice == '2':
#             if data == {}:
#                 print('No short-cuts found')
                
#             else:
#                 print('You shirt-cuts')
#                 for short, long in data.items():
#                     print(f'{short}: {long}')
                    
#         elif choice == '3':
#             if data == {}:
#                 print('No short-cuts found')
#                 break
#             else:
#                 for idx,shorts in enumerate(list(data.keys())):
                    
#                     print(f'{idx+1}. {shorts}')
#                 choice_delete = int(input('Enter number of short-cut to delete: '))
#                 if choice_delete < 1 or choice_delete > len(data):
#                     print('Invalid choice')
#                 else:
#                     del data[list(data.keys())[choice_delete-1]]
#                     save_data()
#                     print('Short-cut has been deleted successfully!')

# shorter = short_cut_creator()

                    
            