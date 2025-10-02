A simple project to analyse ONS vacancy data.

<b> Visualisation </b>

Revisions for individual months seem significant. The ultimate value is generally lower than the initial values.

<b> Forecasting </b> 

I have attempted to create a projection using only the vacancies series itself. I assume from the definition of the exercise that this is appropriate. Were you to want a proper forecast of vacancies, I suspect you would want to use a macroeconomic model rather than time-series methods. Knowledge of forward interest rates, for example, would probably tell you more than applying auto-regression methods to the time series.

I have done a simple SARIMA method with seasonality of 12 months. The supposition was that there might be some calendar-year seasonality. I think this effect might be real, but it does not seem massively significant.

I just used the most recent release of the timeseries to train the model. Given the estimates for different vintage timeseries are heavily correlated, they could not be used as independent training data. One potential avenue for progressing the analysis (see below) would be to find some way of accounting for likelihood of revision in the model. 

I have not had time to do any hyperparameter selection, or to compare the effectiveness of different models. 

To progress the analysis, I would want to compare the performance of different hyperparameter values for this model type, and for other candidate models. Model performance could be assessed on the back-series by holding out periods of known data (for example, training on everything up to 2016 and then predicting 2017 onwards). Averaging performance over a range of different hold-outs would give you an indication of which models / hyperparameters are performing best. A range of loss metrics could be used, but I imagine a simple squared-error loss metric would be a good place to start.

There is minimal consideration in the model of the impact of likely revisions. The scale of revisions would impact attempts to validate the model using newly-published data (although that shouldn't really be the sole method of validation). Revisions may also effect model training. For example, if early estimates are systematically revised down, then the most recent four or five points in the timeseries for the most recent data release may be higher than their true, long-term value. That impact may be effecting the training. Addressing this would progress the analysis. One way to do it would be to train only on mature data (i.e., data for a month more than 12 months ago), but you do lose something in doing this. An alternative would be to introduce exogenous variables for the "age" of these different predictions that would proxy their likelihood of revision. There are trade-offs though, and with a dataset of this size you wouldn't want to introduce too much complexity and end up overfitting.  

Really, the best way to improve the analysis would be to introduce some other data series that may be leading indicators of vacancy levels. The truest way of doing this would be to do this with a macroeconomic model, drawing on known mechanisms. Failing that, a set of paired timeseries methods would likely be an improvement on this simple autoregression. 

