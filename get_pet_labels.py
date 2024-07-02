from os import listdir

def get_pet_labels(image_dir):
    
    results_dic = {}

    for filename in listdir(image_dir):
        if not filename.startswith('.'):
            file_parts = filename.lower().split('_')
            label = ' '.join([part for part in file_parts if part.isalpha()])
            if filename not in results_dic:
                results_dic[filename] = [label]
            else:
                results_dic[filename].append(label)

    return results_dic
