Exercise 1:
  - Environment: python 2.7.10, selenium 3.6.10
  - Execution: python webCaller.py
  - Comments:
     - webCaller.py main running program that performs all the main actions
     - Browser.py contains a factory class and object to store the page info
     - Some additional packages were use.To install them, example "pip install -u selenium"

Exercise 2:
  - Environment: maven 3.5.0, java 1.8.0_144
  - Execution: go to root folder (next to pom.xml) It might be overdoing it a bit to use Maven here, but wanted to play a bit with it and makes dependency mgt easier
            mvn package (if needed)
            mvn test
            my-test-1.0-SNAPSHOT.jar is also available under -/target
   - Comments:
        exercise2/my-test/src/test/java
        - myTest.java . Class that contains the tests
        - TestHelper.java. Class that handles most of the browser interaction through webdriver
        - CalendarHelper.java. Provides some specific date related functions
    - Note:
        - Missing to handle problematic cases when specific appt is not available in the select dates!!! Should get 1st available date from left-side panel info
        - Random dates are for now selected only within this year to avoid complexity of year change
