import os
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        try:
            image_path = os.path.join(images_dir, key)
            model_label = classifier(image_path, model).lower().strip()
            truth = results_dic[key][0]
            results_dic[key].extend([model_label, int(truth in model_label)])
        except Exception as e:
            print(f"Error classifying image {key}: {e}")
      