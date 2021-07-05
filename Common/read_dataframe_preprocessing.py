def get_constants():
    ret_str="""#Some Global Constants
categorical = 'categorical'
numerical = 'numerical'
categorical_null_val = 'None'"""

    return ret_str

def get_col_datatype_util():
    ret_str="""def get_col_datatype_util(col_datatype):
    return dict( [(col,str) if val==categorical else (col,float) for col,val in col_datatype.items()])"""

    return ret_str

def get_col_datatype(col_with_type):
    ret_str = """def get_col_datatype():
    col_datatype = """

    ret_str += col_with_type
    
    ret_str += """\n\n    return col_datatype"""

    return ret_str

def get_col_default():
    ret_str="""def get_col_default(df):
    return dict([(col,categorical_null_val) if val==categorical else (col,round(df[col].mean(),2)) for col,val in get_col_datatype().items()])"""

    return ret_str