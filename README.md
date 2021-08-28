# templerun2
I used a supervised learning technique to train an A.I. to play Temple run. My best try was a 1700m run with a 89% accurate model.

Worfklow:
1.) Move window to standardized area with put_window_at_place.py
2.) If not certain: check if window is covered properly with test_imagedetection.py
3.) Gather trainingdata with gather_training_data.py
4.) Check size of the gathered data with check_database_dimensions
5.) After each game: add data to the maindatabase, but leave the last few datapoints out, which captured your death.
6.) If datacaptioning runs at a frequency of more than 20Hz, add extra fake-actions to dataset for better trainingresults with double_actions.py
7.) Further increase the percentage of actions in the dataset with reduce_no_actions.py for better trainingresults.
8.) train model with train_color.py
9.) let the model play with model_plays.py
