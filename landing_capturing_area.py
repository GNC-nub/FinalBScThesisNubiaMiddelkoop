'''
READ ME
    landing_area(x, y, z)
    capturing_area(x, y, z)

DESCRIPTION
    These functions determine if a single coordinate is within a capturing or a landing area

OUTPUT
    If the coordinate is within the area the output is True, otherwise it is False.

RESULTS
    In the whole dataset 3197 mosquitos are landing. (9.38 %)
    In the whole dataset 1194 mosquitos are captured. (3.5 %)
'''


from accessing_data import *

def landing_area(x, y, z, landing_width=0.03, trap_height = 0.388, trap_radius = 0.15, inlet_height = 0.083, inlet_radius = 0.055):
    distance = np.sqrt((x**2)+(y**2))
    landing = False

    if -landing_width < z < 0:
        if inlet_radius < distance < inlet_radius + landing_width:
            landing = True
    elif -(inlet_height - landing_width) < z < -landing_width:
        if inlet_radius - landing_width < distance < inlet_radius + landing_width:
            landing = True
    elif -(inlet_height + landing_width) < z < -(inlet_height - landing_width):
        if inlet_radius - landing_width < distance < trap_radius + landing_width:
            landing = True
    elif -trap_height < z < -(inlet_height + landing_width):
        if trap_radius - landing_width < distance < trap_radius + landing_width:
            landing = True
    return landing

def capturing_area(x, y, z, capturing_width = 0.03, inlet_radius = 0.055):
    distance = np.sqrt((x**2)+(y**2))
    capture = False
    if 0 < z < capturing_width:
        if distance < (inlet_radius + capturing_width):
            capture = True
    elif -capturing_width < z < 0:
        if distance < inlet_radius:
            capture = True
    return capture


def landing_trial(trial, capturing_width = 0.03, landing_width = 0.03):
    landing_count, capturing_count, total_count = 0, 0, 0
    data = accessing_trial(trial)
    for track in data:
        header, x_list, y_list, z_list, time_list = track
        x, y, z, time = x_list[-1], y_list[-1], z_list[-1], time_list[-1]
        total_count += 1
        if landing_area(x, y, z, landing_width = landing_width) == True:
            msg = f'Track {header} lands on the trap.'
            landing_count += 1
        elif capturing_area(x, y, z, capturing_width = capturing_width) == True:
            msg = f'Track {header} lands on the trap.'
            capturing_count +=1
        else:
            msg = f'Track {header} escapes.'
    extra_info = f'The amount of landing mosquitos is {landing_count} \nThe amount of captured mosquitos is {capturing_count} \nThe total amount of mosquito tracks in trial {trial} is {total_count}'
    return extra_info

def landing_subset(capturing_width = 0.03, landing_width = 0.03):
    landing_count, capturing_count, total_count = 0, 0, 0
    total_number_of_trials = 65
    for i in range(1, total_number_of_trials + 1):  # loop through all the trials
        data = accessing_trial(i)
        for track in data:
            header, x_list, y_list, z_list, time_list = track
            x, y, z, time = x_list[-1], y_list[-1], z_list[-1], time_list[-1]
            total_count += 1
            if landing_area(x, y, z, landing_width = landing_width) == True:
                landing_count += 1
            elif capturing_area(x, y, z, capturing_width = capturing_width) == True:
                capturing_count += 1
    return landing_count, capturing_count, total_count







if __name__ == "__main__":
    #print(capturing_area(0, 0.05, 0.01))
    #print(landing_area(0.05,0.05,-0.03))

    landing, capturing, total_tracks = landing_subset()
    print(f'Total tracks = {total_tracks}')
    print(f'In the whole dataset {landing} mosquitos are landing. ({round(landing/total_tracks*100, 2)} % of the tracks end in landing)')
    print(f'From this testing: In the whole dataset {capturing} mosquitos are captured. ({round(capturing/total_tracks*100, 2)} % of the tracks end in capture)')
    print(f'From the capture rate of the article: In the whole dataset 1335 mosquitos are captured. ({round(1335/total_tracks*100, 2)} % of the tracks end in capture)')

