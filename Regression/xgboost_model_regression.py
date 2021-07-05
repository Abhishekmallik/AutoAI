def import_xgboost_libraries_regression():
    ret_str = """from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor,plot_importance,plot_tree
import graphviz"""

    return ret_str

def fit_xgboost_model_regression():
    ret_str = """def fit_xgboost_model(df,target_col,weight_col):
    df = make_copy_df(df)

    target = df[target_col]
    df.drop([target_col],axis=1,inplace=True)
    weight = df[weight_col]
    df.drop([weight_col],axis=1,inplace=True)
    
    model = XGBRegressor(max_depth=5,learning_rate=0.1,n_estimators=10,missing=None,silent=False)
    model.fit(df,target,sample_weight=weight)
    
    return model"""

    return ret_str

def make_numerical_df_na_regression():
    ret_str = """numerical_df = make_numerical_df(misced_df,target_col,weight_col,weighted_target_col,True)"""

    return ret_str

def plot_weightplot_target_based_regression():
    ret_str = """average_value_plot(df,ret_list,target_col,weight_col,weighted_target_col)"""
    return ret_str

def plot_average_value_plot_regression():
    ret_str ="""average_value_plot(misced_df,ret_list,target_col,weight_col,weighted_target_col)"""

    return ret_str

def plot_boxplot_regression():
    ret_str = """# box_plot(misced_df,[target_col],weight_col,col_datatype)
ax = plt.boxplot(misced_df[target_col],notch=True,showfliers=False)"""

    return ret_str

def plot_scatterplot_regression():
    ret_str = """scatter_plot(misced_df,['device_id'],target_col,weight_col,col_datatype)"""

    return ret_str


def get_ret_list_regression():
    ret_str = """ret_list = rank_mean(misced_df,coeff_df,'col',imp_feature_list_xgboost,imp_feature_list_lightgbm)"""
    return ret_str

