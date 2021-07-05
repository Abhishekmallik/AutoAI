def target_and_weight_const(target_col,weight_col):
    ret_str = """target_col = """+target_col
    ret_str += """\nweight_col = """+weight_col

    return ret_str

def check_weight_col():
    ret_str = """if weight_col is None:
    weight_col='weight'
    df[weight_col] = 1"""

    return ret_str

def get_features():
    ret_str = """def get_features(df):
    return [x for x in list(df.columns) if x not in [target_col,weight_col]]
    
def get_categorical_cols():
    return [x for x,v in col_datatype.items() if v==categorical]
    
def get_numerical_cols():
    return [x for x,v in col_datatype.items() if v==numerical]"""

    return ret_str

def get_needful_functions():
    ret_str = """def random_colors(num_of_colors):
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(num_of_colors)]
    return color
    
def make_copy_df(df):
    return df.copy()
    
def get_total(df,col):
    return df[col].sum()
    
def fill_default_values(df):
    for c in get_features(df):
        df[c].fillna(col_default.get(c),inplace=True)
    return df
    
def return_top_k(df,col,top_k):
    temp_df = df.sort_values(by=col,ascending=False)
    return temp_df[:top_k]"""

    return ret_str

def unique_count():
    ret_str = """#Unique Values DataFrame
def unique_count(df):
    feature_col = 'Features'
    count_col = 'Unique Count'
    unique_count_df = pd.DataFrame(columns=[feature_col,count_col])
    
    unique_count_df[feature_col] = get_categorical_cols()
    unique_count_df[count_col] = unique_count_df[feature_col].apply(lambda col: df[col].nunique())
    
    return unique_count_df"""

    return ret_str

def make_unique_df():
    ret_str = """unique_count_df = unique_count(df)
unique_count_df"""

    return ret_str

def make_group():
    ret_str = """# This function returns the dataframe subset and fill NULL values with some other value
def make_group(df,col,weight_col,fill_na=False,reset_index=True):
    temp_df = pd.DataFrame(df[col+[weight_col]])
    
    if fill_na:
        temp_df = fill_default_values(temp_df)
    
    group = temp_df.groupby(col).agg({weight_col:'sum'})
    
    if reset_index:
        group = group.reset_index()
    
    return group"""

    return ret_str

def do_miscing():
    ret_str = """def do_miscing(df,col,weight_col,misc_percent):
    group = make_group(df,[col],weight_col)

    if_misc_col = 'if_misc'
    group[if_misc_col]=False
    
    summation = get_total(df,weight_col)*misc_percent*0.01
    
    group[if_misc_col] = group[weight_col].apply(lambda x:True if x<summation else False)
    group[col] = group.apply(lambda x:misc_col_value if x[if_misc_col] else x[col],axis=1)
    
    misced_group = make_group(group,[col],weight_col)
    return misced_group"""

    return ret_str

def is_feature_irrelevant():
    ret_str = """def is_feature_irrelevant(df,col,weight_col,misc_percent):    
    fin_group = do_miscing(df,col,weight_col,misc_percent)
    fin_group = fin_group[(fin_group[col]!=col_default.get(col)) & (fin_group[col]!=misc_col_value)]
    
    return fin_group.empty"""

    return ret_str

def get_irrelevant_features():
    ret_str = """def get_irrelevant_features(df,weight_col,misc_precent):
    irrelevant_cols=[]
    
    for col in get_features(df):
        if df[col].nunique()==df.shape[0]:
            irrelevant_cols.append(col)
        elif is_feature_irrelevant(df,col,weight_col,0.05):
            irrelevant_cols.append(col)
            
    return irrelevant_cols"""

    return ret_str

def remove_irrelevant_features():
    ret_str = """def remove_irrelevant_features(df,weight_col,misc_percent):
    irrelevant_features = get_irrelevant_features(df,weight_col,misc_percent)
    df.drop(irrelevant_features,axis=1,inplace=True)
    return df"""

    return ret_str

def remove_irrelevant_features_from_df():
    ret_str = """df = remove_irrelevant_features(df,weight_col,misc_percent)"""

    return ret_str


def make_misced_df():
    ret_str = """def make_misced_df(df,target_col,weight_col):
    df = make_copy_df(df)
    df = fill_default_values(df)
    
    misced_df = pd.DataFrame(columns = list(df.columns))
    misced_df[target_col] = df[target_col]
    misced_df[weight_col] = df[weight_col]
    
    for col in get_categorical_cols():
        misced_group = do_miscing(df,col,weight_col,misc_percent)
        unique_values = set(misced_group[col].unique())
        misced_df[col] = df[col].apply(lambda x: x if (x in unique_values) else misc_col_value)
    
    for col in get_numerical_cols():
        misced_df[col] = df[col]
        
    return misced_df"""

    return ret_str

def misced_df():
    ret_str = """misced_df = make_misced_df(make_copy_df(df),target_col,weight_col)
misced_df.head()"""

    return ret_str