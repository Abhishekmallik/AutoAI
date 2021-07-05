def group_bar_chart():
    ret_str = """def plot_group_bar_chart(df,col,target_col,weight_col,title,top_k):
    df_target_one = df[df[target_col]==1]
    df_target_zero = df[df[target_col]==0]

    trace_target_zero = get_bar_trace(df_target_zero[col],df_target_zero[weight_col],'Not Visible')
    trace_target_one = get_bar_trace(df_target_one[col],df_target_one[weight_col],'Visible')

    data = [trace_target_zero,trace_target_one]
    layout = go.Layout(barmode='group',title=title,xaxis=dict(type='category'))

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)"""

    return ret_str

def get_topk_feature_val():
    ret_str = """def get_topk_feature_value(df,col,target_col,weight_col,top_k):
    group_with_weight = return_top_k(make_group(df,[col],weight_col),weight_col,top_k)
    
    group_with_target_and_weight = make_group(df,[col,target_col],weight_col)
    
    group = group_with_target_and_weight[group_with_target_and_weight[col].isin(group_with_weight[col])]
    group = group[(group[col]!=col_default.get(col)) & (group[col]!=misc_col_value)]
    
    return group"""

    return ret_str

def bar_plot():
    ret_str = """# BarPlot of the classes of a category for Visible and Not Visible Target
def bar_plot(df,col,target_col,weight_col,top_k):
    title_name = col
    
    group = get_topk_feature_value(df,col,target_col,weight_col,top_k)
    
    plot_group_bar_chart(group,col,target_col,weight_col,title_name,top_k)"""

    return ret_str


def hist_plot_target():
    ret_str = """def hist_plot_target(df,col,target_col,weight_col,nbins):
    title = col

    temp_df = df[[col,target_col,weight_col]]
    temp_df = fill_default_values(temp_df)
    temp_df = remove_outliers(temp_df,col,weight_col)
    
    temp_df_target_one = temp_df[temp_df[target_col]==1]
    temp_df_target_zero = temp_df[temp_df[target_col]==0]

    set_plt_params(12,9,'Hist 0/1',col,'Weight')
    plt.hist(temp_df_target_zero[col], bins=nbins, alpha=0.5, label='0',weights=temp_df_target_zero[weight_col])
    plt.hist(temp_df_target_one[col], bins=nbins, alpha=0.5, label='1',weights=temp_df_target_one[weight_col])
    plt.legend(loc='upper right')
    plt.show()"""

    return ret_str

def weight_plot_target():
    ret_str = """def weight_plot_target(df,col,target_col,weight_col):
    for c in col:
        if col_datatype.get(c)==categorical:
            bar_plot(df,c,target_col,weight_col,100)
        elif col_datatype.get(c)==numerical:
            hist_plot_target(df,c,target_col,weight_col,100)"""

    return ret_str


def get_avg_values():
    ret_str = """def get_avg_values(df,col,target_col,weight_col,top_k):
    group = get_topk_feature_value(df,col,target_col,weight_col,top_k)  
    columns = set(group[col].unique())
    
    group = group.set_index([col,target_col])
    group = group.to_dict()
    
    values = dict()
    for i in columns:
        val1 = group.get(weight_col).get((i,0)) if group.get(weight_col).get((i,0)) is not None else 0
        val2 = group.get(weight_col).get((i,1)) if group.get(weight_col).get((i,1)) is not None else 0
        values[i] = 0 if val2==0 else val2/(val1+val2)

    values.pop(col_default.get(col),None)
    values.pop(misc_col_value,None)
    
    return values"""

    return ret_str


def avg_val_bar_plot():
    ret_str = """#Plot the Encoded Value of each feature value in a feature
def avg_val_bar_plot(df,col,target_col,weight_col,top_k):
    values = get_avg_values(df,col,target_col,weight_col,top_k)
    
    sorted_values = sorted(values.items(), key=lambda kv: kv[1],reverse=True)
    sorted_x = [x[0] for x in sorted_values]
    sorted_y = [x[1] for x in sorted_values]
    
    plot_bar_chart(sorted_x,sorted_y,'Average Target Value : '+str(col))"""

    return ret_str


def dist_plot():
    ret_str = """def dist_plot(df,col,weight_col,nbins):
    title = col

    temp_df = df[[col,weight_col]]
    temp_df = fill_default_values(temp_df)
    temp_df = remove_outliers(temp_df,col,weight_col)

    ax = sns.distplot(temp_df[col],kde=True,bins=nbins,
                 hist_kws={'weights': temp_df[weight_col]})
    ax.set(xlabel=col, ylabel='PDF Value',title=title)
    plt.show()"""

    return ret_str


def average_value_plot():
    ret_str = """def average_value_plot(df,col,target_col,weight_col):
    for c in col:
        if col_datatype.get(c)==categorical:
            avg_val_bar_plot(df,c,target_col,weight_col,500)
        elif col_datatype.get(c)==numerical:
            dist_plot(df,c,weight_col,100)"""

    return ret_str
