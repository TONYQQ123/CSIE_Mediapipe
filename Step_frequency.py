from Steps import Caculate_steps
import cv2

def Calculate_step_frequency(candidate,current_time):
    Steps = Caculate_steps(candidate)
    Step_frequency = Steps / current_time * 60
    with open('Step_frequency.txt','w') as file:
        file.write(f"{Steps}\n")
        file.write(f"{Step_frequency}\n")
    print('Step_frequency: ' + str(Step_frequency) + '\n')
    return Step_frequency
