import pandas as pd


def load_data(path: str = './remote_work_productivity.csv') -> pd.DataFrame:
    """Load data from csv file and ensure scores are within valid range.

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

    data = pd.read_csv(path, index_col='Employee_ID', dtype=dtype_dict)

    data['Productivity_Score'] = data['Productivity_Score'].clip(
        lower=0, upper=100)
    data['Well_Being_Score'] = data['Well_Being_Score'].clip(
        lower=0, upper=100)

    return data
