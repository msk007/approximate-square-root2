number=int(input("""what is your number?""))

def user_input():
    if (number == 0) then
    my_sqrt=0
    if (number < 0) then
    print ("Invalid Number")
    if (number > 0) then
    my_sqrt()


def my_sqrt():
    epsilon = 1
    x = b/2
    new_x = 0
    count = 1
    while epsilon > float(0.01):
        new_x = (x +(b/x))/2
        epsilon = (x - new_x)
        x = new_x
        print("after {} iterations, guess is {}".format(count,x))
        count +=1
    print("the square root of {} is{}.".format(user_inpt, x))

user_input()         
