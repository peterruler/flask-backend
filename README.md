# Flask Backend

# Prerequisites
- install tensorflow on your specific system (pc, linux or macos arch x64 or arch arm is different), install miniconda, please check jeff heaton YouTube and GitHub pages.
- https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-jul-2020.ipynb

# Blueprint as a start on Webpage 
- https://narainsreehith.medium.com/upload-image-video-to-flask-backend-from-react-native-app-expo-app-1aac5653d344

# Install needed pip packages
- conda activate tensorflow
- conda install -y flask && conda install -y flask-cors 

# start for development
```
  conda activate tensorflow && python app.py
```
# stop development server
`CTRL + C`

# start in background 'for production'
```
conda activate tensorflow &&
nohup python app.py > my.log 2>&1 &
echo $! > save_pid.txt
```
# stop server 'for production'
```
ps -ef | grep python # get pid of app.py process
kill -9 `cat save_pid.txt`
rm save_pid.txt
```
# Demo
- call http://keepitnative.xyz:4000/ hello world endpoint
- Download and use Postman, choose type: POST on address: http://keepitnative.xyz:4000/image
using contents of file: payload.base64img.txt as body content
