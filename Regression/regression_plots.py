def get_avg_values_regression():
    ret_str = """#Diff from Classification
def get_avg_values(df,df_weight,col,weight_col,weighted_target_col):
    columns = set([x for x in df.index])

    df = df.to_dict()
    df_weight = df_weight.to_dict()

    values = dict()
    for i in columns:
        num = df.get(weighted_target_col).get(i) if df.get(weighted_target_col).get(i) is not None else 0
        den = df_weight.get(weight_col).get(i) if df_weight.get(weight_col).get(i) is not None else 0
        values[i] = 0 if num==0 else num/den

    values.pop(col_default.get(col),None)
    values.pop(misc_col_value,None)

    return values"""

    return ret_str

def get_topk_feature_val_regression():
    ret_str = """def get_topk_feature_val(df,col,target_col,weight_col,weighted_target_col,top_k):
    temp_df = df[[col,target_col,weight_col]]
    temp_df[weighted_target_col] = temp_df[target_col]*temp_df[weight_col]
        
    group_weight = return_top_k(make_group(temp_df,[col],weight_col),weight_col,top_k)
    group = make_group(temp_df,[col],weighted_target_col)
    
    group= group[group[col].isin(group_weight[col])]
    
    group.set_index(col,inplace=True)
    group_weight.set_index(col,inplace=True)
    
    return get_avg_values(group,group_weight,col,weight_col,weighted_target_col)"""

    return ret_str

def avg_val_bar_plot_regression():
    ret_str = """def avg_val_bar_plot(df,col,target_col,weight_col,weighted_target_col,top_k):
    values = get_topk_feature_val(df,col,target_col,weight_col,weighted_target_col,top_k)
    
    sorted_values = sorted(values.items(), key=lambda kv: kv[1],reverse=True)
    sorted_x = [x[0] for x in sorted_values]
    sorted_y = [x[1] for x in sorted_values]
    
    plot_bar_chart(sorted_x,sorted_y,'Average Target Value : '+str(col))"""

    return ret_str

def dist_plot_regression():
    ret_str = """def dist_plot(df,col,weight_col,nbins):
    title = col
    
    temp_df = df[[col,weight_col]]
    temp_df = fill_default_values(temp_df)
    temp_df = remove_outliers(temp_df,col,weight_col)
    
    ax = sns.distplot(temp_df[col],kde=True,bins=nbins,
                 hist_kws={'weights': temp_df[weight_col]})
    ax.set(xlabel=col, ylabel='Probability',title=title)
    
    plt.show()"""

    return ret_str

def average_value_plot_regression():
    ret_str = """def average_value_plot(df,col,target_col,weight_col,weighted_target_col):
    for c in col:
        if col_datatype.get(c)==categorical:
            avg_val_bar_plot(df,c,target_col,weight_col,weighted_target_col,100)
        elif col_datatype.get(c)==numerical:
            dist_plot(df,c,weight_col,100)"""

    return ret_str