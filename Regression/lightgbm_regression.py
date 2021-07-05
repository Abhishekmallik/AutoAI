def fit_lightgbm_model_regression():
    ret_str = """def fit_lightgbm_model(df,target_col,weight_col):
    df = make_copy_df(df)
    
    target = df[target_col]
    df.drop([target_col],axis=1,inplace=True)
    weight = df[weight_col]
    df.drop([weight_col],axis=1,inplace=True)
    
    model = lgb.LGBMRegressor(num_leaves=20,
                               max_depth=4,learning_rate=0.01,objective='regression',n_estimators=100)
    
    model.fit(df,target,sample_weight=weight,categorical_feature=get_categorical_cols())
    
    return model"""

    return ret_str