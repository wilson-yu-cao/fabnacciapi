# fabnacciapi

Requirements
1. An endpoint that returns the value from the Fibonacci sequence for a given number.
2. An endpoint that returns a list of numbers and the corresponding values from the Fibonacci sequence from 1 to N with support for pagination. Page size
should be parameterized with a default of 100.
3. An endpoint to blacklist a number to permanently stop it from being shown in Fibonacci results when requested. The blacklisted numbers should persist in
application state.
4. An endpoint to remove a number from the blacklist.

Guidelines
+ Work on your solution using a preferred version control system. Commit frequently and share a link to the final repository with us.
+ Consider potential performance and concurrency problems. Be aware of limitations of your implementation (memory, cpu, time, network etc).
+ Document your code and API (readme or generated docs).
+ We value code quality. Use consistent and clean style across the codebase.
+ Make sure your API handles invalid input well.
+ Make sure code can be compiled and tests can be run and pass. Optionally add a Makefile.
+ Use publicly available libraries, but keep in mind that solution should be easily maintainable

This is the final work of Python Application Engineer Assignment.

Start  : July 16, 2019
Finish : July 16, 2019

Files:
main.py       The implementation of a RESTAPI under Flask framework
functions.py  The implementation of the functions required in the Assignment
test.py       Unit test cases, using Python unittest framework

Setup:
OS      Windows 10
Editor  Visual Studio Code
Browser Chrome
Python  V3.7.3
flask   V1.1.4
flask-restx  V0.4.0

Instructions:
    Start RESTAPI, python ./main.py
    RESTAPI doc URL, http://localhost:5000/
    
Start unittest:
    python ./test.py
                

