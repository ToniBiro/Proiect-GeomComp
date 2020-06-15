# Documentation: Test Plan and Description for Backend

## Introduction

The Test Plan has been created to comunicate the test approch to team members. It incudes the objectives, scope and approuch. T document will clearly identify what the test deliverables will be and what is deemed in and out of scope.

## Objectives

The backend can be run into a Docker so that the test can be run automatically after each commit to make sure that all the features that worked previouselly are still working and that the new added features are working. It is more time-consiuming to do it this way, but it is a lot easier to create the test only once and then to be automatically run after each commit and you receive a mail to notify you that one or more test have failed. We are a small team so we don't have a test team, we all have the responsability to perform unit testing before adding a new feature. Also after the unit testing is done, that will becone part of the regresion test.

## Scope

All backend API must be tested tu ensure that whenever there is a bug in the frontend, it wasn't the API fault.
As new features will be added, the testing plan might include new tests.
All tests we will presume that all polygons reprezented as a polygonal chains are valid and their validity won't be checked.

## Test Approach
All test will be hardcoded, more complex testing is encoureged during the unit testing.
All test will be performed manually before they are verified and add them the the regresion tests.

## Test Environment

The backend is up and running on a server and the test will call an API and verify the API response.

# Test Description

- test polygon info
  - Description: Sends multiple post requests to the backed with a polygonal chain and all its circular permutations 
    ```
    Here is an example with all circular permutation for the follwing polygon chain: [(0, 0), (1, 0), (1, 1), (0, 1)]
      [(0, 0), (1, 0), (1, 1), (0, 1)], 
      [(1, 0), (1, 1), (0, 1), (0, 0)],  
      [(1, 1), (0, 1), (0, 0), (1, 0)],  
      [(0, 1), (0, 0), (1, 0), (1, 1)]
    ```
  - Target: all the circular permutatations of polygon chain must have same area, perimeter and type as specified in the expected response
  
- test polygon intersection
  - Description: Sends multiple post request to the beckend with 2 polygonal chains and all posibile combinations of the circular permutation for both of them
  - Target: all the intersection for the 2 polygonal chains and all posibile combinations of the circular permutations must have the same intersection. Warning: even if 2 polygonal chains might not have the same vertices order, one might be a circular permutation of the other one; If the intersection has more then one polygon, the poligons might appear in any order
  ```
  Here is an example with 2 intersection results that reprezents the same intersection:
    [[(0, 0), (0, 1), (1, 0)], [(1, 3), (3, 1), (3, 3)]]
    [[(3, 3), (3, 1), (1, 3)], [(1, 0), (0, 1), (0, 0)]]
  ```
