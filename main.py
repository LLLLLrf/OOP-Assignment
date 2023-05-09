'''
Introduction:
    Welcome here, this file is to make the program more user-friendly, so if you just  want to use the functions of this program, please run in this file.
    When you start the program, you will see three options, choose what you want to do by neter the number before it.
    If you want to save you tree after enter the equation, type in the name of the file, if the file already exist in "tree_files" it will save in it, if it do not exist in it, the program will create one and save your tree.
'''


import os
from assignment import *


while True:
    os.system("cls")
    print('Choose what you want to do, enter a number to tell me')
    print('1. Type in equation and print out the tree')
    print('2. Load a tree from file')
    print('3. Exit')
    ans = input()
    if ans == '1':
        os.system('cls')
        formula = input('please type in your equation\n')
        # test the equation first, if the equation has something wrong, exit the program now
        if not test(formula):
            os.system("pause")
            continue
        try:
            res = eval(formula)
        except (Exception) as e:
            print(repr(e))
            os.system("pause")
            continue
        # turn the equation into suffix expression
        suffix_expr = suffix(formula)
        root = build_tree(suffix_expr)
        print(f"the result is: {res}")
        print('=' * 60)
        print_inorder(root)
        # you can save a tree here
        ans2 = input("Do you want to save the tree? [Y/N]")
        if ans2 == "Y" or ans2 == "y":
            ans3 = input("please enter the file name(enter '1' for the default file)\n")
            if ans3 == '1':
                # save to the default file
                save_tree(root)
            else:
                # save to a specified file
                save_tree(root, ans3)
            print("saving successfully")
            os.system("pause")
    elif ans == '2':
        os.system('cls')
        print("file list:")
        for i in os.listdir("tree_files"):
            print(i)
        ans3 = input("please enter the file name(enter '1' for the default file)\n")
        if ans3 == '1':
            root = read_tree()
        else:
            root = read_tree(ans3)
        os.system("pause")
    elif ans == '3':
        print('Goodbye, see you next time ~')
        os.system('pause')
        break
    else:
        print("This is not an valid input, please make sure you only type in '1','2','3'")
        os.system("pause")