<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Dhaval Patel(dap44)</td></tr>
<tr><td> <em>Generated: </em> 2/23/2022 10:30:46 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/dap44" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you&#39;re working in an up to date branch</p>
<ul>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b M4-Simple-Calc</code></li>
</ul>
<p>This will likely be started in class.</p>
<p>Steps:</p>
<ol>
<li>Create a new Folder called M4</li>
<li>Create a new file called MyCalc.py inside this folder</li>
<li>Create a MyCalc Class</li>
<li>Define basic addition / subtraction / multiplication / division functions<ol>
<li>These functions should update an internal variable as a running total/value called <code>ans</code></li>
<li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero)</li>
<li>Since you&#39;ll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li>
</ol>
</li>
<li>Define a &quot;main&quot; logic to run when the program runs</li>
<li>This logic should ask for user input<ol>
<li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol>
<li>This will do an immediate calculation, print it, and store the answer in the <code>ans</code> variable</li>
</ol>
</li>
<li>Alternatively, the input can be <code>ans</code>, any valid math operator, any valid number (i.e., <code>ans</code> * 2)<ol>
<li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the <code>ans</code> variable</li>
</ol>
</li>
</ol>
</li>
<li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass<ol>
<li>Test number-add-number</li>
<li>Test ans-add-number</li>
<li>Test number-sub-number</li>
<li>Test ans-sum-number</li>
<li>Test number-mult-number</li>
<li>Test ans-mult-number</li>
<li>Test number-div-number</li>
<li>Test ans-div-number</li>
</ol>
</li>
<li>Create a new file called m4_submission.md inside the M4 folder</li>
<li>Fill out the below deliverables</li>
<li>Generate the markdown and paste it into the m4_submission.md</li>
<li><code>git add .</code></li>
<li><code>git commit -m &quot;adding m4 hw&quot;</code></li>
<li><code>git push origin M4-Simple-Calc</code></li>
<li>Create a pull request M4-Simple-Calc to dev</li>
<li>Create a pull request dev to prod (after the previous one is merged)</li>
<li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li>
<li>Submit this link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155450398-4e83c2b6-9350-4ddc-9a34-06b6ce36bc20.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Addition function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155450398-4e83c2b6-9350-4ddc-9a34-06b6ce36bc20.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155450398-4e83c2b6-9350-4ddc-9a34-06b6ce36bc20.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155450398-4e83c2b6-9350-4ddc-9a34-06b6ce36bc20.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division Function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of passing number-add-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155451624-5b817277-e5aa-423f-a332-b2f78c6eed3c.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case number added to number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of passing ans-add-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155451729-4f7dd688-be00-49f8-b647-1cad2766dd1c.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case previous answer added to number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of passing number-sub-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155451786-fad2b0dd-54aa-4f86-9790-83a872c97fa5.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case number subtracted by  number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of passing ans-sub-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155451810-bdc00788-6201-4c0d-98f0-0750ad21415e.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case previous answer subtracted by a number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot of passing number-mult-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155451853-65aeca3b-004a-4b3b-8a31-97865248fcf4.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case number multiplied with number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot of passing ans-multi-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155452138-ea2bd413-932d-410d-8629-f42312a71012.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case previous answer multiplied to number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshot of passing number-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155452178-376226d2-c974-4128-bfd8-dd0840cb97ba.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case number divided by  number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshot of passing ans-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123361/155452196-2ea96ef5-e24b-484d-a9c4-18b0b9ec328f.JPG"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case previous answer divided by  number<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I learned about the python class and object during this assignment. Pytest module<br>introduced in this module was a new thing for me . It took<br>me lot of work and documentation to learn that. I am stilling learning<br>the pytest.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Test basically means checking the code is right or wrong. In test cases<br>we provide the input to the code and expected output  (which is<br>the correct output) .Then the function run through the code and checks the<br>output was the code and output we provide in test case function. If<br>that matches means the code is correct.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Dhavalpatel11/Dhavalpatel11-IS601-004/pull/7">https://github.com/Dhavalpatel11/Dhavalpatel11-IS601-004/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/dap44" target="_blank">Grading</a></td></tr></table>