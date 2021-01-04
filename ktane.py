def split(serial_number):
    return [char for char in serial_number]

serial_number_validity = 0
serial_number_elements = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
serial_number = (split((input('Serial number: ').lower())))
serial_number_element_check = [x for x in serial_number if x in serial_number_elements]
if len(serial_number) != len(serial_number_element_check):
    serial_number_validity = 1
elif len(serial_number) != 6:
    serial_number_validity = 1
elif serial_number[len(serial_number) - 1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    serial_number_validity = 1
else:
    serial_number_validity = 0
while serial_number_validity == 1:
    print('That serial number was incorrect: Retry')
    serial_number = (split((input('Serial number: ').lower())))
    serial_number_element_check = [x for x in serial_number if x in serial_number_elements]
    if len(serial_number) != len(serial_number_element_check):
        serial_number_validity = 1
    elif len(serial_number) != 6:
        serial_number_validity = 1
    elif serial_number[len(serial_number) - 1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        serial_number_validity = 1
    else:
        serial_number_validity = 0
serial_number_count = len(serial_number)
battery_count_validity = 1
battery_count = input('Number of batteries: ')
while battery_count_validity == 1:
    try:
        battery_count = int(battery_count)
        if battery_count > -1:
            battery_count_validity = 0
        else:
            battery_count = input('Invalid input: Retry ')
    except ValueError:
        battery_count_validity = 1
        print('Invalid number of batteries: Retry ')
        battery_count = input('Number of batteries: ')
def ynvalid(x):
    yn_validity = 1
    while yn_validity == 1:
        if x == 'y':
            yn_validity = 0
        elif x == 'n':
            yn_validity = 0
        else:
            yn_validity = 1
            x = (input('Invalid input: Retry '))
    return(x)
lit_indicator_CAR = ynvalid((input("Lit indicator 'CAR'? (Y/N) ").lower()))
lit_indicator_FRK = ynvalid((input("Lit indicator 'FRK'? (Y/N) ").lower()))
parallel_port_check = ynvalid((input('Is there a parallel port? (Y/N) ').lower()))

x = 0

while x == 0:
    module_validity = 0
    module = (input("Which module? [1] Wires, [2] Button, [3] Keypads, [4] Simon Says, [5] Who's on First, [6] Memory, [7] Morse Code, [8] Complicated Wires, [9] Wire Sequences, [10] Mazes, [11] Passwords, [12] Needy Knobs, [n] New Bomb, [x] Exit ").lower())
    if module == '1':
        wires = (input('Input wires in order (e.g. white yellow yellow black red) ').split())
        valid_wires = ['red', 'white', 'blue', 'black', 'yellow', 'red', 'white', 'blue', 'black', 'yellow', 'red', 'white', 'blue', 'black', 'yellow', 'red', 'white', 'blue', 'black', 'yellow', 'red', 'white', 'blue', 'black', 'yellow', 'red', 'white', 'blue', 'black', 'yellow']
        wires_validity_check = [x for x in wires if x in valid_wires]
        wires_validity = 0
        if len(wires) < 3 or len(wires) > 6:
            wires_validity = 1
        elif len(wires) != len(wires_validity_check):
            wires_validity = 1
        else:
            wires_validity = 0
        while wires_validity == 1:
            wires = (input('Invalid input: Retry ').split())
            wires_validity_check = [x for x in wires if x in valid_wires]
            if len(wires) < 3 or len(wires) > 6:
                wires_validity = 1
            elif len(wires) != len(wires_validity_check):
                wires_validity = 1
            else:
                wires_validity = 0
        wires_count = len(wires)
        blue_wires = [blue for blue in wires if blue == 'blue']
        blue_wires_count = len(blue_wires)
        red_wires = [red for red in wires if red == 'red']
        red_wires_count = len(red_wires)
        yellow_wires = [yellow for yellow in wires if yellow == 'yellow']
        yellow_wires_count = len(yellow_wires)
        white_wires = [white for white in wires if white == 'white']
        white_wires_count = len(white_wires)
        if wires_count == 3:
            if 'red' not in wires:
                print('Cut the second wire')
            elif blue_wires_count > 1:
                if wires[2] == 'blue':
                    print('Cut the last wire')
                else:
                    print('Cut the second wire')
            else:
                print('Cut the last wire')
        elif wires_count == 4:
            if red_wires_count > 1 and serial_number[(serial_number_count) - 1] in ['1', '3', '5', '7', '9']:
                if wires[3] == 'red':
                    print('Cut the last wire')
                elif wires[2] == 'red':
                    print('Cut the third wire')
                elif wires[1] == 'red':
                    print('Cut the second wire')
            elif wires[3] == 'yellow' and red_wires_count == 0:
                print('Cut the first wire')
            elif blue_wires_count == 1:
                print('Cut the first wire')
            elif yellow_wires_count > 1:
                print('Cut the last wire')
            else:
                print('Cut the second wire')
        elif wires_count == 5:
            if wires[4] == 'black' and serial_number[(serial_number_count) - 1] in ['1', '3', '5', '7', '9']:
                print('Cut the fourth wire')
            elif red_wires_count == 1 and yellow_wires_count > 1:
                print('Cut the first wire')
            elif 'black' not in wires:
                print('Cut the second wire')
            else:
                print('Cut the first wire')
        else:
            if yellow_wires_count == 0 and serial_number[(serial_number_count) - 1] in ['1', '3', '5', '7', '9']:
                print('Cut the third wire')
            elif yellow_wires_count == 1 and white_wires_count > 1:
                print('Cut the fourth wire')
            elif red_wires_count == 0:
                print('Cut the last wire')
            else:
                print('Cut the fourth wire')
    elif module == '2':
        button_colour = input('What is the colour of the button? (e.g. red) ')
        def validButton(button_colour):
            button_colour_split = button_colour.split()
            button_colour_list = ['white', 'red', 'blue', 'yellow']
            button_colour_validity_check = [x for x in button_colour_split if x in button_colour_list]
            if len(button_colour_split) != 1:
                button_colour_validity = 1
            elif len(button_colour_validity_check) != 1:
                button_colour_validity = 1
            else:
                button_colour_validity = 0
            while button_colour_validity == 1:
                button_colour = input('Invalid input: Retry ')
                button_colour_split = button_colour.split()
                button_colour_validity_check = [x for x in button_colour_split if x in button_colour_list]
                if len(button_colour_split) != 1:
                    button_colour_validity = 1
                elif len(button_colour_validity_check) != 1:
                    button_colour_validity = 1
                else:
                    button_colour_validity = 0
        validButton(button_colour)
        button_text = input('What does the text on the button read? (e.g. hold) ')
        button_text_split = button_text.split()
        button_text_list = ['hold', 'press', 'detonate']
        button_text_validity_check = [x for x in button_text_split if x in button_text_list]
        if len(button_text_split) != 1:
            button_text_validity = 1
        elif len(button_text_validity_check) != 1:
            button_text_validity = 1
        else:
            button_text_validity = 0
        while button_text_validity == 1:
            button_text = input('Invalid input: Retry ')
            button_text_split = button_text.split()
            button_text_validity_check = [x for x in button_text_split if x in button_text_list]
            if len(button_text_split) != 1:
                button_text_validity = 1
            elif len(button_text_validity_check) != 1:
                button_text_validity = 1
            else:
                button_text_validity = 0
        if battery_count > 1 and button_text == 'detonate':
            print('Press and immediately release the button')
        elif battery_count > 2 and lit_indicator_FRK == 'y':
            print('Press and immediately relase the button')
        elif button_colour == 'red' and button_text == 'hold':
            print('Press and immediately release the button')
        else:
            print('Hold the button')
            strip_colour = input('What colour is the strip? (e.g. blue) ')
            validButton(strip_colour)
            if strip_colour == 'blue':
                print('Release the button when the countdown timer has a 4 in any position')
            elif strip_colour == 'yellow':
                print('Release the button when the countdown timer has a 5 in any position')
            else:
                print('Release the button when the countdown timer has a 1 in any position')
    elif module == '3':
        print("1: Empty tennis racket")
        print("2: Pyramid with a 'T' inside of it")
        print("3: Lambda with a small line crossing the top of it")
        print("4: 'N' backwards with squiggly start and ending")
        print("5: Like a 'H' but the right side is a triangle on top of a sideways Euro sign")
        print("6: Squiggly 'H' or 'x' with a small comma attached on the bottom right")
        print("7: Backwards 'C' with a dot in the middle")
        print("8: Backwards Euro sign with two dots above it")
        print("9: Like a fancy, squiggly version of the letters 'co' joined together")
        print("10: White star")
        print("11: Upside down '?'")
        print("12: Copyright symbol")
        print("13: Like a big, squiggly 'W' with a comma and a '~' above it")
        print("14: Like two 'K's put back to back with a flick down in the bottom left (like and 'I' in the middle)")
        print("15: Almost a '3' but the bottom is missing, flick down in the bottom right")
        print("16: A '6' with the top slightly squished down")
        print("17: Backwards 'P', filled in")
        print("18: Like a 'b' and a 'T' put together in Times New Roman font")
        print("19: Smiley face with a tongue sticking out")
        print("20: Jewish candles / trident")
        print("21: 'C' with a dot in the middle")
        print("22: A '3' with an antennae at the top and curve at the bottom")
        print("23: Black star (filled in)")
        print("24: Like a not-equals-to sign slanted or like half a '#'")
        print("25: The letters 'ae' squished together")
        print("26: Like a 'H' but the middle is diagonal, hook in bottom right, small telephone on top")
        print("27: Omega sign")
        keypads = (input('Enter the four numbers that are referring to the symbols you have (e.g. 8 12 5 22): ').split())
        c1 = ['1', '2', '3', '4', '5', '6', '7']
        c2 = ['8', '1', '7', '9', '10', '6', '11']
        c3 = ['12', '13', '9', '14', '15', '3', '10']
        c4 = ['16', '17', '18', '5', '14', '11', '19']
        c5 = ['20', '19', '18', '21', '17', '22', '23']
        c6 = ['16', '8', '24', '25', '20', '26', '27']
        c1_combined = [a for a in c1 if a in keypads]
        c2_combined = [b for b in c2 if b in keypads]
        c3_combined = [c for c in c3 if c in keypads]
        c4_combined = [d for d in c4 if d in keypads]
        c5_combined = [e for e in c5 if e in keypads]
        c6_combined = [f for f in c6 if f in keypads]
        keypads_validity = 1
        while keypads_validity == 1:
            if len(c1_combined) == 4:
                keypads_validity = 0
                print('Press the symbols in this order (you may have to refer to the above list):')
                print(c1_combined)
            elif len(c2_combined) == 4:
                keypads_validity = 0
                print('Press the symbols in this order (you may have to refer to the above list):')
                print(c2_combined)
            elif len(c3_combined) == 4:
                keypads_validity = 0
                print('Press the symbols in this order (you may have to refer to the above list):')
                print(c3_combined)
            elif len(c4_combined) == 4:
                keypads_validity = 0
                print('Press the symbols in this order (you may have to refer to the above list):')
                print(c4_combined)
            elif len(c5_combined) == 4:
                keypads_validity = 0
                print('Press the symbols in this order (you may have to refer to the above list):')
                print(c5_combined)
            elif len(c6_combined) == 4:
                keypads_validity = 0
                print('Press the symbols in this order (you may have to refer to the above list):')
                print(c6_combined)
            else:
                keypads = (input('Invalid input: Retry ').split())
                c1_combined = [a for a in c1 if a in keypads]
                c2_combined = [b for b in c2 if b in keypads]
                c3_combined = [c for c in c3 if c in keypads]
                c4_combined = [d for d in c4 if d in keypads]
                c5_combined = [e for e in c5 if e in keypads]
                c6_combined = [f for f in c6 if f in keypads]
    elif module == '4':
        vowel = ['a', 'e', 'i', 'o', 'u']
        vowel_check = [z for z in serial_number if z in vowel]
        strike_count = input('How many strikes? ')
        strike_count_validity = 1
        if strike_count == '0':
            strike_count_validity = 0
        elif strike_count == '1':
            strike_count_validity = 0
        elif strike_count == '2':
            strike_count_validity = 0
        else:
            while strike_count_validity == 1:
                strike_count = input('Invalid input: Retry ')
                if strike_count == '0':
                    strike_count_validity = 0
                elif strike_count == '1':
                    strike_count_validity = 0
                elif strike_count == '2':
                    strike_count_validity = 0
        def validFlash(x):
            valid_flash_list = ['green', 'red', 'yellow', 'blue']
            flash_split = x.split()
            flash_validity_check = [z for z in flash_split if z in valid_flash_list]
            while len(flash_validity_check) != 1:
                x = input('Invalid input: Retry ')
                flash_split = x.split()
                flash_validity_check = [z for z in flash_split if z in valid_flash_list]
            return(x)
        if strike_count == '0':
            if len(vowel_check) > 0:
                first_flash = validFlash(input('What colour is the first flash? '))
                if first_flash == 'red':
                    ss_list = ['blue']
                elif first_flash == 'blue':
                    ss_list = ['red']
                elif first_flash == 'green':
                    ss_list = ['yellow']
                else:
                    ss_list = ['green']
                ss_loop = 'n'
                print('Press: ')
                print(ss_list)
                while ss_loop == 'n':
                    next_flash = validFlash(input('What colour is the new flash? '))
                    if next_flash == 'red':
                        ss_list.append('blue')
                    elif next_flash == 'blue':
                        ss_list.append('red')
                    elif next_flash == 'green':
                        ss_list.append('yellow')
                    else:
                        ss_list.append('green')
                    print('Press: ')
                    print(ss_list)
                    ss_loop = ynvalid((input('Has the module finished (Y/N)? ').lower()))
            elif len(vowel_check) == 0:
                first_flash = validFlash(input('What colour is the first flash? '))
                if first_flash == 'red':
                    ss_list = ['blue']
                elif first_flash == 'blue':
                    ss_list = ['yellow']
                elif first_flash == 'green':
                    ss_list = ['green']
                else:
                    ss_list = ['red']
                ss_loop = 'n'
                print('Press: ')
                print(ss_list)
                while ss_loop == 'n':
                    next_flash = validFlash(input('What colour is the new flash? '))
                    if next_flash == 'red':
                        ss_list.append('blue')
                    elif next_flash == 'blue':
                        ss_list.append('yellow')
                    elif next_flash == 'green':
                        ss_list.append('green')
                    else:
                        ss_list.append('red')
                    print('Press: ')
                    print(ss_list)
                    ss_loop = ynvalid((input('Has the module finished (Y/N)? ').lower()))
        elif strike_count == '1':
            if len(vowel_check) > 0:
                first_flash = validFlash(input('What colour is the first flash? '))
                if first_flash == 'red':
                    ss_list = ['yellow']
                elif first_flash == 'blue':
                    ss_list = ['green']
                elif first_flash == 'green':
                    ss_list = ['blue']
                else:
                    ss_list = ['red']
                ss_loop = 'n'
                print('Press: ')
                print(ss_list)
                while ss_loop == 'n':
                    next_flash = validFlash(input('What colour is the new flash? '))
                    if next_flash == 'red':
                        ss_list.append('yellow')
                    elif next_flash == 'blue':
                        ss_list.append('green')
                    elif next_flash == 'green':
                        ss_list.append('blue')
                    else:
                        ss_list.append('red')
                    print('Press: ')
                    print(ss_list)
                    ss_loop = ynvalid((input('Has the module finished (Y/N)? ').lower()))
            elif len(vowel_check) == 0:
                first_flash = validFlash(input('What colour is the first flash? '))
                if first_flash == 'red':
                    ss_list = ['red']
                elif first_flash == 'blue':
                    ss_list = ['blue']
                elif first_flash == 'green':
                    ss_list = ['yellow']
                else:
                    ss_list = ['green']
                ss_loop = 'n'
                print('Press: ')
                print(ss_list)
                while ss_loop == 'n':
                    next_flash = validFlash(input('What colour is the new flash? '))
                    if next_flash == 'red':
                        ss_list.append('red')
                    elif next_flash == 'blue':
                        ss_list.append('blue')
                    elif next_flash == 'green':
                        ss_list.append('yellow')
                    else:
                        ss_list.append('green')
                    print('Press: ')
                    print(ss_list)
                    ss_loop = ynvalid((input('Has the module finished (Y/N)? ').lower()))
        elif strike_count == '2':
            if len(vowel_check) > 0:
                first_flash = validFlash(input('What colour is the first flash? '))
                if first_flash == 'red':
                    ss_list = ['green']
                elif first_flash == 'blue':
                    ss_list = ['red']
                elif first_flash == 'green':
                    ss_list = ['yellow']
                else:
                    ss_list = ['blue']
                ss_loop = 'n'
                print('Press: ')
                print(ss_list)
                while ss_loop == 'n':
                    next_flash = validFlash(input('What colour is the new flash? '))
                    if next_flash == 'red':
                        ss_list.append('green')
                    elif next_flash == 'blue':
                        ss_list.append('red')
                    elif next_flash == 'green':
                        ss_list.append('yellow')
                    else:
                        ss_list.append('blue')
                    print('Press: ')
                    print(ss_list)
                    ss_loop = ynvalid((input('Has the module finished (Y/N)? ').lower()))
            elif len(vowel_check) == 0:
                first_flash = validFlash(input('What colour is the first flash? '))
                if first_flash == 'red':
                    ss_list = ['yellow']
                elif first_flash == 'blue':
                    ss_list = ['green']
                elif first_flash == 'green':
                    ss_list = ['blue']
                else:
                    ss_list = ['red']
                ss_loop = 'n'
                print('Press: ')
                print(ss_list)
                while ss_loop == 'n':
                    next_flash = validFlash(input('What colour is the new flash? '))
                    if next_flash == 'red':
                        ss_list.append('yellow')
                    elif next_flash == 'blue':
                        ss_list.append('green')
                    elif next_flash == 'green':
                        ss_list.append('blue')
                    else:
                        ss_list.append('red')
                    print('Press: ')
                    print(ss_list)
                    ss_loop = ynvalid((input('Has the module finished (Y/N)? ').lower()))
    elif module == '5':
        ready_list = ['yes', 'okay', 'what', 'middle', 'left', 'press', 'right', 'blank', 'ready', 'no', 'first', 'uhhh', 'nothing', 'wait']
        first_list = ['left', 'okay', 'yes', 'middle', 'no', 'right', 'nothing', 'uhhh', 'wait', 'ready', 'blank', 'what', 'press', 'first']
        no_list = ['blank', 'uhhh', 'wait', 'first', 'what', 'ready', 'right', 'yes', 'nothing', 'left', 'press', 'okay', 'no', 'middle']
        blank_list = ['wait', 'right', 'okay', 'middle', 'blank', 'press', 'ready', 'nothing', 'no', 'what', 'left', 'uhhh', 'yes', 'first']
        nothing_list = ['uhhh', 'right', 'okay', 'middle', 'yes', 'blank', 'no', 'press', 'left', 'what', 'wait', 'first', 'nothing', 'ready']
        yes_list = ['okay', 'right', 'uhhh', 'middle', 'first', 'what', 'press', 'ready', 'nothing', 'yes', 'left', 'blank', 'no', 'wait']
        what_list = ['uhhh', 'what', 'left', 'nothing', 'ready', 'blank', 'middle', 'no', 'okay', 'first', 'wait', 'yes', 'press', 'right']
        uhhh_list = ['ready', 'nothing', 'left', 'what', 'okay', 'yes', 'right', 'no', 'press', 'blank', 'uhhh', 'middle', 'wait', 'first']
        left_list = ['right', 'left', 'first', 'no', 'middle', 'yes', 'blank', 'what', 'uhhh', 'wait', 'press', 'ready', 'okay', 'nothing']
        right_list = ['yes', 'nothing', 'ready', 'press', 'no', 'wait', 'what', 'right', 'middle', 'left', 'uhhh', 'blank', 'okay', 'first']
        middle_list = ['blank', 'ready', 'okay', 'what', 'nothing', 'press', 'no', 'wait', 'left', 'middle', 'right', 'first', 'uhhh', 'yes']
        okay_list = ['middle', 'no', 'first', 'yes', 'uhhh', 'nothing', 'wait', 'okay', 'left', 'ready', 'blank', 'press', 'what', 'right']
        wait_list = ['uhhh', 'no', 'blank', 'okay', 'yes', 'left', 'first', 'press', 'what', 'wait', 'nothing', 'ready', 'right', 'middle']
        press_list = ['right', 'middle', 'yes', 'ready', 'press', 'okay', 'nothing', 'uhhh', 'blank', 'left', 'first', 'what', 'no', 'wait']
        you_list = ['sure', 'you are', 'your', "you're", 'next', 'uh', 'huh', 'ur', 'hold', 'what?', 'you', 'uh', 'uh', 'like', 'done', 'u']
        you_are_list = ['your', 'next', 'like', 'uh huh', 'what?', 'done', 'uh uh', 'hold', 'you', 'u', "you're", 'sure', 'ur', 'you are']
        your_list = ['uh uh', 'you are', 'uh huh', 'your', 'next', 'ur', 'sure', 'u', "you're", 'you', 'what?', 'hold', 'like', 'done']
        youre_list = ['you', "you're", 'ur', 'next', 'uh uh', 'you are', 'u', 'your', 'what?', 'uh huh', 'sure', 'done', 'like', 'hold']
        ur_list = ['done', 'u', 'ur', 'uh huh', 'what?', 'sure', 'your', 'hold', "you're", 'like', 'next', 'uh uh', 'you are', 'you']
        u_list = ['uh huh', 'sure', 'next', 'what?', "you're", 'ur', 'uh uh', 'done', 'u', 'you', 'like', 'hold', 'you are', 'your']
        uh_huh_list = ['uh huh', 'your', 'you are', 'you', 'done', 'hold', 'uh uh', 'next', 'sure', 'like', "you're", 'ur', 'u', 'what?']
        uh_uh_list = ['ur', 'u', 'you are', "you're", 'next', 'uh uh', 'done', 'you', 'uh huh', 'like', 'your', 'sure', 'hold', 'what?']
        what_q_mark_list = ['you', 'hold', "you're", 'your', 'u', 'done', 'uh uh', 'like', 'you are', 'uh huh', 'ur', 'next', 'what?', 'sure']
        done_list = ['sure', 'uh huh', 'next', 'what?', 'your', 'ur', "you're", 'hold', 'like', 'you', 'u', 'you are', 'uh uh', 'done']
        next_list = ['what?', 'uh huh', 'uh uh', 'your', 'hold', 'sure', 'next', 'like', 'done', 'you are', 'ur', "you're", 'u', 'you']
        hold_list = ['you are', 'u', 'done', 'uh uh', 'you', 'ur', 'sure', 'what?', "you're", 'next', 'hold', 'uh huh', 'your', 'like']
        sure_list = ['you are', 'done', 'like', "you're", 'you', 'old', 'uh huh', 'ur', 'sure', 'u', 'what?', 'next', 'your', 'uh uh']
        like_list = ["you're", 'next', 'u', 'ur', 'hold', 'done', 'uh uh', 'what?', 'uh huh', 'you', 'like', 'sure', 'you are', 'your']
        def validWordOptions(x):
            word_options_list = ['ready','first','no','blank','nothing','yes','what','uhhh','left','right','middle','okay','wait','press','you','you are','your',"you're",'ur','u','uh huh','uh uh','what?','done','next','hold','sure','like']
            user_options_validity = 1
            while user_options_validity == 1:
                if x in word_options_list:
                    user_options_validity = 0
                else:
                    x = input('Invalid input: Retry ')
                    user_options_validity = 1
            return(x)
        display_word = (input("What does the display read? (If there is no word on display, enter a space: ' ') "))
        display_word_list = ['yes','first','display','okay','says','nothing',' ','blank','no','led','lead','read','red','reed','leed','hold on','you','you are','your',"you're",'ur','there',"they're",'their','cee','c','see','they are']
        display_word_validity = 1
        display_word_list_validity = [a for a in display_word_list if a in display_word]
        while display_word_validity == 1:
            if len(display_word_list_validity) == 1:
                display_word_validity = 0
            else:
                display_word_validity = 1
                display_word = input('Invalid input: Retry ')
                display_word_list_validity = [a for a in display_word_list if a in display_word]
        user_options = [validWordOptions(input('Top left label: '))]
        user_options.append(validWordOptions(input('Middle left label: ')))
        user_options.append(validWordOptions(input('Bottom left label: ')))
        user_options.append(validWordOptions(input('Top right label: ')))
        user_options.append(validWordOptions(input('Middle right label: ')))
        user_options.append(validWordOptions(input('Bottom right label: ')))
        user_options_list = ['ready','first','no','blank','nothing','yes','what','uhhh','left','right','middle','okay','wait','press','you','you are','your',"you're",'ur','u','uh huh','uh uh','what?','done','next','hold','sure','like']
        user_options_check_list = [a for a in user_options_list if a in user_options]
        user_options_list_validity = 1
        while user_options_list_validity == 1:
            if len(user_options_check_list) == 6:
                user_options_list_validity = 0
            else:
                user_options_list_validity = 1
                print('Invalid input: Retry')
                user_options = [validWordOptions(input('Top left label: '))]
                user_options.append(validWordOptions(input('Middle left label: ')))
                user_options.append(validWordOptions(input('Bottom left label: ')))
                user_options.append(validWordOptions(input('Top right label: ')))
                user_options.append(validWordOptions(input('Middle right label: ')))
                user_options.append(validWordOptions(input('Bottom right label: ')))
                user_options_check_list = [a for a in user_options_list if a in user_options]
                user_options_list_validity = 1         
        ready_user = [ready for ready in ready_list if ready in user_options]
        first_user = [first for first in first_list if first in user_options]
        no_user = [no for no in no_list if no in user_options]
        blank_user = [blank for blank in blank_list if blank in user_options]
        nothing_user = [nothing for nothing in nothing_list if nothing in user_options]
        yes_user = [yes for yes in yes_list if yes in user_options]
        what_user = [what for what in what_list if what in user_options]
        uhhh_user = [uhhh for uhhh in uhhh_list if uhhh in user_options]
        left_user = [left for left in left_list if left in user_options]
        right_user = [right for right in right_list if right in user_options]
        middle_user = [middle for middle in middle_list if middle in user_options]
        okay_user = [okay for okay in okay_list if okay in user_options]
        wait_user = [wait for wait in wait_list if wait in user_options]
        press_user = [press for press in press_list if press in user_options]
        you_user = [you for you in you_list if you in user_options]
        you_are_user = [youare for youare in you_are_list if youare in user_options]
        your_user = [your for your in your_list if your in user_options]
        youre_user = [youre for youre in youre_list if youre in user_options]
        ur_user = [ur for ur in ur_list if ur in user_options]
        u_user = [u for u in u_list if u in user_options]
        uh_huh_user = [uhhuh for uhhuh in uh_huh_list if uhhuh in user_options]
        uh_uh_user = [uhuh for uhuh in uh_uh_list if uhuh in user_options]
        what_q_mark_user = [wqm for wqm in what_q_mark_list if wqm in user_options]
        done_user = [done for done in done_list if done in user_options]
        next_user = [nxt for nxt in next_list if nxt in user_options]
        hold_user = [hold for hold in hold_list if hold in user_options]
        sure_user = [sure for sure in sure_list if sure in user_options]
        like_user = [like for like in like_list if like in user_options]
        if display_word == 'ur':
            pick = user_options[0]
            if pick == 'ready':
                print('Press: ')
                print(ready_user[0])
            elif pick == 'first':
                print('Press: ')
                print(first_user[0])
            elif pick == 'no':
                print('Press: ')
                print(no_user[0])
            elif pick == 'blank':
                print('Press: ')
                print(blank_user[0])
            elif pick == 'nothing':
                print('Press: ')
                print(nothing_user[0])
            elif pick == 'yes':
                print('Press: ')
                print(yes_user[0])
            elif pick == 'what':
                print('Press: ')
                print(what_user[0])
            elif pick == 'uhhh':
                print('Press: ')
                print(uhhh_user[0])
            elif pick == 'left':
                print('Press: ')
                print(left_user[0])
            elif pick == 'right':
                print('Press: ')
                print(right_user[0])
            elif pick == 'middle':
                print('Press: ')
                print(middle_user[0])
            elif pick == 'okay':
                print('Press: ')
                print(okay_user[0])
            elif pick == 'wait':
                print('Press: ')
                print(wait_user[0])
            elif pick == 'press':
                print('Press: ')
                print(press_user[0])
            elif pick == 'you':
                print('Press: ')
                print(you_user[0])
            elif pick == 'you are':
                print('Press: ')
                print(you_are_user[0])
            elif pick == 'your':
                print('Press: ')
                print(your_user[0])
            elif pick == "you're":
                print('Press: ')
                print(youre_user[0])
            elif pick == 'ur':
                print('Press: ')
                print(ur_user[0])
            elif pick == 'u':
                print('Press: ')
                print(u_user[0])
            elif pick == 'uh huh':
                print('Press: ')
                print(uh_huh_user[0])
            elif pick == 'uh uh':
                print('Press: ')
                print(uh_uh_user[0])
            elif pick == 'what?':
                print('Press: ')
                print(what_q_mark_user[0])
            elif pick == 'done':
                print('Press: ')
                print(done_user[0])
            elif pick == 'next':
                print('Press: ')
                print(next_user[0])
            elif pick == 'hold':
                print('Press: ')
                print(hold_user[0])
            elif pick == 'sure':
                print('Press: ')
                print(sure_user[0])
            elif pick == 'like':
                print('Press: ')
                print(like_user[0])
        elif display_word in ['yes', 'nothing', 'led', 'they are']:
            pick = user_options[1]
            if pick == 'ready':
                print('Press: ')
                print(ready_user[0])
            elif pick == 'first':
                print('Press: ')
                print(first_user[0])
            elif pick == 'no':
                print('Press: ')
                print(no_user[0])
            elif pick == 'blank':
                print('Press: ')
                print(blank_user[0])
            elif pick == 'nothing':
                print('Press: ')
                print(nothing_user[0])
            elif pick == 'yes':
                print('Press: ')
                print(yes_user[0])
            elif pick == 'what':
                print('Press: ')
                print(what_user[0])
            elif pick == 'uhhh':
                print('Press: ')
                print(uhhh_user[0])
            elif pick == 'left':
                print('Press: ')
                print(left_user[0])
            elif pick == 'right':
                print('Press: ')
                print(right_user[0])
            elif pick == 'middle':
                print('Press: ')
                print(middle_user[0])
            elif pick == 'okay':
                print('Press: ')
                print(okay_user[0])
            elif pick == 'wait':
                print('Press: ')
                print(wait_user[0])
            elif pick == 'press':
                print('Press: ')
                print(press_user[0])
            elif pick == 'you':
                print('Press: ')
                print(you_user[0])
            elif pick == 'you are':
                print('Press: ')
                print(you_are_user[0])
            elif pick == 'your':
                print('Press: ')
                print(your_user[0])
            elif pick == "you're":
                print('Press: ')
                print(youre_user[0])
            elif pick == 'ur':
                print('Press: ')
                print(ur_user[0])
            elif pick == 'u':
                print('Press: ')
                print(u_user[0])
            elif pick == 'uh huh':
                print('Press: ')
                print(uh_huh_user[0])
            elif pick == 'uh uh':
                print('Press: ')
                print(uh_uh_user[0])
            elif pick == 'what?':
                print('Press: ')
                print(what_q_mark_user[0])
            elif pick == 'done':
                print('Press: ')
                print(done_user[0])
            elif pick == 'next':
                print('Press: ')
                print(next_user[0])
            elif pick == 'hold':
                print('Press: ')
                print(hold_user[0])
            elif pick == 'sure':
                print('Press: ')
                print(sure_user[0])
            elif pick == 'like':
                print('Press: ')
                print(like_user[0])
        elif display_word in ['', 'reed', 'leed', "they're"]:
            pick = user_options[2]
            if pick == 'ready':
                print('Press: ')
                print(ready_user[0])
            elif pick == 'first':
                print('Press: ')
                print(first_user[0])
            elif pick == 'no':
                print('Press: ')
                print(no_user[0])
            elif pick == 'blank':
                print('Press: ')
                print(blank_user[0])
            elif pick == 'nothing':
                print('Press: ')
                print(nothing_user[0])
            elif pick == 'yes':
                print('Press: ')
                print(yes_user[0])
            elif pick == 'what':
                print('Press: ')
                print(what_user[0])
            elif pick == 'uhhh':
                print('Press: ')
                print(uhhh_user[0])
            elif pick == 'left':
                print('Press: ')
                print(left_user[0])
            elif pick == 'right':
                print('Press: ')
                print(right_user[0])
            elif pick == 'middle':
                print('Press: ')
                print(middle_user[0])
            elif pick == 'okay':
                print('Press: ')
                print(okay_user[0])
            elif pick == 'wait':
                print('Press: ')
                print(wait_user[0])
            elif pick == 'press':
                print('Press: ')
                print(press_user[0])
            elif pick == 'you':
                print('Press: ')
                print(you_user[0])
            elif pick == 'you are':
                print('Press: ')
                print(you_are_user[0])
            elif pick == 'your':
                print('Press: ')
                print(your_user[0])
            elif pick == "you're":
                print('Press: ')
                print(youre_user[0])
            elif pick == 'ur':
                print('Press: ')
                print(ur_user[0])
            elif pick == 'u':
                print('Press: ')
                print(u_user[0])
            elif pick == 'uh huh':
                print('Press: ')
                print(uh_huh_user[0])
            elif pick == 'uh uh':
                print('Press: ')
                print(uh_uh_user[0])
            elif pick == 'what?':
                print('Press: ')
                print(what_q_mark_user[0])
            elif pick == 'done':
                print('Press: ')
                print(done_user[0])
            elif pick == 'next':
                print('Press: ')
                print(next_user[0])
            elif pick == 'hold':
                print('Press: ')
                print(hold_user[0])
            elif pick == 'sure':
                print('Press: ')
                print(sure_user[0])
            elif pick == 'like':
                print('Press: ')
                print(like_user[0])
        elif display_word in ['first', 'okay', 'c']:
            pick = user_options[3]
            if pick == 'ready':
                print('Press: ')
                print(ready_user[0])
            elif pick == 'first':
                print('Press: ')
                print(first_user[0])
            elif pick == 'no':
                print('Press: ')
                print(no_user[0])
            elif pick == 'blank':
                print('Press: ')
                print(blank_user[0])
            elif pick == 'nothing':
                print('Press: ')
                print(nothing_user[0])
            elif pick == 'yes':
                print('Press: ')
                print(yes_user[0])
            elif pick == 'what':
                print('Press: ')
                print(what_user[0])
            elif pick == 'uhhh':
                print('Press: ')
                print(uhhh_user[0])
            elif pick == 'left':
                print('Press: ')
                print(left_user[0])
            elif pick == 'right':
                print('Press: ')
                print(right_user[0])
            elif pick == 'middle':
                print('Press: ')
                print(middle_user[0])
            elif pick == 'okay':
                print('Press: ')
                print(okay_user[0])
            elif pick == 'wait':
                print('Press: ')
                print(wait_user[0])
            elif pick == 'press':
                print('Press: ')
                print(press_user[0])
            elif pick == 'you':
                print('Press: ')
                print(you_user[0])
            elif pick == 'you are':
                print('Press: ')
                print(you_are_user[0])
            elif pick == 'your':
                print('Press: ')
                print(your_user[0])
            elif pick == "you're":
                print('Press: ')
                print(youre_user[0])
            elif pick == 'ur':
                print('Press: ')
                print(ur_user[0])
            elif pick == 'u':
                print('Press: ')
                print(u_user[0])
            elif pick == 'uh huh':
                print('Press: ')
                print(uh_huh_user[0])
            elif pick == 'uh uh':
                print('Press: ')
                print(uh_uh_user[0])
            elif pick == 'what?':
                print('Press: ')
                print(what_q_mark_user[0])
            elif pick == 'done':
                print('Press: ')
                print(done_user[0])
            elif pick == 'next':
                print('Press: ')
                print(next_user[0])
            elif pick == 'hold':
                print('Press: ')
                print(hold_user[0])
            elif pick == 'sure':
                print('Press: ')
                print(sure_user[0])
            elif pick == 'like':
                print('Press: ')
                print(like_user[0])
        elif display_word in ['read', 'blank', 'you', 'red', 'your', "you're", 'their']:
            pick = user_options[4]
            if pick == 'ready':
                print('Press: ')
                print(ready_user[0])
            elif pick == 'first':
                print('Press: ')
                print(first_user[0])
            elif pick == 'no':
                print('Press: ')
                print(no_user[0])
            elif pick == 'blank':
                print('Press: ')
                print(blank_user[0])
            elif pick == 'nothing':
                print('Press: ')
                print(nothing_user[0])
            elif pick == 'yes':
                print('Press: ')
                print(yes_user[0])
            elif pick == 'what':
                print('Press: ')
                print(what_user[0])
            elif pick == 'uhhh':
                print('Press: ')
                print(uhhh_user[0])
            elif pick == 'left':
                print('Press: ')
                print(left_user[0])
            elif pick == 'right':
                print('Press: ')
                print(right_user[0])
            elif pick == 'middle':
                print('Press: ')
                print(middle_user[0])
            elif pick == 'okay':
                print('Press: ')
                print(okay_user[0])
            elif pick == 'wait':
                print('Press: ')
                print(wait_user[0])
            elif pick == 'press':
                print('Press: ')
                print(press_user[0])
            elif pick == 'you':
                print('Press: ')
                print(you_user[0])
            elif pick == 'you are':
                print('Press: ')
                print(you_are_user[0])
            elif pick == 'your':
                print('Press: ')
                print(your_user[0])
            elif pick == "you're":
                print('Press: ')
                print(youre_user[0])
            elif pick == 'ur':
                print('Press: ')
                print(ur_user[0])
            elif pick == 'u':
                print('Press: ')
                print(u_user[0])
            elif pick == 'uh huh':
                print('Press: ')
                print(uh_huh_user[0])
            elif pick == 'uh uh':
                print('Press: ')
                print(uh_uh_user[0])
            elif pick == 'what?':
                print('Press: ')
                print(what_q_mark_user[0])
            elif pick == 'done':
                print('Press: ')
                print(done_user[0])
            elif pick == 'next':
                print('Press: ')
                print(next_user[0])
            elif pick == 'hold':
                print('Press: ')
                print(hold_user[0])
            elif pick == 'sure':
                print('Press: ')
                print(sure_user[0])
            elif pick == 'like':
                print('Press: ')
                print(like_user[0])
        elif display_word in ['display', 'says', 'lead', 'no', 'hold on', 'you are', 'there', 'see', 'cee']:
            pick = user_options[5]
            if pick == 'ready':
                print('Press: ')
                print(ready_user[0])
            elif pick == 'first':
                print('Press: ')
                print(first_user[0])
            elif pick == 'no':
                print('Press: ')
                print(no_user[0])
            elif pick == 'blank':
                print('Press: ')
                print(blank_user[0])
            elif pick == 'nothing':
                print('Press: ')
                print(nothing_user[0])
            elif pick == 'yes':
                print('Press: ')
                print(yes_user[0])
            elif pick == 'what':
                print('Press: ')
                print(what_user[0])
            elif pick == 'uhhh':
                print('Press: ')
                print(uhhh_user[0])
            elif pick == 'left':
                print('Press: ')
                print(left_user[0])
            elif pick == 'right':
                print('Press: ')
                print(right_user[0])
            elif pick == 'middle':
                print('Press: ')
                print(middle_user[0])
            elif pick == 'okay':
                print('Press: ')
                print(okay_user[0])
            elif pick == 'wait':
                print('Press: ')
                print(wait_user[0])
            elif pick == 'press':
                print('Press: ')
                print(press_user[0])
            elif pick == 'you':
                print('Press: ')
                print(you_user[0])
            elif pick == 'you are':
                print('Press: ')
                print(you_are_user[0])
            elif pick == 'your':
                print('Press: ')
                print(your_user[0])
            elif pick == "you're":
                print('Press: ')
                print(youre_user[0])
            elif pick == 'ur':
                print('Press: ')
                print(ur_user[0])
            elif pick == 'u':
                print('Press: ')
                print(u_user[0])
            elif pick == 'uh huh':
                print('Press: ')
                print(uh_huh_user[0])
            elif pick == 'uh uh':
                print('Press: ')
                print(uh_uh_user[0])
            elif pick == 'what?':
                print('Press: ')
                print(what_q_mark_user[0])
            elif pick == 'done':
                print('Press: ')
                print(done_user[0])
            elif pick == 'next':
                print('Press: ')
                print(next_user[0])
            elif pick == 'hold':
                print('Press: ')
                print(hold_user[0])
            elif pick == 'sure':
                print('Press: ')
                print(sure_user[0])
            elif pick == 'like':
                print('Press: ')
                print(like_user[0])
    elif module == '6':
        def validMemoryDisplay(x):
            memory_display_validity = 1
            memory_display_list = ['1','2','3','4']
            memory_display_user_list = [a for a in memory_display_list if a in x]
            while memory_display_validity == 1:
                if len(memory_display_user_list) == 1:
                    memory_display_validity = 0
                else:
                    x = input('Invalid input: Retry ')
                    memory_display_user_list = [a for a in memory_display_list if a in x]
            return(x)
        def validMemoryOptions(x):
            memory_options_validity = 1
            memory_options_list = ['1','2','3','4']
            memory_options_user_list = [a for a in memory_options_list if a in x]
            while memory_options_validity == 1:
                if len(memory_options_user_list) == 4:
                    memory_options_validity = 0
                else:
                    x = (input('Invalid input: Retry ').split())
                    memory_options_user_list = [a for a in memory_options_list if a in x]
            return(x)
        labels = []
        positions = []
        s1_display = validMemoryDisplay(input('What number is on the display? '))
        s1_options = validMemoryOptions((input('What are the four number options? (e.g. 3 2 4 1) ').split()))
        if s1_display in ['1', '2']:
            labels.append(s1_options[1])
            positions.append('1')
            print('Press: ')
            print(labels[0])
        elif s1_display == '3':
            labels.append(s1_options[2])
            positions.append('2')
            print('Press: ')
            print(labels[0])
        elif s1_display == '4':
            labels.append(s1_options[3])
            positions.append('3')
            print('Press: ')
            print(labels[0])
        s2_display = validMemoryDisplay(input('What number is on the display? '))
        s2_options = validMemoryOptions((input('What are the four number options? ').split()))
        if s2_display == '1':
            labels.append('4')
            positions.append(str(s2_options.index('4')))
            print('Press: ')
            print(labels[1])
        elif s2_display in ['2', '4']:
            labels.append(s2_options[int(positions[0])])
            positions.append(positions[0])
            print('Press: ')
            print(labels[1])
        elif s2_display == '3':
            labels.append(s2_options[0])
            positions.append('0')
            print('Press: ')
            print(labels[1])
        s3_display = validMemoryDisplay(input('Display: '))
        s3_options = validMemoryOptions((input('Options: ').split()))
        if s3_display == '1':
            labels.append(labels[1])
            positions.append(str(s3_options.index(labels[1])))
            print('Press: ')
            print(labels[2])
        elif s3_display == '2':
            labels.append(labels[0])
            positions.append(str(s3_options.index(labels[0])))
            print('Press: ')
            print(labels[2])
        elif s3_display == '3':
            labels.append(s3_options[2])
            positions.append('2')
            print('Press: ')
            print(labels[2])
        elif s3_display == '4':
            labels.append('4')
            positions.append(str(s3_options.index('4')))
            print('Press: ')
            print(labels[2])
        s4_display = validMemoryDisplay(input('Display: '))
        s4_options = validMemoryOptions((input('Options: ').split()))
        if s4_display == '1':
            labels.append(s4_options[int(positions[0])])
            positions.append(positions[0])
            print('Press: ')
            print(labels[3])
        elif s4_display == '2':
            labels.append(s4_options[0])
            positions.append('0')
            print('Press: ')
            print(labels[3])
        elif s4_display in ['3', '4']:
            labels.append(s4_options[int(positions[1])])
            positions.append(positions[1])
            print('Press: ')
            print(labels[3])
        s5_display = validMemoryDisplay(input('Display: '))
        print('Press: ')
        if s5_display == '1':
            print(labels[0])
        elif s5_display == '2':
            print(labels[1])
        elif s5_display == '3':
            print(labels[3])
        elif s5_display == '4':
            print(labels[2])
    elif module == '7':
        possibilities = ['shell', 'halls', 'slick', 'trick', 'boxes', 'leaks', 'strobe', 'bistro', 'flick', 'bombs', 'break', 'brick', 'steak', 'sting', 'vector', 'beats']
        letters = []
        while len(possibilities) > 1:
            mc_user = input('Input a letter in morse code (e.g. .-..) ')
            if mc_user == '.-':
                letters.append('a')
            elif mc_user == '-...':
                letters.append('b')
            elif mc_user == '-.-.':
                letters.append('c')
            elif mc_user == '.':
                letters.append('e')
            elif mc_user == '..-.':
                letters.append('f')
            elif mc_user == '--.':
                letters.append('g')
            elif mc_user == '....':
                letters.append('h')
            elif mc_user == '..':
                letters.append('i')
            elif mc_user == '-.-':
                letters.append('k')
            elif mc_user == '.-..':
                letters.append('l')
            elif mc_user == '--':
                letters.append('m')
            elif mc_user == '-.':
                letters.append('n')
            elif mc_user == '---':
                letters.append('o')
            elif mc_user == '.-.':
                letters.append('r')
            elif mc_user == '...':
                letters.append('s')
            elif mc_user == '-':
                letters.append('t')
            elif mc_user == '...-':
                letters.append('v')
            elif mc_user == '-..-':
                letters.append('x')
            else:
                print('You may have misinterpreted that letter')
                continue
            if len(letters) > 5:
                print('I cannot seem to find the word you are looking for')
                print('You may have repeated a letter by mistake')
                possibilities = ['shell', 'halls', 'slick', 'trick', 'boxes', 'leaks', 'strobe', 'bistro', 'flick', 'bombs', 'break', 'brick', 'steak', 'sting', 'vector', 'beats']
                letters = []
                continue
            possibilities = [p for p in possibilities if letters[len(letters) - 1] in p]
        print('Frequency: ')
        if possibilities[0] == 'shell':
            print('3.505 MHz')
        elif possibilities[0] == 'halls':
            print('3.515 MHz')
        elif possibilities[0] == 'slick':
            print('3.522 MHz')
        elif possibilities[0] == 'trick':
            print('3.532 MHz')
        elif possibilities[0] == 'boxes':
            print('3.535 MHz')
        elif possibilities[0] == 'leaks':
            print('3.542 MHz')
        elif possibilities[0] == 'strobe':
            print('3.545 MHz')
        elif possibilities[0] == 'bistro':
            print('3.552 MHz')
        elif possibilities[0] == 'flick':
            print('3.555 MHz')
        elif possibilities[0] == 'bombs':
            print('3.565 MHz')
        elif possibilities[0] == 'break':
            print('3.572 MHz')
        elif possibilities[0] == 'brick':
            print('3.575 MHz')
        elif possibilities[0] == 'steak':
            print('3.582 MHz')
        elif possibilities[0] == 'sting':
            print('3.592 MHz')
        elif possibilities[0] == 'vector':
            print('3.595 MHz')
        elif possibilities[0] == 'beats':
            print('3.600 MHz')
        else:
            print('Error')
            continue
    elif module == '8':
        cw_status = 'n'
        while cw_status == 'n':
            cw_conditions = ['f', 'f', 'f', 'f']
            c_wire = (input('List the features of the wire in any order (e.g. white red star light) ').split())
            c_wire_list = ['white','red','blue','star','light']
            c_wire_list_validity = [a for a in c_wire if a in c_wire_list]
            c_wire_validity = 1
            while c_wire_validity == 1:
                if len(c_wire) == len(c_wire_list_validity):
                    if len(c_wire) > 0:
                        c_wire_validity = 0
                    else:
                        c_wire = (input('Invalid input: Retry ').split())
                        c_wire_list_validity = [a for a in c_wire if a in c_wire_list]
                else:
                    c_wire = (input('Invalid input: Retry ').split())
                    c_wire_list_validity = [a for a in c_wire if a in c_wire_list]
            if 'red' in c_wire:
                cw_conditions[0] = 't'
            if 'blue' in c_wire:
                cw_conditions[1] = 't'
            if 'star' in c_wire:
                cw_conditions[2] = 't'
            if 'light' in c_wire:
                cw_conditions[3] = 't'
            if cw_conditions == ['f', 'f', 'f', 'f'] or cw_conditions == ['f', 'f', 't', 'f'] or cw_conditions == ['t', 'f', 't', 'f']:
                print('Cut')
            elif cw_conditions == ['t', 'f', 'f', 'f'] or cw_conditions == ['f', 't', 'f', 'f'] or cw_conditions == ['t', 't', 'f', 'f'] or cw_conditions == ['t', 't', 'f', 't']:
                if serial_number[(serial_number_count) - 1] in ['0', '2', '4', '6', '8']:
                    print('Cut')
                else:
                    print('Next')
            elif cw_conditions == ['t', 't', 't', 'f'] or cw_conditions == ['f', 't', 'f', 't'] or cw_conditions == ['f', 't', 't', 't']:
                if parallel_port_check == 'y':
                    print('Cut')
                else:
                    print('Next')
            elif cw_conditions == ['t', 'f', 't', 't'] or cw_conditions == ['t', 'f', 'f', 't'] or cw_conditions == ['f', 'f', 't', 't']:
                if battery_count > 1:
                    print('Cut')
                else:
                    print('Next')
            else:
                print('Next')
            cw_status = ynvalid((input('Has the module finished? (Y/N) ').lower()))
    elif module == '9':
        ws_status = 'n'
        red_count = 0
        blue_count = 0
        black_count = 0
        while ws_status == 'n':
            wire_sequence_input = (input('Input wire colour and connecting letter (e.g. red b) ').split())
            wire_sequence_input_validity = 1
            while wire_sequence_input_validity == 1:
                if len(wire_sequence_input) == 2 and wire_sequence_input[0] in ['red','black','blue'] and wire_sequence_input[1] in ['a','b','c']:
                    wire_sequence_input_validity = 0
                else:
                    wire_sequence_input = (input('Invalid input: Retry ').split())
            if wire_sequence_input[0] == 'red':
                red_count += 1
                if red_count == 1:
                    if wire_sequence_input[1] == 'c':
                        print('Cut')
                    else:
                        print('Next')
                elif red_count == 2:
                    if wire_sequence_input[1] == 'b':
                        print('Cut')
                    else:
                        print('Next')
                elif red_count == 3:
                    if wire_sequence_input[1] == 'a':
                        print('Cut')
                    else:
                        print('Next')
                elif red_count == 4:
                    if wire_sequence_input[1] == 'b':
                        print('Next')
                    else:
                        print('Cut')
                elif red_count == 5:
                    if wire_sequence_input[1] == 'b':
                        print('Cut')
                    else:
                        print('Next')
                elif red_count == 6:
                    if wire_sequence_input[1] == 'b':
                        print('Next')
                    else:
                        print('Cut')
                elif red_count == 7:
                    print('Cut')
                elif red_count == 8:
                    if wire_sequence_input[1] == 'c':
                        print('Next')
                    else:
                        print('Cut')
                elif red_count == 9:
                    if wire_sequence_input[1] == 'b':
                        print('Cut')
                    else:
                        print('Next')
                else:
                    print('Error')
            if wire_sequence_input[0] == 'blue':
                blue_count += 1
                if blue_count == 1:
                    if wire_sequence_input[1] == 'b':
                        print('Cut')
                    else:
                        print('Next')
                elif blue_count == 2:
                    if wire_sequence_input[1] == 'b':
                        print('Next')
                    else:
                        print('Cut')
                elif blue_count == 3:
                    if wire_sequence_input[1] == 'b':
                        print('Cut')
                    else:
                        print('Next')
                elif blue_count == 4:
                    if wire_sequence_input[1] == 'a':
                        print('Cut')
                    else:
                        print('Next')
                elif blue_count == 5:
                    if wire_sequence_input[1] == 'b':
                        print('Cut')
                    else:
                        print('Next')
                elif blue_count == 6:
                    if wire_sequence_input[1] == 'a':
                        print('Next')
                    else:
                        print('Cut')
                elif blue_count == 7:
                    if wire_sequence_input[1] == 'c':
                        print('Cut')
                    else:
                        print('Next')
                elif blue_count == 8:
                    if wire_sequence_input[1] == 'b':
                        print('Next')
                    else:
                        print('Cut')
                elif blue_count == 9:
                    if wire_sequence_input[1] == 'a':
                        print('Cut')
                    else:
                        print('Next')
                else:
                    print('Error')
            if wire_sequence_input[0] == 'black':
                black_count += 1
                if black_count == 1:
                    print('Cut')
                elif black_count == 2:
                    if wire_sequence_input[1] == 'b':
                        print('Next')
                    else:
                        print('Cut')
                elif black_count == 3:
                    if wire_sequence_input[1] == 'b':
                        print('Cut')
                    else:
                        print('Next')
                elif black_count == 4:
                    if wire_sequence_input[1] == 'b':
                        print('Next')
                    else:
                        print('Cut')
                elif black_count == 5:
                    if wire_sequence_input[1] == 'b':
                        print('Cut')
                    else:
                        print('Next')
                elif black_count == 6:
                    if wire_sequence_input[1] == 'a':
                        print('Next')
                    else:
                        print('Cut')
                elif black_count == 7:
                    if wire_sequence_input[1] == 'c':
                        print('Next')
                    else:
                        print('Cut')
                elif black_count == 8:
                    if wire_sequence_input[1] == 'c':
                        print('Cut')
                    else:
                        print('Next')
                elif black_count == 9:
                    if wire_sequence_input[1] == 'c':
                        print('Cut')
                    else:
                        print('Next')
                else:
                    print('Error')
            ws_status = ynvalid((input('Has the module finished? (Y/N) ').lower()))
    elif module == '10':
        maze_pick_validity = 1
        maze_pick = input('Give the coordinates of any one of the green circles in format x, y (where the bottom left point would be 0, 0) ')
        while maze_pick_validity == 1:
            if maze_pick == '1, 5' or maze_pick == '6, 4' or maze_pick == '2, 3' or maze_pick == '5, 5' or maze_pick == '4, 3' or maze_pick == '6, 3' or maze_pick == '1, 6' or maze_pick == '1, 3' or maze_pick == '4, 1' or maze_pick == '5, 4' or maze_pick == '3, 2' or maze_pick == '5, 6' or maze_pick == '2, 1' or maze_pick == '2, 6' or maze_pick == '3, 3' or maze_pick == '4, 6' or maze_pick == '1, 2' or maze_pick == '3, 2':
                maze_pick_validity = 0
            else:
                maze_pick = input('Invalid input: Retry ')
        if maze_pick in ['1, 5', '6, 4']:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        elif maze_pick in ['2, 3', '5, 5']:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        elif maze_pick in ['4, 3', '6, 3']:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        elif maze_pick in ['1, 6', '1, 3']:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        elif maze_pick in ['4, 1', '5, 4']:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        elif maze_pick in ['3, 2', '5, 6']:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                   [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        elif maze_pick in ['2, 1', '2, 6']:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        elif maze_pick in ['3, 3', '4, 6']:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        else:
            maze = [
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        def validMaze(x):
            maze_position_validity = 1
            while maze_position_validity == 1:
                try:
                    x = int(x)
                    if 0 < x < 7:
                        maze_position_validity = 0
                    else:
                        x = input('Invalid input: Retry ')
                except ValueError:
                    x = input('Invalid input: Retry ')
            return(x)
        white_light_r = validMaze(input('White light row number: '))
        white_light_c = validMaze(input('White light column number: '))
        not_start = ((int(white_light_r)+1)*2)-3,((int(white_light_c)+1)*2)-3
        red_triangle_r = validMaze(input('Red triangle row number: '))
        red_triangle_c = validMaze(input('Red triangle column number: '))
        not_end = ((int(red_triangle_r)+1)*2)-3,((int(red_triangle_c)+1)*2)-3
        start = not_end
        end = not_start
        a = maze
        def make_step(k):
            for i in range(len(m)):
                for j in range(len(m[i])):
                    if m[i][j] == k:
                        if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
                            m[i-1][j] = k + 1
                        if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
                            m[i][j-1] = k + 1
                        if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
                            m[i+1][j] = k + 1
                        if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
                            m[i][j+1] = k + 1
        m = []
        for i in range(len(a)):
            m.append([])
            for j in range(len(a[i])):
                m[-1].append(0)
        i,j = start
        m[i][j] = 1
        k = 0
        while m[end[0]][end[1]] == 0:
            k += 1
            make_step(k)
        i, j = end
        k = m[i][j]
        the_path = [(i,j)]
        while k > 1:
            if i > 0 and m[i - 1][j] == k-1:
                i, j = i-1, j
                the_path.append((i, j))
                k-=1
            elif j > 0 and m[i][j - 1] == k-1:
                i, j = i, j-1
                the_path.append((i, j))
                k-=1
            elif i < len(m) - 1 and m[i + 1][j] == k-1:
                i, j = i+1, j
                the_path.append((i, j))
                k-=1
            elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
                i, j = i, j+1
                the_path.append((i, j))
                k -= 1
        maze_counter = -1
        directions = []
        while maze_counter + 2 < len(the_path):
            maze_counter += 1           
            if (the_path[maze_counter])[0] < (the_path[maze_counter + 1])[0]:
                directions.append('down')
            elif (the_path[maze_counter])[0] > (the_path[maze_counter + 1])[0]:
                directions.append('up')
            elif (the_path[maze_counter])[1]< (the_path[maze_counter + 1])[1]:
                directions.append('right')
            elif (the_path[maze_counter])[1] > (the_path[(maze_counter + 1)])[1]:
                directions.append('left')
        dir_counter = -1
        dir_answer = []
        while dir_counter + 1 < len(directions):
            dir_counter += 2
            dir_answer.append(directions[dir_counter]) 
        print(dir_answer)            
    elif module == '11':
        password_list = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'which', 'world', 'would', 'write']
        answer = password_list
        def validPassword(x):
            alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            alphabet_valid = [letter for letter in x if letter in alphabet]
            letters_validity = 1
            while letters_validity == 1:
                if len(alphabet_valid) == 6:
                    letters_validity = 0
                else:
                    x = (input('Invalid input: Retry ').split())
                    alphabet_valid = [letter for letter in x if letter in alphabet]
            return(x)
        while len(answer) != 1:
            user_pos_1 = validPassword((input('Enter each possible letter available in the first slot (e.g. a p r x c t) ').split()))
            px = 1
            possibilities_1 = [i for i in password_list if i.startswith(user_pos_1[px - 1])]
            while px < len(user_pos_1):
                px += 1
                possibilities_1.extend([i for i in password_list if i.startswith(user_pos_1[px - 1])])
            answer = possibilities_1
            if len(answer) > 1:
                user_pos_2 = validPassword((input('Enter each possible letter available in the second slot (e.g. a p r x c t) ').split()))
                px = 0
                possibilities_2 = []
                t = -1
                while px < len(user_pos_2):
                    px += 1
                    while t + 1 < len(user_pos_1):
                        t += 1
                        possibilities_2.extend([i for i in possibilities_1 if i.startswith(user_pos_1[t]+user_pos_2[px - 1])])
                    t = -1
                answer = possibilities_2
            if len(answer) > 1:
                user_pos_3 = validPassword((input('Enter each possible letter available in the third slot (e.g. a p r x c t) ').split()))
                px = 0
                possibilities_3 = []
                t = -1
                u = -1
                while px < len(user_pos_3):
                    px += 1
                    while u + 1 < len(user_pos_2):
                        u += 1
                        while t + 1 < len(user_pos_1):
                            t += 1
                            possibilities_3.extend([i for i in possibilities_2 if i.startswith(user_pos_1[t]+user_pos_2[u]+user_pos_3[px - 1])])
                        t = -1
                    u = -1
                answer = possibilities_3
            if len(answer) > 1:
                user_pos_4 = validPassword((input('Enter each possible letter available in the fourth slot (e.g. a p r x c t) ').split()))
                px = 0
                possibilities_4 = []
                t = -1
                u = -1
                v = -1
                while px < len(user_pos_4):
                    px += 1
                    while v + 1 < len(user_pos_3):
                        v += 1
                        while u + 1 < len(user_pos_2):
                            u += 1
                            while t + 1 < len(user_pos_1):
                                t += 1
                                possibilities_4.extend([i for i in possibilities_3 if i.startswith(user_pos_1[t]+user_pos_2[u]+user_pos_3[v]+user_pos_4[px - 1])])
                            t = -1
                        u = -1
                    v = -1
                answer = possibilities_4
            if len(answer) > 1:
                user_pos_5 = validPassword((input('Enter each possible letter available in the fifth slot (e.g. a p r x c t) ').split()))
                px = 0
                possibilities_5 = []
                t = -1
                u = -1
                v = -1
                w = -1
                while px < len(user_pos_5):
                    px += 1
                    while w + 1 < len(user_pos_4):
                        w += 1
                        while v + 1 < len(user_pos_3):
                            v += 1
                            while u + 1 < len(user_pos_2):
                                u += 1
                                while t + 1 < len(user_pos_1):
                                    t += 1
                                    possibilities_5.extend([i for i in possibilities_4 if i.startswith(user_pos_1[t]+user_pos_2[u]+user_pos_3[v]+user_pos_4[w]+user_pos_5[px - 1])])
                                t = -1
                            u = -1
                        v = -1
                    w = -1
                answer = possibilities_5
            if len(answer) != 1:
                print('Error: Retry')
            if len(answer) == 1:
                print('The word is: ')
                print(answer)          
    elif module == '12':
        knobs_validity = 1
        while knobs_validity == 1:
            knobs_1 = (input('Which lights are turned on in the top row (x=on o=off)? (e.g. xooxox) ').lower())
            knobs_validity = 0
            second_valid = 0
            if knobs_1 == 'ooxoxx':
                print('Position: Up')
            elif knobs_1 in ['xoxxxx', 'xoxxoo']:
                print('Position: Right')
            elif knobs_1 == 'oxxoox':
                print('Position: Down')
            elif knobs_1 == 'xoxoxo':
                knobs_2 = (input('How many lights are turned on in the bottom row? '))
                if knobs_2 == '4':
                    print('Position: Up')
                elif knobs_2 == '2':
                    print('Position: Down')
                else:
                    print('Error: Retry')
                    knobs_validity = 1
            elif knobs_1 == 'ooooxo':
                print('Position: Left')
            else:
                print('Error: Retry')
                knobs_validity = 1
    elif module == 'x':
        x = 1
    elif module == 'n':
        def split(serial_number):
            return [char for char in serial_number]
        serial_number = (split((input('Serial number: ').lower())))
        serial_number_element_check = [x for x in serial_number if x in serial_number_elements]
        if len(serial_number) != len(serial_number_element_check):
            serial_number_validity = 1
        elif len(serial_number) != 6:
            serial_number_validity = 1
        elif serial_number[len(serial_number) - 1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            serial_number_validity = 1
        else:
            serial_number_validity = 0
        while serial_number_validity == 1:
            print('That serial number was incorrect: Retry')
            serial_number = (split((input('Serial number: ').lower())))
            serial_number_element_check = [x for x in serial_number if x in serial_number_elements]
            if len(serial_number) != len(serial_number_element_check):
                serial_number_validity = 1
            elif len(serial_number) != 6:
                serial_number_validity = 1
            elif serial_number[len(serial_number) - 1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                serial_number_validity = 1
            else:
                serial_number_validity = 0
        serial_number_count = len(serial_number)
        battery_count_validity = 1
        battery_count = input('Number of batteries: ')
        while battery_count_validity == 1:
            try:
                battery_count = int(battery_count)
                if battery_count > -1:
                    battery_count_validity = 0
                else:
                    battery_count = input('Invalid input: Retry ')
            except ValueError:
                battery_count_validity = 1
                print('Invalid number of batteries: Retry ')
                battery_count = input('Number of batteries: ')
        lit_indicator_CAR = ynvalid((input("Lit indicator 'CAR'? (Y/N) ").lower()))
        lit_indicator_FRK = ynvalid((input("Lit indicator 'FRK'? (Y/N) ").lower()))
        parallel_port_check = ynvalid((input('Is there a parallel port? (Y/N) ').lower()))
    else:
        print('Error: Invalid input')
