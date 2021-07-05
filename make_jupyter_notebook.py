import nbformat as nbf
import os
import sys,getopt

from Common.libraries_import import *
from Common.read_dataframe_preprocessing import *
from Common.read_data_frame import *
from Common.prerequisite_functions import *
from Common.plotting_prerequisite_functions import *
from Common.plotting_functions import *
from Common.plot_xgboost_results import *
from Common.correlation import *

from Classification.data_preprocessing import *
from Classification.xgboost_model import *
from Classification.categorical_plots import *
from Classification.regression_model import *
from Classification.categorical_other_functions import *
from Classification.clustering import *
from Classification.conditional_feature_importance import *
from Classification.lightgbm import *

from Regression.numerical_other_functions import *
from Regression.regression_data_preprocessing import *
from Regression.regression_plots import *
from Regression.regression_model_regression import *
from Regression.xgboost_model_regression import *
from Regression.lightgbm_regression import *
from Regression.conditional_feature_importance_regression import *

def make_new_notebook():
    nb = nbf.v4.new_notebook()
    nb['cells'] = []
    return nb

def make_new_cell(code):
    ret_cell = nbf.v4.new_code_cell(code)
    return ret_cell

def make_new_markdown_cell(code):
    ret_cell = nbf.v4.new_markdown_cell(code)
    return ret_cell

def add_cell_to_notebook(nb,new_cell):
    nb['cells'].append(new_cell)

def make_file(nb,file_name):
    nbf.write(nb, file_name)

def run_file(file_name,output_file_name):
    os.system('jupyter nbconvert --ExecutePreprocessor.timeout=None --to notebook --execute '+file_name+' --output '+output_file_name)
    os.system('jupyter trust '+ output_file_name)

