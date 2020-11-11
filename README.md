## Summary
```
- TDD bread factory is the latest bread brand in Py Land. 
- It always produces the best bread because it has the best testing strategy!
```
#### What they do:
```
- Before they make any new bread, 
- They make a test to make sure the end output is correct. 
- Then they adjust the recipe until it's just right!
```
You are going to do the same with bread! This is called Test Driven Development.

## Tasks
- This exercise is going to bring together lots of concepts.

### Learning Outcomes
```
- git
- github
- functions
- TDD
- Separation of concerns - this is important do not ignore!
- DRY code
- DOD
```
### Installing and running
- To run the naan factory do the following:
```
import naan factory
run factory()
TDD - test driven development
```
```
- write the test
- run it, and read the error
- code and make it pass the test
```
```
This helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems
```
- How it works is that we write unit tests.

### Unit Tests
- Test single pieces of code. Like a function.

#### Base of a test
```
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with know variables
- asserting for expect output
```
### User stories for Naan Factory
```
#1
As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake dough with dough to get naan.

#3
As a user, I can user the run factory with water and flour and get naan.
```
### Acceptance Criteria
```
- you have written tests
- test pass
- you have written more test to make sure everything works as indented
- all user stories are satisfied
- code does not break
- code has exit condition
- DOD if followed
```

## Description
- relevant modules are imported
```
from factory import NaanFactory
import unittest
```
- class is initiated and an object created
```
class TestNaanFactory(unittest.TestCase):
    factory = NaanFactory()
```
- test the return of make_dough using two different assert methods
```
    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough('water', 'flour'), 'dough')
        self.assertNotEqual(self.factory.make_dough('sugar', 'flour'), 'dough')
```
- test the return of bake_naan using a single assert method
```
    def test_bake_naan(self):
        self.assertEqual(self.factory.bake_naan('dough'), 'bread')
'''
- test the return of run_factory with a single assert method
```
 def test_run_factory(self):
        self.assertTrue(self.factory.run_factory('water', 'flour'))
```
