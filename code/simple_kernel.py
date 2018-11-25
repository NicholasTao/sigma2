from function import get_training_data

market_train_df, news_train_df = get_training_data()
print(type(market_train_df))


# train_my_model(market_train_df, news_train_df)
#
# for (market_obs_df, news_obs_df, predictions_template_df) in env.get_prediction_days():
#   predictions_df = make_my_predictions(market_obs_df, news_obs_df, predictions_template_df)
#   env.predict(predictions_df)
#
# env.write_submission_file()
