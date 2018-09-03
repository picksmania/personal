import re

# Updating CONTROLLER SLOT with PRODUCT NAME in a Dictionary format

# ctrl_info = {}
# with open(r'C:\STORCLI\ctrl_show_simulated.txt', 'r') as FR:
#     all_ctrl = FR.read()
#     all_ctrl_details = re.split('\n', all_ctrl)
#
# pat = '(HPESmart.*.Gen10)'
# MR_ctrl = re.findall(pat,all_ctrl)
#
# for item in all_ctrl_details:
#     for ctrl in MR_ctrl:
#         if item.__contains__(ctrl):
#             ctrl_info.setdefault(ctrl,item[2])
# print ctrl_info
#
# for k,v in ctrl_info.items():
#     print v
############################################################################################


#def search_of_specific_drive(self):
print "*** starting Drive Check ***"
with open(r'C:\one_off.txt', 'r') as f:
    lines = f.readlines()
model_list = []
for line in lines:
    if '@' in line:
        line = line.split('@')
        model_list.append(line[0])
    else:
        model_list.append(line)
#print model_list
set_model = []
for model in model_list:
    model = str(model).replace('\n', '')
    if '_' in model:
        model_family = model.split('_')
        if len(model_family[-1]) > 6:
            set_model.append(model)
        else:
            set_model.append(model.rsplit('_', 1)[0])
    else:
        if len(model) > 5:  # filtering for new lines(/n) from the file
            print "No underscore found in the model %s, so adding the individual model " % model
            set_model.append(model)
print "The family of models for checking are %s" % str(set_model)


available_drive = {}
unavailable_drive = {}
unavailable_drive_family = {}
available_drive_with_id = {}
available_drive_with_ctrl_slot = {}
unavailable_drive_with_ctrl_slot = {}
flag = False

with open(r'C:\STORCLI\Mesa_Verde_Info.txt', 'r') as FR:
    all_drive_details = FR.read()
    all_pd_details_of_drive = re.split('\n', all_drive_details)

for family_model in set_model:
    family_model_list = family_model.split('_')
    for one_model in family_model_list:
        for one_drive_detail in all_pd_details_of_drive:
            #print "ONE DRIVE DETAIL::::",one_drive_detail
            if one_drive_detail.__contains__(one_model):
            #if one_model in one_drive_detail:
                ar1 = re.split('\n', one_drive_detail)
                flag = True
                print "Model drive found is %s" % one_model
                available_drive.setdefault(family_model, []).append(one_model)
                available_drive_with_id[one_model] = ar1[0][:5]

if flag == True:
    for family_model in set_model:
        family_model_list = family_model.split('_')
        for one_model in family_model_list:
            if one_model not in [x for v in available_drive.values() for x in v]:
                unavailable_drive.setdefault(family_model, []).append(one_model)


print "The available drives with id are %s" % str(available_drive_with_id)
print "*************************************************************"
print "The available drives are %s" % str(available_drive)
print "*************************************************************"
print "The unavailable family drives are %s" % str(unavailable_drive)
print "*************************************************************"
print "The available drives with CONTROLLER SLOT are %s" % str(available_drive_with_ctrl_slot)
print "*************************************************************"
print "The unavailable DRIVE families are %s" % str(unavailable_drive_family)

#return available_drive,available_drive_with_id,unavailable_drive