import pandas as pd 


def get_change_in_range_for_velocityZ2(current_elevation, current_muzzle_velocity):
    def get_change_in_range_for_velocity_increase(elevation_value, target_column, change_in_muzzle_velocity):
        value = data.loc[data['elevation'] == elevation_value, target_column].values[0]
        return value * abs(change_in_muzzle_velocity)

    def get_change_in_range_for_velocity_decrease(elevation_value, target_column, change_in_muzzle_velocity):
        value = data.loc[data['elevation'] == elevation_value, target_column].values[0]
        return value * abs(change_in_muzzle_velocity)

    base_muzzle_velocity = 479  # for zone 2
    change_in_muzzle_velocity = current_muzzle_velocity - base_muzzle_velocity

    if change_in_muzzle_velocity > 0:
        target_column = 'vinc'
        change_in_range_for_muzzle_velocity = get_change_in_range_for_velocity_increase(current_elevation, target_column, change_in_muzzle_velocity)
    elif change_in_muzzle_velocity == 0:
        change_in_range_for_muzzle_velocity = 0
    else:
        target_column = 'vdec'
        change_in_range_for_muzzle_velocity = get_change_in_range_for_velocity_decrease(current_elevation, target_column, change_in_muzzle_velocity)

    return change_in_range_for_muzzle_velocity

def get_change_in_range_for_htwindZ2(current_elevation, current_htwind):
    def get_change_in_range_for_htwind_increase(elevation_value, target_column, change_in_htwind):
        value = data.loc[data['elevation'] == elevation_value, target_column].values[0]
        return value * abs(change_in_htwind)

    def get_change_in_range_for_htwind_decrease(elevation_value, target_column, change_in_htwind):
        value = data.loc[data['elevation'] == elevation_value, target_column].values[0]
        return value * abs(change_in_htwind)

    base_htwind = 0  # for zone 2
    change_in_htwind = current_htwind - base_htwind

    if change_in_htwind > 0:
        target_column = 'tw'
        change_in_range_for_htwind = get_change_in_range_for_htwind_increase(current_elevation, target_column, change_in_htwind)
    elif change_in_htwind == 0:
        change_in_range_for_htwind = 0
    else:
        target_column = 'hw'
        change_in_range_for_htwind = get_change_in_range_for_htwind_decrease(current_elevation, target_column, change_in_htwind)

    return change_in_range_for_htwind

# Load data from the original CSV
data = pd.read_csv('F:/Vasaikar/datu.csv')

# Process the data
results = []

for index, row in data.iterrows():
    Range = row['Range']
    current_elevation = row['elevation']
    current_velocity = row['Vel']
    current_htwind = row['htwind']

    change_in_range_velocity = get_change_in_range_for_velocityZ2(current_elevation, current_velocity)
    change_in_range_htwind = get_change_in_range_for_htwindZ2(current_elevation, current_htwind)
    predicted_range = data.loc[data['elevation'] == current_elevation, 'Range'].values[0] + change_in_range_htwind + change_in_range_velocity
    difference = Range - predicted_range
    results.append({
        'elevation': current_elevation,
        'velocity': current_velocity,
        'change_in_range_velocity': change_in_range_velocity,
        'htwind': current_htwind,
        'change_in_range_htwind': change_in_range_htwind,
        'predicted_range': predicted_range,
        'Range': Range,
        'difference': difference
    })

# Convert results to a DataFrame and print
results_df = pd.DataFrame(results)
results_df.to_csv('F:/Vasaikar/result2.csv', index=False)
# print(results_df)

max = results_df.iloc[:,7].max()
min = results_df.iloc[:,7].min()
print(max)
print(min)
