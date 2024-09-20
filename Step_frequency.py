from Steps import Calculate_steps

def Calculate_step_frequency(candidate, current_time, array, steps,flags,image):
    Steps , flags = Calculate_steps(candidate, array, steps,flags,image)
    Step_frequency = Steps / current_time * 60

    #print('Step_frequency: ' + str(Step_frequency) + '\n')
    return Step_frequency , flags

