# Flask Backend

- install tensorflow on your desired system, install miniconda, please see:
- https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-jul-2020.ipynb

# Tutorial
- https://narainsreehith.medium.com/upload-image-video-to-flask-backend-from-react-native-app-expo-app-1aac5653d344

- start:
```
  conda activate tensorflow && python app.py
```
- run forever:
```
conda activate tensorflow &&
nohup python app.py > my.log 2>&1 &
echo $! > save_pid.txt
```
```
ps -ef | grep python # get pid of app.py process
kill -9 `cat save_pid.txt`
rm save_pid.txt
```
- Call server:
- http://keepitnative.xyz:4000/
- Postman, POST on: http://keepitnative.xyz:4000/image

