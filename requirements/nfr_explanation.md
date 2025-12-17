The chosen non-functional requirement was that the platform should be easy and intuitive to use.  
My implementation meets this requirement by providing a simple command-line interface that displays all meals, allows users to search by name, ingredient, or category
and loops in a clear, guided manner. Users are prompted explicitly whether they want to continue browsing, which gives them control over the flow and avoids confusion. 
The whole process is also given some very simple error handling, such as an output if a user gives a wrong input or if nothing is found etc. This way
the process of browsing and searching for meals is guided by an output explanation and the user is always given the explanation of what they can do at each step. 

Limitations:
- The prototype uses in-memory sample data and does not connect to a database- this example only provides built-in meals and cannot expand the list without editing it.
- The search is case-insensitive and doesn't understand typical typos etc. 
- The interface is text-based- there is no graphical user interface. It is also just a terminal app, so the user would need to run it with python installed.
