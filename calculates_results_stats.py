def calculates_results_stats(results_dic):
    result = {}

    n_dogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0
    n_images = len(results_dic)

    for key in results_dic:
        n_dogs_img += results_dic[key][3]
        n_match += results_dic[key][2]
        if results_dic[key][3] > 0:
            n_correct_dogs += results_dic[key][4]
        if results_dic[key][3] == 0:
            n_correct_notdogs += results_dic[key][4] == 0
        if results_dic[key][2]:
            n_correct_breed += results_dic[key][3] == 1

    result['n_dogs_img'] = n_dogs_img
    result['n_match'] = n_match
    result['n_correct_dogs'] = n_correct_dogs
    result['n_correct_notdogs'] = n_correct_notdogs
    result['n_correct_breed'] = n_correct_breed
    result['n_images'] = n_images

    result['n_notdogs_img'] = n_images - n_dogs_img
    result['pct_match'] = (n_match / n_images) * 100.0
    result['pct_correct_dogs'] = (n_correct_dogs / n_dogs_img) * 100.0
    result['pct_correct_breed'] = (n_correct_breed / n_dogs_img) * 100.0

    if result['n_notdogs_img'] > 0:
        result['pct_correct_notdogs'] = (n_correct_notdogs / result['n_notdogs_img']) * 100.0
    else:
        result['pct_correct_notdogs'] = 0.0

    return result
    
