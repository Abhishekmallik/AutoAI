def import_xgboost_libraries():
    ret_str = """#XGBoost Implementation
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier,plot_importance,plot_tree
import graphviz"""
    return ret_str

def fit_xgboost_model():
    ret_str = """def fit_xgboost_model(df,target_col,weight_col):
    df = make_copy_df(df)
    
    target = df[target_col]
    df.drop([target_col],axis=1,inplace=True)
    weight = df[weight_col]
    df.drop([weight_col],axis=1,inplace=True)
    
    model = XGBClassifier(max_depth=5,learning_rate=0.1,n_estimators=10,missing=None,silent=False)
    model.fit(df,target,sample_weight=weight)
    
    return model"""

    return ret_str

def make_numerical_df_na():
    ret_str = """numerical_df = make_numerical_df(misced_df,target_col,weight_col,True)"""
    return ret_str

def make_xgboost_model():
    ret_str = """xgboost_model = fit_xgboost_model(numerical_df,target_col,weight_col)
imp_feature_list_xgboost = get_important_features(xgboost_model)"""

    return ret_str

def plotting_importance():
    ret_str = """plot_feature_importance(xgboost_model,'cover')"""

    return ret_str

def plotting_trees():
    ret_str = """plot_and_save_boosted_trees(xgboost_model,1,'final_xgboost_tree',40,30)"""

    return ret_str


def get_ret_list():
    ret_str = """ret_list = rank_mean(misced_df,coeff_df_woe,'col',imp_feature_list_xgboost,imp_feature_list_lightgbm)"""
    return ret_str

def get_ret_list_regression():
    ret_str = """ret_list = rank_mean(misced_df,coeff_df,'col',imp_feature_list_xgboost,imp_feature_list_lightgbm)"""
    return ret_str


def rank_mean_util():
    ret_str = """def rank_mean_util(df,col_list,rank_dict):
    col_set = set()
    
    i=1
    for col in col_list:
        rank_dict[col] = rank_dict[col]+i
        col_set.add(col)
        i +=1
        
    for col in get_features(df):
        if col not in col_set:
            rank_dict[col] +=i
    
    return rank_dict"""
    return ret_str

def rank_mean():
    ret_str = """def rank_mean(df,coeff_df_woe,coeff_col,imp_feature_list_xgboost,imp_feature_list_lightgbm):
    rank_dict = {}
    for col in get_features(df):
        rank_dict[col]=0
        
    rank_dict = rank_mean_util(df,list(coeff_df_woe[coeff_col]),rank_dict)
    rank_dict = rank_mean_util(df,imp_feature_list_xgboost,rank_dict)
    rank_dict = rank_mean_util(df,imp_feature_list_lightgbm,rank_dict)
    
    for col in rank_dict.keys():
        rank_dict[col] = rank_dict[col]/3
    
    sorted_by_rank = sorted(rank_dict.items(), key=lambda kv: kv[1])
    return [x[0] for x in sorted_by_rank]"""

    return ret_str

def add_to_list():
    ret_str = """def add_to_list(ret_list,columns=None):
    if columns is not None:
        return list(set(ret_list+columns))
    else:
        return ret_list"""

    return ret_str

def adding_features_to_list():
    ret_str = """ret_list = add_to_list(ret_list,['hour_id'])"""

    return ret_str

def plot_weightplot():
    ret_str = """weight_plot(misced_df,ret_list,weight_col)"""
    return ret_str

def plot_weightplot_target_based():
    ret_str = """weight_plot_target(misced_df,ret_list,target_col,weight_col)"""
    return ret_str

def plot_average_value_plot():
    ret_str = """average_value_plot(misced_df,ret_list,target_col,weight_col)"""

    return ret_str