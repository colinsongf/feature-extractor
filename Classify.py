from Feature_Extractor import extract_csv, shuffle_record, extract_feature
from Feature_Extractor import GA_Select_Feature, GE_Global_Separability_Fitness
from Feature_Extractor import GE_Local_Separability_Fitness, GE_Multi_Accuration_Fitness
from Feature_Extractor import GE_Tatami
import sys

def extract_feature(csv_file_name):
    records = extract_csv(csv_file_name, delimiter=',')
    records = shuffle_record(records)
    fold_count = 1
    # define extractors
    extractors = [
        {'class': GA_Select_Feature, 'label':'GA Select Feature', 'color':'red', 'params':{'max_epoch':100,'population_size':200}},
        {'class': GE_Global_Separability_Fitness, 'label':'GE Global', 'color':'green', 'params':{'max_epoch':100,'population_size':200}},
        {'class': GE_Local_Separability_Fitness, 'label':'GE Local', 'color':'blue', 'params':{'max_epoch':100,'population_size':200}},
        {'class': GE_Multi_Accuration_Fitness, 'label':'GE Multi', 'color':'magenta', 'params':{'max_epoch':100,'population_size':200}},
        {'class': GE_Tatami, 'label':'GE Tatami', 'color':'black', 'params':{'max_epoch':100,'population_size':200}},
    ]
    # get label
    file_name_partials = csv_file_name.split('.')
    if(len(file_name_partials)>1):
        label = '.'.join(file_name_partials[0:len(file_name_partials)-1])
    else:
        label = csv_file_name
    # extract feature
    extract_feature(records, label+' (whole)', fold_count, extractors)
    fold_count = 5
    extract_feature(records, label+' (5 fold)', fold_count, extractors)

if __name__ == '__main__':
    if len(sys.argv>1):
        csv_file_name = sys.argv[1]
    else:
        print('Give me a csv file name:')
        csv_file_name = raw_input()
    extract_feature(csv_file_name)