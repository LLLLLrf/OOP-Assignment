# README

## assignment2

***
### How to begin

Only **"+", "-", "*", "/", "(", ")"** are acceptible in the program
You can just run **main.py** for a quick start (Recommended)

The following are some examples of invalid expressions

```
(4*3*2)                     Not a valid expression, wrong number of operands.
(4*(2))                     Not a valid expression, wrong number of operands.
(4*(3+2)*(2+1))             Not a valid expression, wrong number of operands.
(2*4)*(3+2)                 Not a valid expression, brackets mismatched.
((2+3)*(4*5)                Not a valid expression, brackets mismatched.
(2+5)*(4/(2+2)))            Not a valid expression, bracket mismatched.
(((2+3)*(4*5))+(1(2+3)))    Not a valid expression, operator missing.
(1+(1*))                    Not a valid expression, one number missing.
(1+(-))                     Not a valid expression, two numbers missing.
(1%2)                       Not a valid expression, invalid symbol was entered.
```

### File Structure

```
├── README.md                   // help
├── tree_demo
│   └── default_read.pkl        // the default document for reading the tree
│   └── default_save.pkl        // the default document for saving the tree
├── assignment.py               // core code for turning an equation into a tree
├── main.py                     // platform for user
└── testunit.py                 // for testing whether the functions work as expected
```

### Function List

functions in **assignment.py**
```
suffix()         // receives an infix expression, turns it into suffix expression and returns it
build_tree()     // receives a suffix expression, turns the expression into tree structure and returns the root node
print_inorder()  // using inorder traversal to visualize the tree

match_bracket()  // checking whether the brackets in equation are matched
check_operands() // checking whether the number of operands in equation are correct
check_valid()    // checking whether all the input symbols are valid
test()           // controls the three functions above simultaneously

save_tree()      // save the root node of the tree into a document
read_tree()      // read the root node of the tree from a document and print it out by print_inorder()

main_function()  // controls all the functions except save_tree() and read_tree()
```


### Summary

In **assignment.py** you may 
- use： main_function() to turn the equation into a tree and print it out
- use： save_tree() to save the root node of the tree into a document
- use： read_tree() to read the root node of the tree from a document and print it out by print_inorder()

In **main.py** you may
- enter 1 to type in an equation
if you want to save this tree into a file, then press "Y" or "y" on keyboard, type in the file name that you want to save in, or you can just type in "1" to save in the default file.
if the file name you just entered has already existed in "tree_files" it will save in it, if it do not exist in it, the program will create one and save your tree.
- enter 2 to read a tree from a document
if you want to read a tree from a specified path, type in the name of the file or type in "1" to read from the default file
- enter 3 to exist the program