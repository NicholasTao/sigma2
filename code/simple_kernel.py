from function import get_training_data, calculate_daily_score

market_train_df, news_train_df = get_training_data()

my_model = train_my_model_daily(market_train_df, news_train_df) # # TODO:

predict_ys = my_predict() ## TODO:

daily_score_x = calculate_daily_score(predict_ys)
