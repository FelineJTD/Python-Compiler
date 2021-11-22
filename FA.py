'''Rules for Python variables (source: https://www.w3schools.com/python/gloss_python_variable_names.asp):
    - A variable name must start with a letter or the underscore character
    - A variable name cannot start with a number
    - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    - Variable names are case-sensitive (age, Age and AGE are three different variables)
'''
def readDFA(file):
    # format file:
    # Q (states). Misal q0,q1,q2,x,f. Special format: x untuk state buangan.
    # input symbols. Misal 0,1
    # start state. Misal q0
    # final state. Misal f
    # transitions, dipisahkan enter. Misal q0,0=q1
    with open(file, "r") as f:
        data = f.read()
    data = data.split("\n")
    # states
    states = data[0].split("\n")
    # input symbols
    input_symbols = data[1].split(",")
    # start state
    start_state = data[2]
    # final state
    final_state = data[3]
    # transitions
    transitions = {}
    for i in range(4, len(data)):
        transition = data[i].split("=")
        transitions[transition[0]] = transition[1]
    return (states, input_symbols, start_state, final_state, transitions)
    
def isVarValid(var):
    # fungsi isVarValid(var) mengembalikan True bila var valid dan False bila var tidak valid
    states, input_symbols, start_state, final_state, transitions = readDFA("dfa.txt")
    # mulai
    currState = start_state
    i = 0
    # x adalah state buangan, dibuat syarat agar menghemat loop
    while (i<len(var) and currState!='x'):
        # determining input type
        if var[i] in (["0","1","2","3","4","5","6","7","8","9"]):
            i_type = "number"
        elif var[i] in (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W' 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
            i_type = "letter"
        elif var[i] == "_":
            i_type = "underscore"
        else:
            i_type = "unknown"

        # proceeding to next state
        if i_type in input_symbols:
            currState = transitions[f"{currState},{i_type}"]
        else:
            return False

        i += 1

    if currState == final_state:
        return True
    else:
        return False