def main(col_with_type,target_col,weight_col,type_of_problem,path,save_name,output_save_name):
    nb = make_new_notebook()

    print(col_with_type)
    print(target_col)
    print(weight_col)
    print(type_of_problem)
    print(path)
    print(output_save_name)
    print(save_name)

    is_classification = True if type_of_problem=='classification' else False

    print(is_classification)
    add_cell_to_notebook(nb, make_new_cell(get_libraries()))
    add_cell_to_notebook(nb,make_new_cell(get_constants()))
    add_cell_to_notebook(nb,make_new_cell(get_col_datatype_util()))

    #Change the below function. Make it via code

    add_cell_to_notebook(nb,make_new_cell(get_col_datatype(col_with_type)))
    add_cell_to_notebook(nb,make_new_cell(get_col_default()))

    add_cell_to_notebook(nb,make_new_markdown_cell("## Read DataFrame"))
    if is_classification:
        add_cell_to_notebook(nb, make_new_cell(read_data_frame(path)))
    else:
        add_cell_to_notebook(nb, make_new_cell(read_data_frame_regression(path)))

    add_cell_to_notebook(nb,make_new_markdown_cell("## Global Constants"))
    add_cell_to_notebook(nb,make_new_cell(target_and_weight_const(target_col,weight_col)))

    if is_classification:
        add_cell_to_notebook(nb, make_new_cell(global_constants_categorical()))
    else:
        add_cell_to_notebook(nb,make_new_cell(global_constants_numerical()))

    #Integrate this cell with code
    add_cell_to_notebook(nb,make_new_cell(check_weight_col()))

    if not is_classification:
        add_cell_to_notebook(nb,make_new_cell("""df['http_referer'].replace(to_replace="http://",inplace=True)"""))

    add_cell_to_notebook(nb,make_new_cell(get_features()))
    add_cell_to_notebook(nb,make_new_cell(get_needful_functions()))
    add_cell_to_notebook(nb,make_new_cell(unique_count()))

    add_cell_to_notebook(nb,make_new_markdown_cell("## Unique Count DataFrame"))
    add_cell_to_notebook(nb,make_new_cell(make_unique_df()))
    add_cell_to_notebook(nb,make_new_cell(make_group()))
    add_cell_to_notebook(nb,make_new_cell(do_miscing()))
    add_cell_to_notebook(nb,make_new_cell(is_feature_irrelevant()))
    add_cell_to_notebook(nb,make_new_cell(get_irrelevant_features()))
    add_cell_to_notebook(nb,make_new_cell(remove_irrelevant_features()))

    add_cell_to_notebook(nb,make_new_markdown_cell("## Remove Irrelevant Features"))
    add_cell_to_notebook(nb,make_new_cell(remove_irrelevant_features_from_df()))
    add_cell_to_notebook(nb,make_new_cell(make_misced_df()))

    add_cell_to_notebook(nb,make_new_markdown_cell("## Misced DataFrame"))
    add_cell_to_notebook(nb,make_new_cell(misced_df()))

    #Plotting Functions
    add_cell_to_notebook(nb,make_new_cell(get_bar_trace()))
    #Missing Plot
    add_cell_to_notebook(nb,make_new_cell(plot_bar_chart()))
    add_cell_to_notebook(nb,make_new_cell(calculate_missing_count()))
    add_cell_to_notebook(nb,make_new_cell(missing_values_plot()))
    add_cell_to_notebook(nb,make_new_markdown_cell("## Missing Count and Ratio"))
    add_cell_to_notebook(nb,make_new_cell(do_missing_values_plot()))

    #Weight Plot
    add_cell_to_notebook(nb,make_new_markdown_cell("## Plotting Functions"))
    add_cell_to_notebook(nb,make_new_cell(set_plt_params()))
    add_cell_to_notebook(nb,make_new_cell(plot_pie_chart()))
    add_cell_to_notebook(nb,make_new_cell(pie_chart()))
    add_cell_to_notebook(nb,make_new_cell(get_value()))
    add_cell_to_notebook(nb,make_new_cell(append_first_and_third_quartile()))
    add_cell_to_notebook(nb,make_new_cell(quartiles()))
    add_cell_to_notebook(nb,make_new_cell(remove_outliers()))
    add_cell_to_notebook(nb,make_new_cell(hist_plot()))
    add_cell_to_notebook(nb,make_new_cell(weight_plot()))

    #Bar Plot(only for classification)
    if is_classification:
        add_cell_to_notebook(nb,make_new_cell(group_bar_chart()))
        add_cell_to_notebook(nb,make_new_cell(get_topk_feature_val()))
        add_cell_to_notebook(nb,make_new_cell(bar_plot()))
        add_cell_to_notebook(nb,make_new_cell(hist_plot_target()))
        add_cell_to_notebook(nb,make_new_cell(weight_plot_target()))


    #Average Values(only for classification)
    if is_classification:
        add_cell_to_notebook(nb, make_new_cell(get_avg_values()))
        add_cell_to_notebook(nb, make_new_cell(avg_val_bar_plot()))
        #Check dist plot
        add_cell_to_notebook(nb, make_new_cell(dist_plot()))
        add_cell_to_notebook(nb, make_new_cell(average_value_plot()))
    else:
        add_cell_to_notebook(nb,make_new_cell(get_avg_values_regression()))
        add_cell_to_notebook(nb,make_new_cell(get_topk_feature_val_regression()))
        add_cell_to_notebook(nb,make_new_cell(avg_val_bar_plot_regression()))
        add_cell_to_notebook(nb,make_new_cell(dist_plot_regression()))
        add_cell_to_notebook(nb, make_new_cell(average_value_plot_regression()))

    if not is_classification:
        add_cell_to_notebook(nb,make_new_cell(set_sns_params()))
        add_cell_to_notebook(nb,make_new_cell(scatter_plot_util()))
        add_cell_to_notebook(nb,make_new_cell(scatter_plot()))

    add_cell_to_notebook(nb,make_new_cell(box_plot_util()))
    add_cell_to_notebook(nb,make_new_cell(box_plot()))

    #Data Preprocessing(only for classification)
    add_cell_to_notebook(nb,make_new_markdown_cell("## Mean Encoding"))
    if is_classification:
        add_cell_to_notebook(nb,make_new_cell(categorical_to_numerical_TBS()))
        add_cell_to_notebook(nb,make_new_cell(calculate_prior()))
        add_cell_to_notebook(nb,make_new_cell(make_numerical_df()))
        add_cell_to_notebook(nb,make_new_cell(numerical_df_without_na()))

        add_cell_to_notebook(nb,make_new_markdown_cell("## Weight of Evidence Encoding"))
        add_cell_to_notebook(nb,make_new_cell(categorical_to_numerical_WOE()))
        add_cell_to_notebook(nb,make_new_cell(calculate_prior_WOE()))
        add_cell_to_notebook(nb,make_new_cell(make_woe_df()))

        add_cell_to_notebook(nb,make_new_markdown_cell("## Weight of Evidence DataFrame"))
        add_cell_to_notebook(nb,make_new_cell(woe_df()))
    else:
        add_cell_to_notebook(nb, make_new_cell(categorical_to_numerical_TBS_regression()))
        add_cell_to_notebook(nb, make_new_cell(calculate_prior_regression()))
        add_cell_to_notebook(nb, make_new_cell(make_numerical_df_regression()))
        add_cell_to_notebook(nb, make_new_cell(numerical_df_without_na_regression()))

    #Regression Model
    if is_classification:
        add_cell_to_notebook(nb,make_new_markdown_cell("## Logistic Regression"))
        add_cell_to_notebook(nb,make_new_cell(import_regression_libraries()))
    else:
        add_cell_to_notebook(nb,make_new_markdown_cell("## Linear Regression"))
        add_cell_to_notebook(nb,make_new_cell(import_regression_libraries_regression()))

    add_cell_to_notebook(nb, make_new_cell(weighted_mean()))
    add_cell_to_notebook(nb, make_new_cell(weighted_std()))

    if is_classification:
        add_cell_to_notebook(nb, make_new_cell(get_coeff_df()))
        add_cell_to_notebook(nb, make_new_cell(fit_logistic_regression_model()))
        add_cell_to_notebook(nb, make_new_cell(make_logisitic_model()))
        add_cell_to_notebook(nb, make_new_markdown_cell("## Coefficient DataFrame"))
        add_cell_to_notebook(nb, make_new_cell(display_logistic_coeff()))

        add_cell_to_notebook(nb,make_new_cell(fit_logistic_regression_model_woe()))
        add_cell_to_notebook(nb, make_new_cell(make_logisitic_model_woe()))
        add_cell_to_notebook(nb, make_new_markdown_cell("## Coefficient DataFrame(Using WOE Encoded Data)"))
        add_cell_to_notebook(nb, make_new_cell(display_logistic_coeff_woe()))

        # add_cell_to_notebook(nb,make_new_cell(stepwise_addition_logistic_regression()))
        # add_cell_to_notebook(nb,make_new_cell(logloss_df_stepwise_addition()))
    else:
        add_cell_to_notebook(nb,make_new_cell(get_coeff_df_regression()))
        add_cell_to_notebook(nb, make_new_cell(fit_linear_regression_model()))
        add_cell_to_notebook(nb, make_new_cell(make_linear_model()))
        add_cell_to_notebook(nb, make_new_markdown_cell("## Coefficient DataFrame"))
        add_cell_to_notebook(nb, make_new_cell(display_logistic_coeff()))

        # add_cell_to_notebook(nb,make_new_cell(stepwise_addition_linear_regression()))
        # add_cell_to_notebook(nb,make_new_cell(r2_df_stepwise_addition()))

    add_cell_to_notebook(nb, make_new_markdown_cell("## XGBoost Implementation"))
    #XgBoost Plots
    if is_classification:
        add_cell_to_notebook(nb,make_new_cell(import_xgboost_libraries()))
    else:
        add_cell_to_notebook(nb,make_new_cell(import_xgboost_libraries_regression()))

    #Common for both
    add_cell_to_notebook(nb,make_new_cell(plot_importance()))
    add_cell_to_notebook(nb,make_new_cell(plot_and_save_boosted_trees()))
    add_cell_to_notebook(nb,make_new_cell(get_important_features()))


    #Running XgBoost Model(only for classification)
    if is_classification:
        add_cell_to_notebook(nb,make_new_cell(fit_xgboost_model()))
        add_cell_to_notebook(nb,make_new_cell(make_numerical_df_na()))
    else:
        add_cell_to_notebook(nb,make_new_cell(fit_xgboost_model_regression()))
        add_cell_to_notebook(nb,make_new_cell(make_numerical_df_na_regression()))

    add_cell_to_notebook(nb,make_new_cell(make_xgboost_model()))

    add_cell_to_notebook(nb, make_new_markdown_cell("## Feature Importance(XGBoost)"))
    add_cell_to_notebook(nb,make_new_cell(plotting_importance()))

    # add_cell_to_notebook(nb, make_new_markdown_cell("## Trained Trees"))
    # add_cell_to_notebook(nb,make_new_cell(plotting_trees()))

    #LightGBM Implementation
    add_cell_to_notebook(nb, make_new_markdown_cell("## LightGBM Implementation"))
    add_cell_to_notebook(nb, make_new_cell(get_lightgbm_libraries()))
    add_cell_to_notebook(nb, make_new_cell(label_encode_data()))
    add_cell_to_notebook(nb, make_new_cell(get_label_data_and_encoders()))

    add_cell_to_notebook(nb, make_new_cell(plot_feature_importance_lightgbm()))
    add_cell_to_notebook(nb, make_new_cell(get_important_features_lightgbm()))

    if is_classification:
        add_cell_to_notebook(nb,make_new_cell(fit_lightgbm_model()))
    else:
        add_cell_to_notebook(nb, make_new_cell(fit_lightgbm_model_regression()))

    add_cell_to_notebook(nb, make_new_cell(make_lightgbm_model()))

    add_cell_to_notebook(nb, make_new_markdown_cell("## Feature Importance LightGBM"))
    add_cell_to_notebook(nb, make_new_cell(plotting_importance_lightgbm()))

    add_cell_to_notebook(nb, make_new_markdown_cell("## Rank Mean"))
    add_cell_to_notebook(nb, make_new_cell(rank_mean_util()))
    add_cell_to_notebook(nb,make_new_cell(rank_mean()))
    if is_classification:
        add_cell_to_notebook(nb, make_new_cell(get_ret_list()))
    else:
        add_cell_to_notebook(nb, make_new_cell(get_ret_list_regression()))

    add_cell_to_notebook(nb, make_new_cell(add_to_list()))
    add_cell_to_notebook(nb, make_new_cell("ret_list = ret_list[:5]"))

    add_cell_to_notebook(nb, make_new_markdown_cell("## Weight Plot"))
    add_cell_to_notebook(nb, make_new_cell(plot_weightplot()))

    if is_classification:
        add_cell_to_notebook(nb, make_new_markdown_cell("## Weight Plot(Target Based)"))
        add_cell_to_notebook(nb, make_new_cell(plot_weightplot_target_based()))

    add_cell_to_notebook(nb, make_new_markdown_cell("## Average Values Plot(Average Target)"))
    if is_classification:
        add_cell_to_notebook(nb, make_new_cell(plot_average_value_plot()))
    else:
        add_cell_to_notebook(nb, make_new_cell(plot_average_value_plot_regression()))

    if not is_classification:
        add_cell_to_notebook(nb, make_new_markdown_cell("## Box Plot"))
        add_cell_to_notebook(nb,make_new_cell(plot_boxplot_regression()))

        add_cell_to_notebook(nb, make_new_markdown_cell("## Scatter Plot"))
        add_cell_to_notebook(nb, make_new_cell(plot_scatterplot_regression()))

    add_cell_to_notebook(nb, make_new_markdown_cell("## Conditional Feature Importance(Next Candidate Feature)"))

    #Conditional Feature Importance
    if is_classification:
        add_cell_to_notebook(nb,make_new_cell(conditional_feature_importance_util()))
        add_cell_to_notebook(nb,make_new_cell(conditional_feature_importance()))
        add_cell_to_notebook(nb,make_new_cell(get_conditional_feature_importance()))

        add_cell_to_notebook(nb ,make_new_markdown_cell("## Loss Reduction on addition of each feature"))
        add_cell_to_notebook(nb, make_new_cell("""logloss_logistic = logloss_logistic.sort_values(by='Logloss Reduction',ascending=False)
logloss_logistic"""))
        add_cell_to_notebook(nb, make_new_cell("""logloss_xgboost = logloss_xgboost.sort_values(by='Logloss Reduction',ascending=False)
logloss_xgboost"""))
    else:
        add_cell_to_notebook(nb,make_new_cell(conditional_feature_importance_util_regression()))
        add_cell_to_notebook(nb,make_new_cell(conditional_feature_importance_regression()))
        add_cell_to_notebook(nb,make_new_cell(get_conditional_feature_importance_regression()))

        add_cell_to_notebook(nb ,make_new_markdown_cell("## R2 Increase on addition of each feature"))
        add_cell_to_notebook(nb, make_new_cell("""r2_linear = r2_linear.sort_values(by = "R2 Coeff",ascending=False)
r2_linear"""))
        add_cell_to_notebook(nb, make_new_cell("""r2_xgboost = r2_xgboost.sort_values(by = "R2 Coeff",ascending=False)
r2_xgboost"""))

    #Correlation
    add_cell_to_notebook(nb,make_new_cell(cramers_v()))
    add_cell_to_notebook(nb,make_new_cell(categorical_corr_df()))
    add_cell_to_notebook(nb,make_new_cell(categorical_corr()))
    add_cell_to_notebook(nb,make_new_cell(pearson_functions()))
    add_cell_to_notebook(nb,make_new_cell(numerical_corr_df()))
    add_cell_to_notebook(nb,make_new_cell(numerical_corr()))

    if is_classification:
        add_cell_to_notebook(nb,make_new_cell(corr_with_categorical_target()))
    else:
        add_cell_to_notebook(nb,make_new_cell(corr_with_numerical_target()))

    #Clustering
    add_cell_to_notebook(nb ,make_new_markdown_cell("## Clustering Feature Values having similar target behaviour"))

    add_cell_to_notebook(nb, make_new_cell(save_cluster()))
    if is_classification:
        add_cell_to_notebook(nb,make_new_cell(lightgbm_clustering()))
    else:
        add_cell_to_notebook(nb,make_new_cell(lightgbm_clustering_regression()))

    add_cell_to_notebook(nb,make_new_cell(make_cluster()))
    add_cell_to_notebook(nb,make_new_cell(display_cluster()))

    make_file(nb,save_name)

    print('Running notebook1')
    run_file(save_name,output_save_name)

if __name__=='__main__':
    main(sys.argv[1:])