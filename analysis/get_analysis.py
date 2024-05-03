import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

MAHA = 'maha'
BASELINE = 'baseline'
# reading csv file 
def get_aggr_result_csv_string(result_file_type):
    df = pd.read_csv(result_file_type+"results.csv")
    # print(df.head())
    csv_rows = []
    csv_rows.append(",".join(["scenario", "scenario_type_intensity", "route_change", "route_change_avg", "collisions_vehicle", "collisions_layout"]))
    scenarios = ['haze', 'shade', 'rain']
    for scenario in scenarios:
        for scenario_intensity in range(0, 10):
            route_change = df.loc[(df['scenario_type'] == scenario) & (df['scenario_type_intensity'] == scenario_intensity) & (pd.notna(df['outside_route_lanes']))]['outside_route_lanes'].describe().loc['count']
            #print(df.loc[(df['scenario_type'] == scenario) & (df['scenario_type_intensity'] == scenario_intensity) & (pd.notna(df['outside_route_lanes']))]['outside_route_lanes'].describe())
            collisions_vehicle = df.loc[(df['scenario_type'] == scenario) & (df['scenario_type_intensity'] == scenario_intensity) & (pd.notna(df['collisions_vehicle']))]['collisions_vehicle'].describe().loc['count']
            #print(df.loc[(df['scenario_type'] == scenario) & (df['scenario_type_intensity'] == scenario_intensity) & (pd.notna(df['collisions_vehicle']))]['collisions_vehicle'].describe())
            collisions_layout = df.loc[(df['scenario_type'] == scenario) & (df['scenario_type_intensity'] == scenario_intensity) & (pd.notna(df['collisions_layout']))]['collisions_layout'].describe().loc['count']
            #print(df.loc[(df['scenario_type'] == scenario) & (df['scenario_type_intensity'] == scenario_intensity) & (pd.notna(df['collisions_layout']))]['collisions_layout'].describe())
            route_change_avg = df.loc[(df['scenario_type'] == scenario) & (df['scenario_type_intensity'] == scenario_intensity)]['outside_route_lanes_average'].describe().loc['mean']
            #print(df.loc[(df['scenario_type'] == scenario) & (df['scenario_type_intensity'] == scenario_intensity)].describe())
            csv_rows.append(",".join([str(scenario), str(scenario_intensity), "{:.2f}".format(route_change/0.11), "{:.2f}".format(route_change_avg), "{:.2f}".format(collisions_vehicle/0.11), "{:.2f}".format(collisions_layout/0.11)]))
            # print(scenario, scenario_intensity, route_change/0.11, collisions_vehicle/0.11, collisions_layout/0.11)
        #print(df.loc[:,['scenario_num', 'scenario_type_intensity', 'collisions_vehicle', 'collisions_layout', 'outside_route_lanes']]) 
    return "\n".join(csv_rows)

result_file_type = BASELINE
with open(result_file_type + 'aggregate.csv', 'w') as result_file:
    result_file.write(get_aggr_result_csv_string(result_file_type))