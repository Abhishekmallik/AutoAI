def import_regression_libraries_regression():
    ret_str = """#Linear Regression Model
from sklearn.linear_model import LinearRegression,Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import RFE"""

    return ret_str

def get_coeff_df_regression():
    ret_str = """def get_coeff_df(df,model,columns):
    coeff_df = pd.DataFrame(columns=['col','coeff','std','Coefficient'])
    coeff_df['coeff'] = list(model.coef_)
    coeff_df['col'] = columns
    coeff_df['std'] = weighted_std(df,columns,weight_col)
    coeff_df['Coefficient'] = abs(coeff_df['coeff']*coeff_df['std'])
    coeff_df = coeff_df.sort_values(by='Coefficient',ascending=False)
    coeff_df.drop(['coeff','std'],axis=1,inplace=True)
    return coeff_df"""

    return ret_str

def fit_linear_regression_model():
    ret_str = """def fit_linear_regression_model(df,target_col,weight_col,columns=None,reg=False,alpha=1):
    train_df = make_copy_df(df)
    
    target = train_df[target_col]
    train_df.drop([target_col],axis=1,inplace=True)
    weight = train_df[weight_col]
    train_df.drop([weight_col],axis=1,inplace=True)
    
    if columns is not None:
        train_df.drop(columns,axis=1,inplace=True)
    
    if reg:
        model = Lasso(alpha=alpha)
    else:
        model = LinearRegression(verbose=1)
        
    model.fit(train_df,target)
    
    train_df[target_col] = df[target_col]
    train_df[weight_col] = df[weight_col]
    coeff_df = get_coeff_df(train_df,model,get_features(train_df))
    
    return (model,coeff_df)"""

    return ret_str

def make_linear_model():
    ret_str = """linear_model,coeff_df = fit_linear_regression_model(numerical_df_without_na,target_col,weight_col,None,True,0.003)"""

    return ret_str