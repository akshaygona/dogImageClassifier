def adjust_results4_isadog(results_dic, dogfile):
    with open(dogfile, "r") as f:
        lines = [line.rstrip('\n') for line in f]
        unique_lines = list(set(lines))

    for key in results_dic:
        truthVal = results_dic[key][0] 
        truthVal2 = results_dic[key][1] 
        results_dic[key] = results_dic.get(key, []) 
        results_dic[key].append(int(truthVal in unique_lines))
        results_dic[key].append(int(truthVal2 in unique_lines))

    
