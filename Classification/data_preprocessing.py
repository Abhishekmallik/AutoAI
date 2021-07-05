def categorical_to_numerical_TBS():
    ret_str = """#Creating Numerical DF
def cat_to_numerical_TBS(col,prior,default_val,group,weight_col,include_na=True):
    if (include_na) & (col==default_val):
        return None
    
    weight_target_zero = group.get(weight_col).get((col, 0)) if group.get(weight_col).get((col, 0)) is not None else 0
    weight_target_one = group.get(weight_col).get((col, 1)) if group.get(weight_col).get((col, 1)) is not None else 0
    
    summation = weight_target_zero + weight_target_one + 1
    
    retval = (weight_target_one+prior)/summation
    return retval

vectorized_cat_to_numerical_TBS = np.vectorize(cat_to_numerical_TBS)"""

    return ret_str

def calculate_prior():
    ret_str = """def calculate_prior(df,target_col,weight_col):
    group = make_group(df,[target_col],weight_col,reset_index=False).to_dict()
    prior = group.get(weight_col).get(1)/((group.get(weight_col).get(0)+group.get(weight_col).get(1)))
    return prior"""

    return ret_str

def make_numerical_df():
    ret_str = """def make_numerical_df(df,target_col,weight_col,include_na=True):
    df = make_copy_df(df)
    df = fill_default_values(df)
    
    numerical_df = pd.DataFrame(columns = list(df.columns))
    numerical_df[target_col] = df[target_col]
    numerical_df[weight_col] = df[weight_col]
    
    prior = calculate_prior(df,target_col,weight_col)
    
    for col in get_categorical_cols():
        group = make_group(df,[col,target_col],weight_col,reset_index=False).to_dict()
        default_val = col_default.get(col)
        numerical_df[col] = vectorized_cat_to_numerical_TBS(df[col],prior,default_val,group,weight_col,include_na)
    
    for col in get_numerical_cols():
        numerical_df[col] = df[col]
        
    return numerical_df"""

    return ret_str

def numerical_df_without_na():
    ret_str = """numerical_df_without_na = make_numerical_df(misced_df,target_col,weight_col,False)"""

    return ret_str

def categorical_to_numerical_WOE():
    ret_str = """def cat_to_numerical_WOE(col,prior_zero,prior_one,default_val,group,weight_col,total_zero,total_one,capval,include_na=True):
    if (include_na) & (col==default_val):
        return None
    
    weight_target_zero = group.get(weight_col).get((col, 0)) if group.get(weight_col).get((col, 0)) is not None else 0
    weight_target_one = group.get(weight_col).get((col, 1)) if group.get(weight_col).get((col, 1)) is not None else 0
    
    retval = math.log(((weight_target_one+prior_one)/total_one)/((weight_target_zero+prior_zero)/total_zero))

    if retval>capval:
        retval = capval
    elif retval<(-capval):
        retval = -capval
        
    return retval

vectorized_cat_to_numerical_WOE = np.vectorize(cat_to_numerical_WOE)"""

    return ret_str

def calculate_prior_WOE():
    ret_str = """def calculate_prior_WOE(df,target_col,weight_col):
    prior_one = (df[df[target_col]==1][weight_col]).sum()/df[weight_col].sum()
    prior_zero = (df[df[target_col]==0][weight_col]).sum()/df[weight_col].sum()
    return (prior_zero,prior_one)"""

    return ret_str

def make_woe_df():
    ret_str = """def make_woe_df(df,target_col,weight_col,include_na=True):
    df = make_copy_df(df)
    df = fill_default_values(df)
    
    woe_df = pd.DataFrame(columns = list(df.columns))
    woe_df[target_col] = df[target_col]
    woe_df[weight_col] = df[weight_col]
    
    prior_zero,prior_one = calculate_prior_WOE(df,target_col,weight_col)
    total_one = df[df[target_col]==1][weight_col].sum()
    total_zero = df[df[target_col]==0][weight_col].sum()
    
    for col in get_categorical_cols():
        group = make_group(df,[col,target_col],weight_col,reset_index=False).to_dict()
        default_val = col_default.get(col)
        woe_df[col] = vectorized_cat_to_numerical_WOE(df[col],prior_zero,prior_one,default_val,group,weight_col,total_zero,total_one,10,include_na)
    
    for col in get_numerical_cols():
        woe_df[col] = df[col]
        
    return woe_df"""

    return ret_str

def woe_df():
    ret_str = """woe_df = make_woe_df(misced_df,target_col,weight_col,False)"""

    return ret_str

