def conditional_feature_importance_util_regression():
    ret_str = """from sklearn.metrics import r2_score

def conditional_feature_importance_util(df,target,weight,columns,model,islasso):
    train_df = df[columns]
    r2_df = pd.DataFrame(columns=['Features','R2 Coeff'])
    
    if islasso:
        model.fit(train_df,target)
        initial_r2_coeff = model.score(train_df,target)
    else:
        model.fit(train_df,target,sample_weight=weight)
        predicted_target = model.predict(train_df)
        initial_r2_coeff = r2_score(target,predicted_target,sample_weight=weight)
        
    for col in set(get_features(df))-set(columns):
        train_df[col] = df[col]
        
        if islasso:
            model.fit(train_df,target)
            r2_coeff = model.score(train_df,target)
        else:
            model.fit(train_df,target,sample_weight=weight)
            predicted_target = model.predict(train_df)
            r2_coeff = r2_score(target,predicted_target,sample_weight=weight)
        
        r2_df = r2_df.append({'Features':col,'R2 Coeff':r2_coeff-initial_r2_coeff},ignore_index=True)
        train_df.drop(col,axis=1,inplace=True)
        
    return r2_df"""

    return ret_str


def conditional_feature_importance_regression():
    ret_str = """def conditional_feature_importance(df,df_with_null,columns):
    df = make_copy_df(df)
    
    target = df[target_col]
    df.drop([target_col],axis=1,inplace=True)
    weight = df[weight_col]
    df.drop([weight_col],axis=1,inplace=True)
    
    model = Lasso(alpha=0.003)
    r2_linear = conditional_feature_importance_util(df,target,weight,columns,model,True)
    
    model = XGBRegressor(max_depth=5,learning_rate=0.1,n_estimators=5,booster='gbtree',missing=None,silent=False)
    r2_xgboost = conditional_feature_importance_util(df_with_null,target,weight,columns,model,False)
    
    return (r2_linear,r2_xgboost)"""

    return ret_str


def get_conditional_feature_importance_regression():
    ret_str = """(r2_linear,r2_xgboost) = conditional_feature_importance(numerical_df_without_na,numerical_df,['keyword_term'])"""

    return ret_str