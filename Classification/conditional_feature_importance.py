def conditional_feature_importance_util():
    ret_str = """from sklearn.metrics import log_loss

def conditional_feature_importance_util(df,target,weight,columns,model):
    train_df = df[columns]
    logloss_df = pd.DataFrame(columns=['Features','Logloss Reduction'])
    
    model.fit(train_df,target,sample_weight = weight)
    predicted_target = model.predict_proba(train_df)
    initial_logloss = log_loss(target,predicted_target,sample_weight = weight)
    
    for col in set(get_features(df))-set(columns):
        train_df[col] = df[col]
        
        model.fit(train_df,target,sample_weight=weight)
        predicted_target = model.predict_proba(train_df)
        
        logloss = log_loss(target,predicted_target,sample_weight = weight)
        logloss_df = logloss_df.append({'Features':col,'Logloss Reduction':initial_logloss-logloss},ignore_index=True)
        train_df.drop(col,axis=1,inplace=True)
        
    return logloss_df"""

    return ret_str

def conditional_feature_importance():
    ret_str = """def conditional_feature_importance(df,df_with_null,columns):
    df = make_copy_df(df)
    
    target = df[target_col]
    df.drop([target_col],axis=1,inplace=True)
    weight = df[weight_col]
    df.drop([weight_col],axis=1,inplace=True)
    
    model = LogisticRegression(penalty='l1',C=0.005,verbose=1)
    logloss_logistic = conditional_feature_importance_util(df,target,weight,columns,model)
    
    model = XGBClassifier(learning_rate=0.1,max_depth=5,n_estimators=5,booster='gbtree',silent=False,missing=None)
    logloss_xgboost = conditional_feature_importance_util(df_with_null,target,weight,columns,model)
    
    return (logloss_logistic,logloss_xgboost)"""

    return ret_str

def get_conditional_feature_importance():
    ret_str = """(logloss_logistic,logloss_xgboost) = conditional_feature_importance(woe_df,numerical_df,['creative_id'])"""

    return ret_str