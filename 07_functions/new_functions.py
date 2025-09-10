#Function that creates a message
def create_message(prefix, *args):
    s = " "
    print(s.join(args))

#call a function
create_message("status", "Temp", 25, "Degree")