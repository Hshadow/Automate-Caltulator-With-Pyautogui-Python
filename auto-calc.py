import pyautogui as pg

pg.FAILSAFE = False

### Only Works On Windows
### Start Calculator Before Execute
### Automatically Type When Calculator Is On Top

all_titles = [*pg.getAllTitles()] # Get All Titles of Visible Windows
all_windows = [*pg.getAllWindows()] # Get All Visible Windows
delay = 0.2 # Time Delay Between Key Press
index = 0

try:
    calculator = all_windows[all_titles.index("Calculator")]
    
    solve = input("Enter Equation To Solve With Calculator.\nFor Example: 25+50\n"+str(40*"=")+"\n") # Equation To Solve With Calculator
    solve = solve.strip().strip("=")
    solve = solve+"="
    
    while calculator:
        active = calculator.isActive
        if index==len(solve):
            break
        
        if active:
            key = solve[index]
            pg.hotkey(key, interval=0.2)
            index+=1
            
except Exception as ex:
    print("Please Start Calculator !")
