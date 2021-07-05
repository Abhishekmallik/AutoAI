def set_plt_params():
    ret_str = """def set_plt_params(width,height,title,xlabel,ylabel):
    plt.rcParams["figure.figsize"] = [width,height]
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)"""

    return ret_str