def categorical_to_numerical_TBS_regression():
    ret_str = """#Make Encoded Data
def categorical_to_numerical_TBS(col,default_val,group,group_weight,weight_col,weighted_target_col,prior,include_na=False):
    if (include_na==True) & (col==default_val):
        return None
    
    num = group.get(weighted_target_col).get(col) if group.get(weighted_target_col).get(col) is not None else 0
    den = group_weight.get(weight_col).get(col) if group_weight.get(weight_col).get(col) is not None else 0
    den = den+1
    retval = (num+prior)/den if num!=0 else 0
    return retval

v_categorical_to_numerical_TBS = np.vectorize(categorical_to_numerical_TBS)"""

    return ret_str

def calculate_prior_regression():
    ret_str = """def calculate_prior(df,target_col,weight_col):
    prior = ((df[target_col]*df[weight_col]).sum())/df[weight_col].sum()
    return round(prior,4)"""

    return ret_str

def make_numerical_df_regression():
    ret_str = """def make_numerical_df(df,target_col,weight_col,weighted_target_col,include_na=True):
    df = make_copy_df(df)
    df = fill_default_values(df)
    
    numerical_df = pd.DataFrame(columns = list(df.columns))
    numerical_df[target_col] = df[target_col]
    numerical_df[weight_col] = df[weight_col]
    
    df[weighted_target_col] = df[target_col]*df[weight_col]
    prior = calculate_prior(df,target_col,weight_col)
    
    for col in get_categorical_cols():
        group = make_group(df,[col],weighted_target_col,fill_na=False,reset_index=False).to_dict()
        group_weight = make_group(df,[col],weight_col,fill_na=False,reset_index=False).to_dict()
        default_val = col_default.get(col)
        numerical_df[col] = v_categorical_to_numerical_TBS(df[col],default_val,group,group_weight,weight_col,
                                                           weighted_target_col,prior,include_na)
                                                            
    for col in get_numerical_cols():
        numerical_df[col] = df[col]
        
    return numerical_df"""

    return ret_str

def numerical_df_without_na_regression():
    ret_str = """numerical_df_without_na = make_numerical_df(misced_df,target_col,weight_col,weighted_target_col,False)"""

    return ret_str