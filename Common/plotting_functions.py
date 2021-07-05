def plot_pie_chart():
    ret_str = """def plot_pie_chart(labels,values,title):
    data = [go.Pie(
        labels=labels,
        values=values,
        marker=dict( colors = random_colors(len(labels)) ),
        textfont=dict( size = 20 )
    )]    
    layout = go.Layout(title = title)
    
    fig = go.Figure(data=data,layout=layout)
    py.iplot(fig)"""

    return ret_str

def pie_chart():
    ret_str = """def pie_chart(df,col,weight_col,top_k):
    title = col
    
    group = make_group(df,[col],weight_col)
    group_top_k = return_top_k(group,weight_col,top_k)
    
    set_values = set(group_top_k[col])
    group[col] = group[col].apply(lambda x:misc_col_value if x not in set_values else x)
    
    group = make_group(group,[col],weight_col)
    
    plot_pie_chart(group[col],group[weight_col],title)"""

    return ret_str

def get_value():
    ret_str = """def get_value(df,val,col,weight_col):
    index = df[weight_col].searchsorted(val)
    ret_df = df.iloc[index].reset_index()
    
    return (ret_df.iloc[0][col])"""

    return ret_str

def append_first_and_third_quartile():
    ret_str = """def append_first_and_third_quartile(arr,df,total_len,factor,col,weight_col):
    if ((total_len+1)%4)==0:
        arr.append(get_value(df,(total_len+1)*factor,col,weight_col))
    else:
        arr.append((get_value(df,math.ceil((total_len+1)*factor),col,weight_col)+get_value(df,math.floor((total_len+1)*factor),col,weight_col))/2)"""

    return ret_str

def quartiles():
    ret_str = """def quartiles(df,col,weight_col):
    df = make_copy_df(df)
    df.sort_values(by=col,inplace=True)
    df.reset_index()
    df[weight_col] = df[weight_col].cumsum()
    
    total_len = df.iloc[df.shape[0]-1][weight_col]
    arr = list()
    
    arr.append(df.iloc[0][col])
    append_first_and_third_quartile(arr,df,total_len,1/4,col,weight_col)
    
    if total_len%2==1:
        arr.append((get_value(df,total_len/2,col,weight_col)+get_value(df,(total_len/2)+1,col,weight_col))/2)
    else:
        arr.append(get_value(df,(total_len+1)/2,col,weight_col))
    
    append_first_and_third_quartile(arr,df,total_len,3/4,col,weight_col)
    arr.append(df.iloc[df.shape[0]-1][col])
    
    return arr"""

    return ret_str

def remove_outliers():
    ret_str = """def remove_outliers(df,col,weight_col):
    quar = quartiles(df,col,weight_col)
    iqr_range = quar[3]-quar[1]
    
    df = df[df[col]>(quar[1]-1.5*iqr_range)]
    df = df[df[col]<(quar[3]+1.5*iqr_range)]
    
    return df"""

    return ret_str

def hist_plot():
    ret_str = """def hist_plot(df,col,weight_col,nbins):
    title = col
    
    temp_df = df[[col,weight_col]]
    temp_df = fill_default_values(temp_df)
    temp_df = remove_outliers(temp_df,col,weight_col)

    set_plt_params(20,15,title,col,'Weight')
    plt.hist(temp_df[col],bins=nbins,weights=temp_df[weight_col])
    plt.show()"""

    return ret_str

def weight_plot():
    ret_str = """def weight_plot(df,col,weight_col):
    for c in col:
        if col_datatype.get(c)==categorical:
            pie_chart(df,c,weight_col,100)
        elif col_datatype.get(c)==numerical:
            hist_plot(df,c,weight_col,100)"""

    return ret_str

def get_bar_trace():
    ret_str = """def get_bar_trace(x,y,name=''):
    return go.Bar(x = x,y = y,name = name,opacity=0.6)"""

    return ret_str

def plot_bar_chart():
    ret_str = """def plot_bar_chart(x,y,title):
    trace = get_bar_trace(x,y)
    data = [trace]
    layout = go.Layout(title=title,xaxis=dict(type='category'))
    fig = go.Figure(data=data,layout=layout)
    py.iplot(fig)"""

    return ret_str

def calculate_missing_count():
    ret_str = """def calculate_missing_count(df,col,weight_col):
    temp_df = df[df[col].isnull()][weight_col]
    return temp_df.sum()"""

    return ret_str

def missing_values_plot():
    ret_str = """#Missing Values Plot (Count and Ratio)
def missing_values_plot(df,weight_col):
    feature_col = 'Features'
    count_col = 'Count'
    ratio_col = 'Ratio'
    
    missing = pd.DataFrame(columns=[feature_col,count_col,ratio_col])
    
    missing[feature_col]=get_features(df)
    missing[count_col] = missing[feature_col].apply(lambda col: calculate_missing_count(df,col,weight_col))
    
    total_weight = get_total(df,weight_col)
    
    missing[ratio_col] = missing[count_col].apply(lambda x:x/total_weight) 
    missing.sort_values(by=count_col,ascending=False,inplace=True)
    
    plot_bar_chart(missing[feature_col],missing[count_col],'Missing Count')
    plot_bar_chart(missing[feature_col],missing[ratio_col],'Missing Ratio')"""

    return ret_str

def do_missing_values_plot():
    ret_str = """missing_values_plot(make_copy_df(df),weight_col)"""

    return ret_str


def set_sns_params():
    ret_str = """def set_sns_params(figsize,ax_facecolor,fig_facecolor):
    sns.set(rc={'figure.figsize':figsize,'axes.facecolor':ax_facecolor, 'figure.facecolor':fig_facecolor})"""

    return ret_str


def scatter_plot_util():
    ret_str = """def scatter_plot_util(df,x_col,y_col,weight_col):
    set_sns_params((12,9),'white','white')
    sns.stripplot(x=x_col,y=y_col,data=df,jitter=True)"""

    return ret_str


def scatter_plot():
    ret_str = """def scatter_plot(df,columns,y_col,weight_col,col_datatype):
    if col_datatype.get(y_col)==numerical:
        for col in columns:
            scatter_plot_util(df,col,y_col,weight_col)"""

    return ret_str


def box_plot_util():
    ret_str = """def box_plot_util(df,title,col,weight_col,group_col=None):
    df = make_copy_df(df)
    data = []
    
    if group_col==None:
        arr = quartiles(df,col,weight_col)
        arr.insert(int(len(arr)/2),arr[int(len(arr)/2)])
        data.append(go.Box(y=arr))
    else:
        for c in df[group_col].unique():
            arr = quartiles(df[df[group_col]==c],col,weight_col)
            arr.insert(int(len(arr)/2),arr[int(len(arr)/2)])
            data.append(go.Box(y=arr,name=c))
    
    layout = go.Layout(title = title)
    fig = go.Figure(data=data,layout=layout)
    
    py.iplot(fig)"""

    return ret_str


def box_plot():
    ret_str = """def box_plot(df,columns,weight_col,col_datatype,group_col=None):
    for col in columns:
        if col_datatype.get(col)==numerical:
            box_plot_util(df,'Box Plot',col,weight_col,group_col)"""

    return ret_str

