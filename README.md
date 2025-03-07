# Flask Backend (Python Rest Server)

## Prerequisites
1. Install TensorFlow on your specific system (PC, Linux, or macOS, arch x64 or arch ARM is different). Install Miniconda. Please check Jeff Heaton's YouTube and GitHub pages for detailed instructions:
   - Download and install Miniconda from the website: [Download Miniconda](https://docs.anaconda.com/miniconda/)
   - [TensorFlow Installation Guide](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-jul-2020.ipynb)

2. Use the following blueprint as a start for your webpage:
   - [Upload Image/Video to Flask Backend from React Native App](https://narainsreehith.medium.com/upload-image-video-to-flask-backend-from-react-native-app-expo-app-1aac5653d344)

## Installation
1. Activate the TensorFlow environment:
   ```sh
   conda activate tensorflow
   ```

2. Install needed pip packages:
   ```sh
   conda install -y flask && conda install -y flask-cors
   ```

## Start for development
```sh
conda activate tensorflow && python app.py
```

## Stop development server
`CTRL + C`

## Start in background 'for production'
```sh
conda activate tensorflow &&
nohup python app.py > my.log 2>&1 &
echo $! > save_pid.txt
```

## Stop server 'for production'
```sh
ps -ef | grep python # get pid of app.py process
kill -9 `cat save_pid.txt`
rm save_pid.txt
```

## Demo
- The Flask-Backend is no longer online on: [http://keepitnative.xyz:4000](http://keepitnative.xyz:4000)
- Please run the server locally instead
- Download and use Postman, choose type: POST on address: http://localhost:4000/image
using contents of file: payload.base64img.txt as body content
