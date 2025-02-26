import pandas as pd
import numpy as np

# review row : 1485031

if __name__ == "__main__":
    data_path = "../data/"
    df = pd.read_csv(data_path+"clear_review_2018.csv", header=0, names=['id', 'name', 'cm_id','cb_id'])
    df.drop(columns=['id'], axis=1, inplace=True)
    df.index = np.arange(1, len(df)+1)
    df.to_csv(f"../data/category_sm_2018.csv")