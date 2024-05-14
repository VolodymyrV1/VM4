from pathlib import Path


def get_cats_info(path):
    try:
        with open(path, 'r') as file:
            cats = file.readlines()
            #cats_i = {'id': '', 'name': '', 'age': ''}
            cats_info = []
            for cat in cats:
                one_cat = { 
                'id': cat.split(',')[0].strip(),  
                'name': cat.split(',')[1].strip(),
                'age': cat.split(',')[2].strip(),
                }
                # if one_cat['age'] != int:
                #     print('erorr age')
                # else:
                cats_info.append(one_cat)
               
        return cats_info   
    
    except FileNotFoundError:
        print("Didn't find txt file!")
    
    except Exception as e:
        print(f'{e} with file')


cats_info = get_cats_info("/Users/volodymyr/Desktop/VM4/EX_2/cats_file.txt")
print(cats_info)

