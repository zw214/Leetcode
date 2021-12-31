import os
from pathlib import Path
from trainer.config import config
import numpy as np
import itertools
from sklearn.metrics import roc_curve, auc

def get_all_files(folder, ext):
    """Returns a list of file paths under the folder with given extension
    """
    file_list = []
    for root, dirs, files in sorted(os.walk(folder)):
        for name in sorted(files):
            if ext in name:
                curr_path = os.path.join(root, name)
                #print(curr_path)
                file_list.append(curr_path)

    return file_list

def get_sel_boxes(filepath):
    box_list = open(filepath, 'r').read().splitlines()
    sel_boxes = [b for b in box_list if len(b.split(' ')) == 9] #TODO b.split(' ')[8] != '0.000\n'
    return sel_boxes

def get_truth_and_pred_arrays(sel_boxes):
    truth_and_pred_array_list = []
    for i in range(len(sel_boxes)):
        object_score, xmin, ymin, xmax, ymax, lesion, iou, class_score = sel_boxes[i].split(' ')[1:]
        class_score = float(class_score)
        truth = int([int(x) for x in lesion][-1])
        truth_and_pred_array_list.append(np.array([truth, class_score]))
    return truth_and_pred_array_list

def make_outer_truth_pred_list(all_file_list, inner_truth_pred_array_list):
    all_unique = sorted(list(set(all_file_list)))
    count_lst = [all_file_list.count(s) for s in all_unique]
    print(count_lst)
    p=0
    outer_truth_pred_array_list = []
    for i in count_lst:
        outer_truth_pred_array_list.append(list(inner_truth_pred_array_list[p:p+i]))
        p += i
    outer_dict = dict(zip(all_unique, outer_truth_pred_array_list))
    return outer_dict, outer_truth_pred_array_list, all_unique

def flatten_list(list_of_lists):
    return list(itertools.chain.from_iterable(list_of_lists))

def choose_most_confident_patch(lst):
    ls = [item[1] for item in lst]
    max_value = max(ls)
    max_index = ls.index(max_value)
    return lst[max_index]

pos_saved_bbox_folder_val = '/Data/Shared_Workspace/mass+calc_malig_model/mass+calc/calc+mass_malignant_froc_info_BM/saved_bbox'

neg_saved_bbox_folder_val = '/Data/Shared_Workspace/mass+calc_malig_model/negative/neg_saved_bbox'

scoring_file_path_list = get_all_files(neg_saved_bbox_folder_val, '.txt')[:20] + get_all_files(pos_saved_bbox_folder_val, '.txt')[:20]

selected_boxes_list = [get_sel_boxes(scoring_file_path_list[i]) for i in range(len(scoring_file_path_list))]
#print(selected_boxes_list)
truth_and_pred_list = [get_truth_and_pred_arrays(sel_boxes) for sel_boxes in selected_boxes_list]
#print(truth_and_pred_list)
#print(scoring_file_path_list)

####roi level####
roi_level_truth_pred_list = list(itertools.chain.from_iterable(truth_and_pred_list))
#print(roi_level_truth_pred_list)
roi_truth = [item[0] for item in roi_level_truth_pred_list]
roi_pred = [item[1] for item in roi_level_truth_pred_list]
print(roi_truth)
print(roi_pred)

fpr, tpr, _ = roc_curve(y_true=roi_truth, y_score=roi_pred, pos_label=1.)
auc_score = auc(fpr, tpr)
print(auc_score)

####view level####
all_views = [os.path.basename(filename).rpartition('_')[0] for filename in scoring_file_path_list]
#print(all_views)
print(truth_and_pred_list)
view_dict, view_level_list, all_unique_views = make_outer_truth_pred_list(all_views, truth_and_pred_list)
print(view_level_list)
flat_view_level_list = [flatten_list(item) for item in view_level_list]
print(flat_view_level_list)

view_level_truth_pred_list = [choose_most_confident_patch(item) for item in flat_view_level_list if len(item)]
print(view_level_truth_pred_list)

view_truth = [item[0] for item in view_level_truth_pred_list]
view_pred = [item[1] for item in view_level_truth_pred_list]
print(view_truth)
print(view_pred)
fpr, tpr, _ = roc_curve(y_true=view_truth, y_score=view_pred, pos_label=1)
auc_score = auc(fpr, tpr)
print(auc_score)

####case level####
all_cases = ["_".join(filename.split("_", 2)[:2]) for filename in all_unique_views]
#print(all_cases)
case_dict, case_level_list, all_unique_cases = make_outer_truth_pred_list(all_cases, flat_view_level_list) #important to be flat_view_level_list

flat_case_level_list = [flatten_list(item) for item in case_level_list]

case_level_truth_pred_list = [choose_most_confident_patch(item) for item in flat_case_level_list if len(item)]

case_truth = [item[0] for item in case_level_truth_pred_list]
case_pred = [item[1] for item in case_level_truth_pred_list]
fpr, tpr, _ = roc_curve(y_true=case_truth, y_score=case_pred, pos_label=1)
auc_score = auc(fpr, tpr)
print(auc_score)
