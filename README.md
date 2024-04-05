# Flask Backend
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

