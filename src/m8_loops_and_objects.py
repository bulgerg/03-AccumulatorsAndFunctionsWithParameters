"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and George Bulger.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math as m


def main():
    run_print_sequence1()
    run_draw_circles1()
    run_print_sequence2()
    run_draw_circles2()
    run_print_sequence3()
    run_print_cosines()
    run_draw_cosines_and_sines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def print_sequence1():
    for k in range(0, 201, 10):
        print(k)
    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """

    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------

def run_print_sequence1():
    # Test 1:
    print()
    print('--------------------------------------------------')
    print('Running print_sequence1:')
    print('--------------------------------------------------')
    print('Test 1 expected', '0')
    print('                10')
    print('                20')
    print('                30')
    print('                40')
    print('                50')
    print('                60')
    print('                70')
    print('                80')
    print('                90')
    print('                100')
    print('                110')
    print('                120')
    print('                130')
    print('                140')
    print('                150')
    print('                160')
    print('                170')
    print('                180')
    print('                190')
    print('                200')
    print('actual')
    print_sequence1()


def draw_circles1():
    window = rg.RoseWindow(400, 400)
    for k in range(0, 201, 10):
        rg.Circle(rg.Point(200, 200), k)
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         -- They have radii:  0  10  20  30  40 ... 200, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # HINT: You might find a prior module useful when 'writing' this code.
    # -------------------------------------------------------------------------
def run_draw_circles1():
    print()
    print('--------------------------------------------------')
    print('Running draw_circles1:  See graphics window')
    print('--------------------------------------------------')
    draw_circles1()


def print_sequence2():
    for k in range(50, 391, 20):
        print(k)
    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
def run_print_sequence2():
    # Test 1:
    print()
    print('--------------------------------------------------')
    print('Running print_sequence2:')
    print('--------------------------------------------------')
    print('Test 1 expected', '0')
    print('                50')
    print('                70')
    print('                90')
    print('                110')
    print('                130')
    print('                150')
    print('                170')
    print('                190')
    print('                210')
    print('                230')
    print('                250')
    print('                270')
    print('                290')
    print('                310')
    print('                330')
    print('                350')
    print('                370')
    print('                390')
    print('actual')
    print_sequence2()


def draw_circles2():
    window = rg.RoseWindow(400, 400)
    for k in range(50, 391, 20):
        rg.Circle(rg.Point(k, 100), 10)
        rg.Color('blue')
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 5. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
def run_draw_circles2():
    print()
    print('--------------------------------------------------')
    print('Running draw_circles2:  See graphics window')
    print('--------------------------------------------------')
    draw_circles2()


def print_sequence3():
    for k in range(1, 101, 1):
        print(k)
    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
def run_print_sequence3():
    print()
    print('--------------------------------------------------')
    print('Running print_sequence3:')
    print('--------------------------------------------------')
    print('Tesr 1 expected', 1)
    print('                2')
    print('                3')
    print('                4')
    print('                ...')
    print('                100')
    print('actual')
    print_sequence3()

def draw_circles3():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 7. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles3:  See graphics window')
    print('--------------------------------------------------')


def print_cosines():
    for k in range(0, 101, 1):
        print(m.cos(k)*80)
    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    # -------------------------------------------------------------------------
    # TODO: 8. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # -------------------------------------------------------------------------
def run_print_cosines():
    print()
    print('--------------------------------------------------')
    print('Running print_cosines:')
    print('--------------------------------------------------')
    print('Test #1 expected', 80)
    print('                  43.224184469451174')
    print('                  -33.29174692377139')
    print('                  -79.19939972803563')
    print('                  -52.29148966908895')
    print('                  22.6929748370581')
    print('                  76.81362293202928')
    print('                  60.31218034746437')
    print('                  ...')
    print('                  68.9855097830147')
    print('actual')
    print_cosines()


def draw_cosines_and_sines():
    window = rg.RoseWindow(400, 400)
    for k in range(0, 101, 1):
        rg.Circle(rg.Point((200 + (80*m.cos(k))), (200 + (80*m.sin(k)))), 10)
    window.close_on_mouse_click()

    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 9. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # -------------------------------------------------------------------------
def run_draw_cosines_and_sines():
    print()
    print('--------------------------------------------------')
    print('Running draw_cosines_and_sines:  See graphics window')
    print('--------------------------------------------------')
    draw_cosines_and_sines()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
