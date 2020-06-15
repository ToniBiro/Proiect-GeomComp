# Documentation: Test Plan and Description for Backend

## Introduction

The Test Plan has been created to communicate the test approach to team members. It includes the objectives, scope and approach. T document will clearly identify what the test deliverables will be and what is deemed in and out of scope.

## Objectives

The backend can be run into a Docker so that the test can be run automatically after each commit to make sure that all the features that worked previously are still working and that the new added features are working. It is more time-consuming to do it this way, but it is a lot easier to create the test only once and then to be automatically run after each commit and you receive a mail to notify you that one or more tests have failed. We are a small team so we don't have a test team, we all have the responsibility to perform unit testing before adding a new feature. Also after the unit testing is done, that will become part of the regression test.

## Scope

All backend API must be tested to ensure that whenever there is a bug in the frontend, it wasn't the API fault.
As new features will be added, the testing plan might include new tests.
All tests we will presume that all polygons represented as polygonal chains are valid and their validity won't be checked.

## Tests Approach
All tests will be hardcoded, more complex testing is encouraged during the unit testing.
All tests will be performed manually before they are verified and add them to the regression tests.

## Test Environment

The backend is up and running on a server and the test will call an API and verify the API response.

# Test Description

- test polygon info
  - Description: Sends multiple post requests to the backed with a polygonal chain and all its circular permutations 
    ```
    Here is an example with all circular permutation for the following polygon chain: [(0, 0), (1, 0), (1, 1), (0, 1)]
      [(0, 0), (1, 0), (1, 1), (0, 1)], 
      [(1, 0), (1, 1), (0, 1), (0, 0)],  
      [(1, 1), (0, 1), (0, 0), (1, 0)],  
      [(0, 1), (0, 0), (1, 0), (1, 1)]
    ```
  - Target: all the circular permutations of polygon chain must have same area, perimeter and type as specified in the expected response
  
- test polygon intersection
  - Description: Sends multiple post request to the backend with 2 polygonal chains and all possible combinations of the circular permutation for both of them
  - Target: all the intersections for the 2 polygonal chains and all possible combinations of the circular permutations must have the same intersection. Warning: even if 2 polygonal chains might not have the same vertices order, one might be a circular permutation of the other one; If the intersection has more than one polygon, the polygons might appear in any order
  ```
  Here is an example with 2 intersection results that represents the same intersection:
    [[(0, 0), (0, 1), (1, 0)], [(1, 3), (3, 1), (3, 3)]]
    [[(3, 3), (3, 1), (1, 3)], [(1, 0), (0, 1), (0, 0)]]
  ```
