"""
.......................................................................................................................................................................................................................................................................................................
............................................................................................................................................................................................................................................................................................................
...................-/............/.....................................................--::-................................................................................................................................................................................................................
...................om-..........+N-.......-NNNNNNNNNNNN-.....+NNNNNNNmds:..........:ohmMMNMMNds:.........:NNNNNNNNNNNN......................................................................................................................................................................................
...................mMh.........:NMo.......-MM----------......oMd-----:+dMy.......:hMms/-...-:odMm+.......:MM----------......................................................................................................................................................................................
................../MMMo........dMMm.......-MM................oMh........hMs.....oMm+...........:dMh......:MM................................................................................................................................................................................................
..................hMyNN:......sMhmM/......-MM................oMh........sMy....+Mm-.............-yd+.....:MM................................................................................................................................................................................................
.................-MM-+Mm-..../Mm-oMh......-MM/:::::::::......oMh.......+NN/....dM+.......................:MM::::::::::......................................................................................................................................................................................
.................sMh..yMy...-NN/.-NM:.....-MMdddddddddy......oMmyyyyyymNh:.....mM/.......:++++++++++-....:MMdddddddddy......................................................................................................................................................................................
.................NM/..-dMo..hMo...yMs.....-MM----------......oMmsshMMy+:.......hMs......./hhhhhhhdMN.....:MM----------......................................................................................................................................................................................
................+Mm....:NN:sMh....:MN-....-MM................oMh..-oNm+........:NN+.............:dMo.....:MM................................................................................................................................................................................................
................dMo.....+MmMm-.....dM+....-MM................oMh..../dMy-.......:dNy/-........:omNo......:MM................................................................................................................................................................................................
...............:MN-......yMN/......+Md....-MM++++++++++......oMh.....-sNm+.......-odNdyo+//+shmms:.......:MM++++++++++......................................................................................................................................................................................
...............+ho........do........hh-...-hhhhhhhhhhhh....../hs......./hh+.........:oydmmmdho/-.........-hhhhhhhhhhhh......................................................................................................................................................................................
..........................-.................................................................................................................................................................................................................................................................................
..........................................................................................................................................................................................................................................................................................................
.................................................................................-..........................................................................................................................................................................................................................
.................+oooooo+/:..................ho..........-ooooooooooo+...........h+..............:+osyyso/-.......:ooooooooooo+....:ooooooooooo+............................................................................................................................................................
.................dMmhhhhddmmy/..............oMN/.........:yyyyhMNyyyys..........yMN:...........:hmhso+oshmmo......+MNyyyyyyyyys....:yyyydMNyyyyo............................................................................................................................................................
.................dM+.....-:odNh:.........../MdNm-............./Mm..............+MdNd-.........-NM/.......:hd/.....+Md...................+Md.................................................................................................................................................................
.................dM+........-oNm:.........:NN:+Mh............./Mm.............:Nm-oMy........./MM-................+Md...................+Md.................................................................................................................................................................
.................dM+..........+Md........-dM+..yMs............/Mm............-mN/..hMo.........hMms/:-............+Md...................+Md.................................................................................................................................................................
.................dM+...........NM-.......yMs...-dM+.........../Mm............hMo...-mN/........./ymNmdhyo/-.......+MNyyyyyyyyy+.........+Md.................................................................................................................................................................
.................dM+...........NM-......oMd-....:NN:........../Mm...........sMh...../MN-...........-/+oydNNh/.....+Mmooooooooo/.........+Md.................................................................................................................................................................
.................dM+..........oMh....../NMdhhhhhhmMm-........./Mm..........+MMhhhhhhhNMd.................-oNM/....+Md...................+Md.................................................................................................................................................................
.................dM+........-sMm-.....-NMo++++++++yMh........./Mm.........:NNo++++++++hMy.....:/:..........hMs....+Md...................+Md.................................................................................................................................................................
.................dM+.....-/yNNs-......dMs..........dMo......../Mm........-mM+.........-mM+....+MN+........+NN:....+Md...................+Md.................................................................................................................................................................
.................dMNmmmNNMmho-.......yMh...........-NM/......./Mm........hMy...........:NM:..../hNNdyyyydNNy:.....+MNdddddddddy.........+Md.................................................................................................................................................................
.................://////:-...........//-............:/:.......-/:........//.............:/:......-:+oooo+:........-///////////:.........-/:.................................................................................................................................................................
............................................................................................................................................................................................................................................................................................................
.......................................................................................................................................................................................................................................................................................................
"""

import os
import pandas as pd

data_folder = 'Dataset'
cd = os.getcwd()
directory = '{}/{}'.format(cd, data_folder)

print('Merging Datasets')
all_csv = os.listdir(directory)

all_df = []
for file in all_csv:
    df = pd.read_csv('{}/{}'.format(directory, file), parse_dates=True)
    all_df.append(df)

phasor_data = pd.concat(all_df)

merged_folder = 'MergedDataset'

if not os.path.exists(merged_folder):
    os.makedirs(merged_folder)

phasor_data.to_csv('{}/full_dataset.csv'.format(merged_folder), index=False)
print("Dataset Merge Complete")
