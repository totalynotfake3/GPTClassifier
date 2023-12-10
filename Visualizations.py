import pandas as pd
import matplotlib.pyplot as plt
import chime


def load_csv():
    data_list = []
    base = pd.read_csv("Multi_Classification_BASE.csv")
    ft = pd.read_csv("Multi_Classification_FT.csv")
    instruct = pd.read_csv("Multi_Classification_INSTRUCT.csv")
    data_list.append(base)
    data_list.append(ft)
    data_list.append(instruct)

    return data_list


def accuracy_calculator(some_df):
    occurrences = (some_df['Ground_Truth'] == some_df['Predicted_Label']).sum()
    total_count = len(some_df)
    return occurrences/total_count

    
def specific_accuracy_calculator(some_df,keyword):
    occurrences = (some_df['Ground_Truth'] == some_df['Predicted_Label']).sum()
    total_count = len(some_df)
    return occurrences/total_count

    
def create_class_accuracy(disorder_list, frame_collection, overview):
    counter = 0 
    for frame in frame_collection:
        for disorder in disorder_list:
            filtered_frame = frame.loc[frame['Ground_Truth'] == disorder] 
            filtered_frame['Predicted_Label'] = filtered_frame['Predicted_Label'].str.upper()
            model = filtered_frame['Model'].iloc[0]
            accuracy = (filtered_frame['Ground_Truth'] == filtered_frame['Predicted_Label']).sum()
            overview.loc[counter] = [model , disorder , accuracy/ len(filtered_frame)]
            counter += 1
    return overview
            

data = load_csv()
columns = ["Model",  "Ground_Truth", "Predicted_Label"]
transfer = pd.DataFrame(columns=columns)
disorder_list = ['ADHD',
 'AUTISM',
 'BIPOLAR',
 'EATING DISORDER',
 'OCD',
 'PTSD',
 'SCHIZOPHRENIA']

some_df = create_class_accuracy(disorder_list, data, transfer)

grouped_df = some_df.groupby(['Model', 'Ground_Truth'])['Predicted_Label'].sum().unstack()

# Create the bar chart with customizations
colors = plt.cm.tab20c.colors
grouped_df.plot(kind='bar', stacked=False, color=colors)
plt.title('Predicted Labels by Model and Ground Truth')
plt.xlabel('Model')
plt.ylabel('Predicted Label')
plt.legend(title='Ground Truth', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('ModelAndClassAccuracy.png', bbox_inches='tight')  # Save as PNG file


grouped_df = some_df.groupby('Model')['Predicted_Label'].mean()
plt.figure(figsize=(10, 6))  
colors = plt.cm.tab10.colors  
bars = grouped_df.plot(kind='bar', color=colors)
plt.title('Overall Accuracy of model', fontsize=14)  
plt.xlabel('Model', fontsize=12)  
plt.ylabel('Accuracy per model', fontsize=12) 
plt.xticks(rotation=45) 
plt.grid(axis='y', linestyle='--', alpha=0.7)  

for bar in bars.patches:
    bars.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(bar.get_height(), 2), ha='center', va='bottom')

plt.savefig('AccuracyPerModel.png', bbox_inches='tight') 


print("Visualizations were created")
chime.theme('material')
chime.success()