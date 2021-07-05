def plot_feature_importance_lightgbm():
    ret_str = """def plot_feature_importance_lightgbm(model):
    plt.rcParams["figure.figsize"] = [12,9]
    lgb.plot_importance(model,importance_type='gain')
    plt.show()"""

    return ret_str

def get_important_features_lightgbm():
    ret_str = """def get_important_features_lightgbm(df,model):
    ret_list = list(zip(list(df.columns),lightgbm_model.booster_.feature_importance(importance_type='gain')))
    
    return [x[0] for x in sorted(ret_list, key=lambda x: x[1],reverse=True)]"""

    return ret_str

def fit_lightgbm_model():
    ret_str = """def fit_lightgbm_model(df,target_col,weight_col):
    df = make_copy_df(df)
    
    target = df[target_col]
    df.drop([target_col],axis=1,inplace=True)
    weight = df[weight_col]
    df.drop([weight_col],axis=1,inplace=True)
    
    model = lgb.LGBMClassifier(num_leaves=20,
                               max_depth=5,learning_rate=0.01,objective='binary',n_estimators=100, max_cat_threshold = 500)
    
    model.fit(df,target,sample_weight=weight,categorical_feature=get_categorical_cols())
    
    return model"""

    return ret_str

def make_lightgbm_model():
    ret_str = """lightgbm_model = fit_lightgbm_model(label_encoded_df,target_col,weight_col)
imp_feature_list_lightgbm = get_important_features_lightgbm(misced_df,lightgbm_model)"""

    return ret_str

def plotting_importance_lightgbm():
    ret_str = """plot_feature_importance_lightgbm(lightgbm_model)"""

    return ret_str