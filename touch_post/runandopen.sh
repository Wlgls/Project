python3 /home/wlgls/Data/Projects/touch_post/touch.py
cd /home/wlgls/Data/Blog/_posts
filename=`ls -l | tail -n 1 | awk '{print $9}'`
typora $filename

