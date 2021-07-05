def plot_importance():
    ret_str = """# Plotting Feature Importance
def plot_feature_importance(model,importance_type):
    plt.rcParams["figure.figsize"] = [12,9]
    plot_importance(model,importance_type=importance_type)
    plt.show()"""

    return ret_str

def plot_and_save_boosted_trees():
    ret_str = """# Plotting Tree Models
def plot_and_save_boosted_trees(model,num_of_trees,filename,width,height):
    plt.rcParams["figure.figsize"] = [width,height]

    i=0
    for i in range(num_of_trees):
        plot_tree(model,num_trees=i)
        plt.savefig(filename+str(i)+".png",dpi=150)
        plt.show()"""

    return ret_str

def get_important_features():
    ret_str = """def get_important_features(model):
    features_importance = model.get_booster().get_score(importance_type='cover')
    sorted_features_importance = sorted(features_importance.items(), key=lambda kv: kv[1],reverse=True)
    
    ret_list = list()
    for i in range(len(sorted_features_importance)):
        ret_list.append(sorted_features_importance[i][0])
    
    return ret_list"""

    return ret_str
