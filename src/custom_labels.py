import torch
label_mapping = {
    0: "upper_part",
    1: "bottom_part",
    2: "onepiece",
    3: "footwear",
    4: "bags"
}

# Applying custom labelling as per the project requirements
def apply_custom_labels(labels):
    custom_labels = []
    for label in labels:
        if label in [0, 2, 4, 6]:
            custom_labels.append(0)
        elif label == 1:
            custom_labels.append(1)
        elif label == 3:
            custom_labels.append(2)
        elif label in [5, 7, 9]:
            custom_labels.append(3)
        elif label == 8:
            custom_labels.append(4)
    return torch.tensor(custom_labels)

