from pandas import read_csv
from statistics import mean, stdev

def get_training_data():
    """
    use this function to get train data
    return two matrix(DataFrame): market_train_df, news_train_df
    """
    return _get_sample_data()

def _get_sample_data():
    market_train_df = read_csv("../sampledata/marketdata_sample.csv")
    news_train_df = read_csv("../sampledata/news_sample.csv")
    return market_train_df, news_train_df

def calculate_daily_score(predict_ys, profit_rs, universes):
    """
    only use to evaluate, cannot use to predict
    return todo
    """
    ## TODO:
    stock_num = len(predict_ys)
    assert stock_num == len(profit_rs) and stock_num == len(universes)
    daily_score_x = sum([predict_ys[i] * profit_rs[i] * universes[i] for i in xrange(stock_num)])
    return daily_score_x

def calculate_total_score(daily_score_xs):
    return mean(daily_score_xs) / stdev(daily_score_xs)
