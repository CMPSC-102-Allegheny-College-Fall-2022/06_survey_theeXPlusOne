# ThreeXPlusOne Survey

## Assigned: Monday, October 24, 2022

## Due: Friday, October 24, 2022

## Project Goals

Build a sequence as described by the Collatz Conjecture.

## Rules

```
f(x) = 3x+1.
	 If f(x) is odd, f(f(x)) = 3(f(x) + 1) + 1,
	 else, f(x) = f(x) /2.
	 Repeat until f(x) = 4, then f(x) = 2 then f(x) = 1 (stop!)
```

## Instructions

Edit the File `threeXPlusOne/threexplusone/main.py` to allow for the following;

* Add functionality to model system of equations to build a sequence
* Allow program to run without errors.

Note: See slides for more information about the sequence.

## Execution

* Get into the virtual environment:
   + `poetry install`
* To get online help for the project
   + `poetry run threexplusone --help`. 
* To input a seed and run the project with a seed (such as 9)
   + `poetry run threexplusone --seed 9`

## Submission

As you are working, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the repository associated
with this assignment students will receive a checkmark grade if their last before-the-deadline
build passes. This is only checking some baseline writing and commit requirements as well as correct
running of the program. An additional reduction will be given if the commit log shows a cluster
of commits at the end clearly used just to pass this requirement. An addition reduction
will also be given if there is no commit during work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark
grade when the responses to the writing questions presented in the `reflection.md` reveal
a proficiency of both writing skills and technical knowledge. To receive a checkmark grade,
the submitted writing should have correct spelling, grammar, and punctuation in addition
to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion
of their assignment grade when their program implementation reveals that they have mastered
all of the technical knowledge and skills developed during the completion of this assignment.
As a part of this grade, the instructor will assess aspects of the programming including,
but not limited to, the completeness and the correctness of the program and the use of
effective source code comments.

## Seeking Assistance

Students who have questions about this project outside of the class or lab times are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.

## More Information
+ [Wikipedia: Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)

+ [The Simplest Math Problem No One Can Solve - Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg)

+ [UNCRACKABLE? The Collatz Conjecture - Numberphile](https://www.youtube.com/watch?v=5mFpVDpKX70)