def read_data_frame(path):
    ret_str = """df = pd.read_csv(r"""+ "\""+path+"\""+""",
                 dtype = get_col_datatype_util(get_col_datatype()))
df.head(10)"""

    return ret_str

def read_data_frame_regression(path):
    ret_str = r"""df = pd.read_csv(r""" + "\"" + path + "\"" + r""",
                 escapechar="\\",quotechar="\"",dtype = get_col_datatype_util(get_col_datatype()))
df.head(100)"""

    return ret_str
