import CoinClass as c
#coinclass is the name of the python file 



# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter
        #will get error if you call coin instead of my_coin
        
       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           my_coin.__sidup = 'Heads'
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
