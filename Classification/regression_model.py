def import_regression_libraries():
    ret_str = """#Logistic Regression Model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import RFE"""

    return ret_str

def weighted_mean():
    ret_str = """def weighted_mean(df,col, weight_col):
    return (df[col]*df[weight_col]).sum()/df[weight_col].sum()"""

    return ret_str

def weighted_std():
    ret_str = """def weighted_std(df,columns,weight_col):
    den = get_total(df,weight_col)
    std_list = list()
    
    for col in columns:
        mean = weighted_mean(df,col,weight_col)
        diff = (df[col]-mean)**2
        diff = diff*df[weight_col]
        std_list.append(math.sqrt(diff.sum()/den))
        
    return std_list"""

    return ret_str

def get_coeff_df():
    ret_str = """def get_coeff_df(df,model,columns):
    coeff_df = pd.DataFrame(columns=['col','coeff','std','Coefficient'])
    coeff_df['coeff'] = list(model.coef_[0])
    coeff_df['col'] = columns
    coeff_df['std'] = weighted_std(df,columns,weight_col)
    coeff_df['Coefficient'] = abs(coeff_df['coeff']*coeff_df['std'])
    coeff_df = coeff_df.sort_values(by='Coefficient',ascending=False)
    coeff_df.drop(['coeff','std'],axis=1,inplace=True)
    return coeff_df"""

    return ret_str

def fit_logistic_regression_model():
    ret_str = """def fit_logistic_regression_model(df,target_col,weight_col,columns=None,reg=False,c=1):
    train_df = make_copy_df(df)
    
    target = train_df[target_col]
    train_df.drop([target_col],axis=1,inplace=True)
    weight = train_df[weight_col]
    train_df.drop([weight_col],axis=1,inplace=True)
    
    if columns is not None:
        train_df.drop(columns,axis=1,inplace=True)
    
    if reg:
        model = LogisticRegression(penalty='l1',C=c,verbose=1)
    else:
        model = LogisticRegression(verbose=1)
        
    model.fit(train_df,target,sample_weight=weight)
    
    train_df[target_col] = df[target_col]
    train_df[weight_col] = df[weight_col]
    coeff_df = get_coeff_df(train_df,model,get_features(train_df))
    
    return (model,coeff_df)"""

    return ret_str

def make_logisitic_model():
    ret_str = """logistic_model,coeff_df = fit_logistic_regression_model(numerical_df_without_na,target_col,weight_col,['os_id'],True,0.005)"""

    return ret_str

def display_logistic_coeff():
    ret_str = """coeff_df"""

    return ret_str

def fit_logistic_regression_model_woe():
    ret_str = """def fit_logistic_regression_model_woe(df,target_col,weight_col,columns=None,reg=False,c=1):
    train_df = make_copy_df(df)
    
    target = train_df[target_col]
    train_df.drop([target_col],axis=1,inplace=True)
    weight = train_df[weight_col]
    train_df.drop([weight_col],axis=1,inplace=True)
    
    if columns is not None:
        train_df.drop(columns,axis=1,inplace=True)
    
    if reg:
        model = LogisticRegression(penalty='l1',C=c,verbose=1)
    else:
        model = LogisticRegression(verbose=1)
        
    model.fit(train_df,target,sample_weight=weight)
    
    train_df[target_col] = df[target_col]
    train_df[weight_col] = df[weight_col]
    coeff_df = pd.DataFrame(columns=['col','Coefficient'])
    coeff_df['col'] = get_features(train_df)
    coeff_df['Coefficient'] = abs(model.coef_[0])
    coeff_df.sort_values(by='Coefficient',inplace=True,ascending=False)
    
    return (model,coeff_df)"""

    return ret_str

def make_logisitic_model_woe():
    ret_str = """logistic_model_woe,coeff_df_woe = fit_logistic_regression_model_woe(woe_df,target_col,weight_col,None,True,0.005)"""

    return ret_str


def display_logistic_coeff_woe():
    ret_str = """coeff_df_woe"""

    return ret_str

def stepwise_addition_logistic_regression():
    ret_str = """from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

def stepwise_addition_logistic_regression(df,coeff_df,target_col,weight_col,reg=False,c=1):
    df = make_copy_df(df)
    
    logloss_df = pd.DataFrame(columns=['Feature','Logloss'])
    
    target = df[target_col]
    df.drop([target_col],axis=1,inplace=True)
    weight = df[weight_col]
    df.drop([weight_col],axis=1,inplace=True)
    
    train_df = pd.DataFrame()
    
    if reg:
        model = LogisticRegression(penalty='l1',C=c,verbose=1)
    else:
        model = LogisticRegression(verbose=1)
        
    for col in coeff_df['col']:
        train_df[col] = df[col]    
        model.fit(train_df,target,sample_weight=weight)
        
        predicted_target = model.predict_proba(train_df)
        logloss = log_loss(target,predicted_target,sample_weight = weight)
        
        logloss_df = logloss_df.append({'Feature': col,'Logloss':logloss}, ignore_index=True)
    
    return logloss_df"""

    return ret_str

def logloss_df_stepwise_addition():
    ret_str = """#Logloss on addition of features
logloss_df = stepwise_addition_logistic_regression(numerical_df_without_na,coeff_df,target_col,weight_col,True,0.005)"""

    return ret_str

def stepwise_addition_linear_regression():
    ret_str = """from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

def stepwise_addition_linear_regression(df,coeff_df,target_col,weight_col,reg=False,alpha=1):
    df = make_copy_df(df)
    
    r2_df = pd.DataFrame(columns=['Feature','R2 Coeff'])
    
    target = df[target_col]
    df.drop([target_col],axis=1,inplace=True)
    weight = df[weight_col]
    df.drop([weight_col],axis=1,inplace=True)
    
    train_df = pd.DataFrame()
    
    if reg:
        model = Lasso(alpha=alpha)
    else:
        model = LinearRegression()
        
    for col in coeff_df['col']:
        train_df[col] = df[col]    
        model.fit(train_df,target)
        
        r_square_coeff = model.score(train_df,target)
        
        r2_df = r2_df.append({'Feature': col,'R2 Coeff':r_square_coeff}, ignore_index=True)
    
    return r2_df"""

    return ret_str

def r2_df_stepwise_addition():
    ret_str = """#R2 Coeff on addition of features
r2_df = stepwise_addition_linear_regression(numerical_df_without_na,coeff_df,target_col,weight_col,True,0.003)"""

    return ret_str