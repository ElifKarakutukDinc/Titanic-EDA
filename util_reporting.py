import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def df_first_look(df):
    """
    This function gets a Python Pandas dataframe and visualize basic information about the dataframe.
    :param df: Dataframe to be analyze
    :return: This function doesn't return anything.
    """
    try:
        print("First 5 rows of dataframe:\n--------------------------\n", df.head())
        print("")
        print("Last 5 rows of dataframe:\n--------------------------\n", df.tail())
        print("")
        print(
            "Row count of dataframe:\n-----------------------\n",
            df.shape[0],
            "\nColumn count of dataframe:\n--------------------------\n",
            df.shape[1],
        )
        print("")
        print(
            "List of columns in the dataframe:\n---------------------------------\n",
            df.columns.values,
        )
        print("")
        print(
            "Looking NaN values and datatypes of columns in the dataframe:\n--------------------------------------------\n"
        )
        print(df.info())
        print("")

    except Exception as e:
        print("Error at df_first_look function: ", str(e))


def df_descriptive_statistics(df, column_list):
    """
    This function gets a Python Pandas dataframe and list of columns to visualize descriptive statistics about those columns.
    :param df: Dataframe to be analyze
    :param column_list: List of columns to filter out only numeric columns to use in the fuction"
    :return: This function doesn't return anything.

    """
    try:
        dummy_df = df[column_list].copy()
        print(
            f"Descriptive Statisctics for column:\n--------------------------\n",
            dummy_df.describe(),
        )
        print("")
        print(f"Mode values for column:\n--------------------------\n", dummy_df.mode())
        print("")
    except Exception as e:
        print("Error at df_descriptive_statistics function: ", str(e))


def df_pivot_aggregated_statistics(
    df, column_list, to_be_calculated_column, descriptive_statistic_list
):
    """
    This function gets a Python Pandas dataframe and calculating aggregation by columns in the dataframe.
    :param df: Dataframe to be analyze
    :param column1: For showing values by this column in group.
    :param column2: For showing values by this column in group.
    :param column3: For showing values by this column in group.
    :param cal_column: Calculation aggregation for this column.
    :param descriptive_statistic: It shows which we use descriptive statistic(Mean,Median,Standard dev,Min,etc.)
    :return: This function doesn't return anything.

    """
    df_dummy = (
        df.groupby(column_list)[to_be_calculated_column]
        .agg(descriptive_statistic_list)
        .round(2)
    )
    print(df_dummy)


def countplot_viz(
    data,
    xcolumn,
    xlabel,
    ylabel,
    title,
    hue=None,
    fontsize_label=16,
    fontsize_title=20,
    rotation=45,
    palette="mako",
):
    """
    This function gets a Python Pandas dataframe and visualize a countplot.
    :param data: Dataframe to be analyze
    :param xcolumn: This column shows x axis column.
    :param xlabel: It shows name of x axis column.
    :param ylabel: It shows name of y axis column.
    :param title: This column shows name of graph.
    :return: This function doesn't return anything.

    """
    plt.figure(figsize=(12, 5))

    sns.countplot(x=xcolumn, data=data, hue=hue, palette=palette)
    plt.xlabel(xlabel, fontsize=fontsize_label)  # seting the xtitle and size
    plt.ylabel(ylabel, fontsize=fontsize_label)  # Seting the ytitle and size
    plt.title(title, fontsize=fontsize_title)
    plt.xticks(rotation=rotation)
    plt.show()


def multiple_plot_viz(
    data,
    column_for_separate,
    column_for_calculate,
    title_1,
    title_2,
    edgecolor="black",
    color_1="orange",
    color_2="blue",
):
    """
    This function gets a Python Pandas dataframe and visualize two countplots.
    :param data: Dataframe to be analyze
    :param xcolumn: This column shows x axis column.
    :param xlabel: It shows name of x axis column.
    :param ylabel: It shows name of y axis column.
    :param title_1 and title_2: These columns show name of graphs.
    :return: This function doesn't return anything.

    """
    f, ax = plt.subplots(1, 2, figsize=(15, 5))

    data[data[column_for_separate] == 0][column_for_calculate].plot.hist(
        ax=ax[0], bins=20, edgecolor=edgecolor, color=color_1
    )
    ax[0].set_title(title_1)
    x1 = list(range(0, 85, 5))
    ax[0].set_xticks(x1)

    data[data[column_for_separate] == 1][column_for_calculate].plot.hist(
        ax=ax[1], bins=20, edgecolor=edgecolor, color=color_2
    )
    ax[1].set_title(title_2)
    x2 = list(range(0, 85, 5))
    ax[1].set_xticks(x2)


def crosstab_viz(data, index_column_1, index_column_2, aggregated_column, cmap="mako"):
    """
    This function gets a Python Pandas dataframe and visualize a crosstab.
    :param data: Dataframe to be analyze
    :param index_column_1: This column works as a stpliter of pivot.
    :param index_column_2: This column works as a stpliter of pivot.
    :param aggregated_column: Calculation aggregation for this column.
    :return: This function doesn't return anything.

    """
    return pd.crosstab(
        [data[index_column_1], data[index_column_2]],
        data[aggregated_column],
        margins=True,
    ).style.background_gradient(cmap=cmap)


def factor_plot_viz(
    data, index_column_1, index_column_2, aggregated_column, title_factor
):
    """
    This function gets a Python Pandas dataframe and visualize a factor plot.
    :param data: Dataframe to be analyze
    :param index_column_1: This column works as a stpliter of pivot.
    :param index_column_2: This column works as a stpliter of pivot.
    :param aggregated_column: Calculation aggregation for this column.
    :param title_factor: It shows name of graph.
    :return: This function doesn't return anything.

    """
    plt.figure(figsize=(12, 5))
    sns.factorplot(aggregated_column, index_column_2, hue=index_column_1, data=data)
    plt.title(title_factor)


def relationship_viz(
    data, index_column_1, index_column_2, aggregated_column, title_factor
):
    """
    This function gets a Python Pandas dataframe and concats two different graphs.
    :param data: Dataframe to be analyze
    :param index_column_1: This column works as a stpliter of pivot.
    :param index_column_2: This column works as a stpliter of pivot.
    :param aggregated_column: Calculation aggregation for this column.
    :param title_factor: It shows name of facot plot graph.
    :return: This function doesn't return anything.

    """
    factor_plot_viz(
        data, index_column_1, index_column_2, aggregated_column, title_factor
    )
    return crosstab_viz(data, index_column_1, index_column_2, aggregated_column)


def swarmplot_viz(
    df,
    xcolumn,
    ycolumn,
    groupped_column,
    xlabel,
    ylabel,
    title,
    fontsize=15,
    fontsize_title=17,
    palette="mako",
):
    """
    This function gets a Python Pandas dataframe and visualize two countplots.
    :param df: Dataframe to be analyze
    :param xcolumn: This column shows x axis column.
    :param ycolumn: This column shows y axis column.
    :param groupped_column: Calculation aggregation for this column.
    :param xlabel: It shows name of x axis column.
    :param ylabel: It shows name of y axis column.
    :param title_1 and title_2: These columns show name of graphs.
    :return: This function doesn't return anything.

    """
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 1, 2)

    sns.swarmplot(x=xcolumn, y=ycolumn, data=df, hue=groupped_column, palette=palette)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    plt.title(title, fontsize=fontsize_title)

    plt.subplots_adjust(hspace=0.5, top=0.9)
