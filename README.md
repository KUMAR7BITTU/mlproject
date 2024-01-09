### End to End machine learning project 

git push .
git commit -m "message"
git push -u origin main

python src/exception.py
python src/components/data_ingestion.py

python app.py
127.0.0.1:5000
http://127.0.0.1:5000/predictdata

Two setup we need to setup whenever we are working with elastic Beanstalk which is a kind of instance that will be provided to you where you can probably deploy your entire application . So, that extension is .EB extension so i have created it and inside this i have created one python config file . python config file is mainly to tell to the elastic binstalk instance saying that what is the entry point of your application . entry point of your application is the most important thing .

The default configuration in the elastic Beanstalk page documentation is :-
option_settings:
   "aws:elasticbeanstalk:container:python":
   WSGIPath:application:application


here app.py name is application , so we have given application 

create application.py file for deployment purpose .


To commit entire code:- git commit .