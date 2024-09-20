def judge_action(arr, step_total_fre, forearm_pos, arr_time, step_total_fre_time, forearm_pos_time, fps, flag):
    txt = ""
    if len(arr) > 0:
        shear_stress = arr[len(arr)-1]
        if shear_stress < 80:
            arr_time = fps * 2
            txt += "Low Contact Angle\n"
        elif arr_time > 0:
            arr_time -= 1
            txt += "Low Contact Angle\n"

    if step_total_fre < 185:
        step_total_fre_time = fps * 2
        txt += "Pace Faster\n"
    elif step_total_fre_time > 0:
        txt += "Pace Faster\n"
        step_total_fre_time -= 1

    if len(forearm_pos) > 0:
        real_amplitude = forearm_pos[len(forearm_pos)-1]
        if real_amplitude > 64:
            forearm_pos_time = fps * 2
            txt += "High Amplitude\n"
        elif forearm_pos_time > 0:
            txt += "High Amplitude\n"
            forearm_pos_time -= 1

    if flag == 1:
        txt += "Low Waist Angle\n"

    if txt == "":
        txt = "Good job\n"
    #if arrr[len(arrr)-1] < 80:
    #    txt += "Low stoop angle\n"

    return txt