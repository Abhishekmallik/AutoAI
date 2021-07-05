def cramers_v():
    ret_str = """def cramers_bias_corrected(df,col1,col2,weight_col):
    confusion_matrix = pd.crosstab(df[col1], df[col2], df[weight_col], aggfunc=sum)
    confusion_matrix.fillna(0,inplace=True)
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))    
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))"""

    return ret_str

def categorical_corr_df():
    ret_str = """def categorical_corr_df(df,weight_col,target_col=None):
    columns = get_categorical_cols()
    if(len(columns)==1):
        return
    
    if target_col is not None:
        corr = pd.DataFrame(index=columns,columns=[target_col])
        i=0
        while i<len(columns):
            corr.ix[columns[i]][target_col] = cramers_bias_corrected(df,columns[i],target_col,weight_col)
            i+=1
        corr.sort_values(by=target_col,ascending=False,inplace=True)
    else:
        corr = pd.DataFrame(index=columns,columns=columns)
        
        i=0
        while i<len(columns):
            j=i
            while j<len(columns):
                if i==j:
                    corr.ix[columns[i]][columns[j]] = 1
                else:
                    corr.ix[columns[j]][columns[i]] = cramers_bias_corrected(df,columns[i],columns[j],weight_col)
                    corr.ix[columns[i]][columns[j]] = corr.ix[columns[j]][columns[i]]
                j+=1
            i+=1
            
    return corr"""

    return ret_str

def categorical_corr():
    ret_str = """cat_corr = categorical_corr_df(misced_df,weight_col)
cat_corr"""

    return ret_str

def pearson_functions():
    ret_str = """def cov(df, col1, col2, weight_col):
    mean_col1 = weighted_mean(df,col1,weight_col)
    mean_col2 = weighted_mean(df,col2,weight_col)
    return ((df[weight_col]*((df[col1]-mean_col1)*(df[col2]-mean_col2))).sum())/get_total(df,weight_col)

def get_pearson_coeff(df,col1,col2,weight_col):
    num = cov(df,col1,col2,weight_col)
    std1 = weighted_std(df,[col1],weight_col)[0]
    std2 = weighted_std(df,[col2],weight_col)[0]
    den = std1*std2
    return num/den"""

    return ret_str

def numerical_corr_df():
    ret_str = """def numerical_corr_df(df,weight_col,target_col=None):
    #Change the below line to get_numerical_columns
    columns = get_numerical_cols()
    if(len(columns)==1):
        return
    
    if target_col is not None:
        corr = pd.DataFrame(index=columns,columns=[target_col])
        i=0
        while i<len(columns):
            corr.ix[columns[i]][target_col] = get_pearson_coeff(df,columns[i],target_col,weight_col)
            i+=1
        corr.sort_values(by=target_col,ascending=False,inplace=True)
    else:
        corr = pd.DataFrame(index=columns,columns=columns)
    
        i=0
        while i<len(columns):
            j=i
            while j<len(columns):
                corr.ix[columns[j]][columns[i]] = get_pearson_coeff(df,columns[i],columns[j],weight_col)
                corr.ix[columns[i]][columns[j]] = corr.ix[columns[j]][columns[i]]
                j+=1
            i+=1
            
    return corr"""

    return ret_str

def numerical_corr():
    ret_str = """num_corr = numerical_corr_df(misced_df,weight_col)
num_corr"""

    return ret_str

def corr_with_categorical_target():
    ret_str = """#Correlation with Target
corr_target = categorical_corr_df(misced_df,weight_col,target_col)
corr_target"""

    return ret_str

def corr_with_numerical_target():
    ret_str = """#Correlation with Target
corr_target = numerical_corr_df(misced_df,weight_col,target_col)
corr_target"""

    return ret_str