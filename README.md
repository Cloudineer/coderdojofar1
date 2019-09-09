# coderdojofar1

September 2019 - ready to turn into a computational sponge, soaking up as much knowledge and skills as possible. This term we will be constructing mazes and finding either our way out of them or other sprites inside them. You have the choice of language, but I suggest Python.    

The first task is to write a program to draw a maze based on the following set of number:

| Start X | Start Y | End X | End Y |
|---------|---------|-------|-------|
| 1 | 1 | 9 | 1 |
| 9 | 1 | 9 | 8 |
| 1 | 1 | 1 | 8 |
| 4 | 1 | 4 | 8 |
| 4 | 4 | 9 | 4 |

Which should make something that looks like:

```
      ..........
      *********.
      *..*....*.
      *..*....*.
      *..******.
      *..*....*.
      *..*....*.
      *..*....*.
      *********.
```

If you want to do this in Scratch you can, but you will need to make a list of lists. Each list will have 4 numbers, so it will look something like ListofLists.png (which can be found in this folder).

## Pass the tests

We will be using some unittests in the future, but when drawing stuff on screen it is impossible (well very difficult) to test automatically.

### Unit-test notes

Download these files into a new folder. Remember you must download them as RAW files, click on the filename to see the file, then right-click on the RAW button and click on Save Target as... (or something similar to that - it varies from browser to browser). To run the tests under Windows, open a command window, by hitting WINDOWS-R then cmd<RETURN>. Then cd into the directory with the python files and type:

$ py -m unittest 

To find where you files are I suggest you open windows explorer and go to My Computer -> C: -> Users -> _your username_, and find the folder where you downloaded these files. That PATH is what you put after _cd_ to change to the right directory.

When you having all of your tests passing, remove the _#_ from the start of the lines for the next test and try that test. Work your way down the test files until all tests pass. 

Remember this is also about teamwork. You do not have to write all of the code yourself, try to share the tests classes; every test must be passed by the group not by each individual.

There are some comments in the test classes to give you hints on how to pass each test.

## Your Mission for Today

To write them just pass the tests in the related test_xxxx.py file. When the tests pass, then uncomment (ie remove the # from the start of the line) of the next test.

Remember that Google is your friend when it comes to coding. If you get stuck try a search to find an answer. A website called StackOverflow is often the best place for answers to coding questions.

*Hint* to run the tests from within IDLE (or any IDE), add the following two lines to the end of your test script:

```
if __name__ == "__main__":
    unittest.main()
```
