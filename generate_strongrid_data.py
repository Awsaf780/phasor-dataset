import pandas as pd
import os

df = pd.read_csv('MergedDataset/full_dataset.csv')
print(df.head())

# Available Columns in DataFrame

# 'Timestamp'

# 'Austin_V1LPM_Magnitude'
# 'Austin_V1LPM_Angle'

# 'HARRIS_V1LPM_Magnitude'
# 'HARRIS_V1LPM_Angle'

# 'McDonald 1P_V1LPM_Magnitude'
# 'McDonald 1P_V1LPM_Angle'

# 'UT 3 phase_VALPM_Magnitude'
# 'UT 3 phase_VALPM_Angle'

# 'UT Pan Am_V1LPM_Magnitude'
# 'UT Pan Am_V1LPM_Angle'

# 'WACO_V1YPM_Magnitude'
# 'WACO_V1YPM_Angle'

# 'Z_UT_3378_AO[079]_Value'
# 'Z_UT_3378_AO[085]_Value'
# 'Z_UT_3378_AO[087]_Value'
# 'Z_UT_3378_AO[090]_Value'
# 'Z_UT_3378_AO[091]_Value'
# 'Z_UT_3378_AO[092]_Value'

# CHOOSE ANY MAGNITUDE-ANGLE PAIR TO FORMAT DATA
magnitude  = 'Austin_V1LPM_Magnitude'
angle = 'Austin_V1LPM_Angle'

data = df[[magnitude, angle]]

folder = 'StrongridDataset'

if not os.path.exists(folder):
    os.makedirs(folder)

# Replace desired filename
filename = 'strongrid_sample.phcsv'

data.to_csv('{}/{}'.format(folder, filename), header=False, sep=';', index=False, line_terminator=',')