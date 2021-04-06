Front-End
    --> Home Page --> Navbar --> Featured Problems --> Latest PRoblems
    --> Problems List --> Database --> Quick View
    --> User Profile
    --> About
    --> Problems Page --> Code Editor --> Run --> Submit --> JudgeAPI CAll
        Submission History
Models
    --> Problems
        ProblemStatement / Content --> Text
        Input / Output --> text
        Test Cases --> Output --> files/text
        Correct_output
        title
        Difficulty --> 1- Easy 2 -Medium 3-Hard
        time_limit
        
    --> Submission History
        user
        problemid
        datetime
        sourcecode
        verdict
        
    --> data
        problemid
        userid
        status --> solved/unsolved

Back-End
    --> Login/Registration
    --> Run & Compile
    --> JudgeAPI --> Submit
      --> ProblemID --> Get all details of that problem
      --> test_cases + correct_output + time_limit
      --> SourceCode --> user
      --> Pass it to rextester with test_cases + time_limit(inputs)
      --> Output --> CatchError: RunTimeError, TimeLimit, MLE.
      --> Compare with {correct_output}
      --> Give Verdict --> WA/AC/TLE --> If AC then --> Solved on data model.
      --> SubmissionHistory

--------------------JUDGE API--------------------------

1. Compile Errors
    (syntactical error)
    --> build_stderr
    --> build_exit_code = 256
    --> build_result = failure

2. Time Out/TLE
    --> result = timeout


3. Successful Execution
    --> Output -> stdout
    --> exit_code = 0
    --> time: time
    --> result = success


status_code = 200 --> SuccessRun -- Output

status_code = 400 --> Compile Errors

status_code = 300 --> TLE