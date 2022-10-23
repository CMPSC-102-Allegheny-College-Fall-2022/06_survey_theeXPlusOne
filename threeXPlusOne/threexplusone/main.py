""" Run a simple analysis of the equation, 3x+1.
This is a recursive function in which it is defined in a system by the following.

f(x)  = {3x+1} if f(x) is odd
f(x)  = (f(x)/2) if f(x) is even.

"""

""" output :
	 Enter a seed number : 7
	   1.	7 	 odd
	   2.	22	 even
	   3.	11 	 odd
	   4.	34	 even
	   5.	17 	 odd
	   6.	52	 even
	   7.	26	 even
	   8.	13 	 odd
	   9.	40	 even
	   10.	20	 even
	   11.	10	 even
	   12.	5 	 odd
	   13.	16	 even
	   14.	8	 even
	   15.	4	 even
	   16.	2	 even
	   17.	1 	 odd

	 [+] Completed at 1, MaxValue = 52
"""

from rich.console import Console
from rich import print
import typer

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(seed: str = typer.Option(..., prompt=True)) -> None:
    """Driver function for the math experiment using the seed number."""

    myResult = int(seed)
    if myResult < 0:
        print("[red] No negative numbers, please.[/red]")
        exit()

    numSeq_dic = {0: seed}  # The dictionary pairs the postition with the value.
    counter = 1
    maxValue_int = 0  # largest value of sequence
    while myResult != 1:

        if int(myResult % 2) == 0:  # even?
            print(
                f"\t   [white]{counter}[/white].\t[bright_yellow]{myResult}[/bright_yellow]\t [green]even[/green]"
            )
            # TODO: Assign myResult to equation for dealing with EVEN values.
            # TODO: Add to numseq_dic the counter(key) for the current value of myResult

        elif myResult % 2 == 1:  # odd?
            print(
                f"\t   [white]{counter}[/white].\t[bright_yellow]{myResult}[/bright_yellow] \t [red]odd[/red]"
            )
            # TODO: Assign myResult to equation for dealing with ODD values.
            # TODO: Add to numseq_dic the counter(key) for the current value of myResult

        counter = counter + 1
        # keep track of largest value for display at finish
        if myResult > maxValue_int:
            maxValue_int = myResult

    print(
        f"\t   [white]{counter}[/white].\t[bright_yellow]{1}[/bright_yellow] \t [red]odd[/red]"
    )
    numSeq_dic[counter] = 1
    print(f"\n\t [+] Completed at {myResult}, MaxValue = {maxValue_int}")

    return numSeq_dic  # We make a dictionary for potential analyais later. The dictionary pairs the postition with the value.


# end of main()
