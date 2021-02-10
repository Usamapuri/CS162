#Usama
# Pseudocode used from https://www.youtube.com/watch?v=W1zKu3fDQR8&ab_channel=TheCodingTrain

#from template import AbstractSimulation
import random
class rule90(AbstractSimulation):
    def __init__(self, number_of_steps):
        super().__init__(number_of_steps)
        self.iter = 0

    def initialize_sim(self):
        arr_len = random.randint(5, 10)
        print("Initializing 1d array, len{}.".format(arr_len))
        result = [True] * arr_len
        for i in range(arr_len):
            temp = random.random()
            if temp > 0.5:
                result[i] = False
        print("Array Initialized, step0:{}.".format(result))
        self.arr = result
    def run_one_step(self):
        '''Changing All Values in array simultaneously
        '''
        temp_copy = self.arr
        for i in range(len(temp_copy)):
            if i == 0:
                self.arr[0] = (False!= temp_copy[1])
            elif i ==len(temp_copy)-1:
                self.arr[-1] = (temp_copy[-2]!= False)
            else:
                self.arr[i] = (temp_copy[i-1] != temp_copy[i+1])
        self.iter +=1
    def print_sim_state(self):
        print("On Step {}, arr looks like {}.".format(self.iter, self.arr))

if __name__=="__main__":
    lets_see = rule90(5)
    lets_see.run()
