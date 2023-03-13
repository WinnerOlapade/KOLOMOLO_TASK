## Problem Solving
This *[folder](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/problem_solving/)* contains corrected *[problem_solving.py](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/problem_solving/problem_solving.py)* code
* Problem: File/code execution. the code refused to execute because the "if" statement in “line 41” ( `if __name__ == "main”:` ) wasn’t formatted properly.
  Solution: Correct format - ( `if __name__ == “__main__”:` ) to call main function correctly.

* Problem: AttributeError in line 17 (self.age == age) - the comparison operator (==) was used instead of assignment operator (=).
  Solution: Corrected to use the assignment “=“ operator.

* Problem: line 32 ( x = Person(p["first_name"], p["age"], p["last_name"]) ) the arguments were in the incorrect order. 
  Solution: Corrected to ( x = Person(p["first_name"], p["last_name"], p["age"]) ) to print the ages as integers.

* Problem: TypeError on line 25 ( `def increase_count()` ) increase_count definition needed a positional argument.
  Solution: Corrected to ( `def increase_count(self)` ).

* Added "for" statement in "main()" definition  
```
for thread in threads:
    thread.join()
``` 
to wait for thread to finish before proceeding so that "number of people created" is printed always at the very end.

