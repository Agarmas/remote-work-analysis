import pandas as pd


def load_data(path: str = './remote_work_productivity.csv') -> pd.DataFrame:
    """Load data from csv file.

    Args:
        path (str, optional): Path to file. Defaults to './remote_work_productivity.csv'.

    Returns:
        pd.DataFrame: Data.
    """
    dtype_dict = {
        'Employee_ID': 'int64',
        'Employment_Type': 'category',
        'Hours_Worked_Per_Week': 'int64',
        'Productivity_Score': 'int64',
        'Well_Being_Score': 'int64'
    }

    return pd.read_csv('./remote_work_productivity.csv', index_col='Employee_ID', dtype=dtype_dict)
