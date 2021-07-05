def get_lightgbm_libraries():
    ret_str = """from sklearn.preprocessing import LabelEncoder
import lightgbm as lgb"""

    return ret_str

def label_encode_data():
    ret_str ="""def label_encode_data(df):
    df = make_copy_df(df)
    
    list_le = dict()
    for col in get_features(df):
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        list_le[col] = le
        
    return df,list_le"""

    return ret_str

def get_label_data_and_encoders():
    ret_str = """label_encoded_df,list_le = label_encode_data(misced_df)"""

    return ret_str

def lightgbm_clustering():
    ret_str = """def lightgbm_clustering(df,col,target_col,weight_col):
    target = df[target_col]
    weight = df[weight_col]
    
    train_df = pd.DataFrame(df[col])
    
    model = lgb.LGBMClassifier(boosting_type='gbdt',num_leaves=14,
                               max_depth=4,learning_rate=1,objective='binary',n_estimators=1, max_cat_threshold = 1000)
    
    model.fit(train_df,target,sample_weight=weight,categorical_feature=col)
    
    return model"""

    return ret_str

def lightgbm_clustering_regression():
    ret_str = """def lightgbm_clustering(df,col,target_col,weight_col):
    target = df[target_col]
    weight = df[weight_col]
    
    train_df = pd.DataFrame(df[col])
    
    model = lgb.LGBMRegressor(boosting_type='gbdt',num_leaves=14,
                               max_depth=4,learning_rate=1,objective='regression',n_estimators=1, max_cat_threshold = 1000)
    
    model.fit(train_df,target,sample_weight=weight,categorical_feature=col)
    
    return model"""

    return ret_str

def save_cluster():
    ret_str = """def save_cluster(cluster_fig):
    cluster_fig.render(view=True)"""
    return ret_str

def make_cluster():
    ret_str = """lightgbm_cluster = lightgbm_clustering(label_encoded_df,["hour_id"],target_col,weight_col)"""

    return ret_str

def display_cluster():
    ret_str = """cluster_fig = lgb.create_tree_digraph(lightgbm_cluster,tree_index=0,filename='hour_tree',format='png')
save_cluster(cluster_fig)
cluster_fig"""

    return ret_str
