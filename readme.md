# 1.设备介绍

## 1.硬件信息：
设备网购地址：https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-16974999502.5.3ae035f9hQnm2x&id=590688396624

硬件结构信息：source/calib.io_checker_240x200_8x10_20.pdf

## 2.软件信息：

```shell
# 安装v4l
sudo apt-get install v4l-utils
# 通过v4l2查看设备
v4l2-ctl --list-devices
# 查看当前摄像头支持的视频压缩格式
v4l2-ctl -d /dev/video0 --list-formats

# cheese是Ubuntu自带摄像软件，中文名称茄子
sudo apt-get install cheese

# 可以查看初步视频流 支持录像和拍照  但有边框和两图合并
cheese /dev/video0
```



# 2.设备使用

## 2.1 数据流接入
### 方法一：[ROS](https://www.pudn.com/news/6257dbabbd8c6f2306dc20ae.html)

```shell
# 相机包
sudo apt-get install ros-melodic-usb-cam
# 标定包
sudo apt-get install ros-melodic-camera-calibration

# 启动相机
roslaunch usb_cam usb_cam-test.launc
# 启动标定
sudo apt-get install ros-melodic-camera-calibration
```

### 方法二：OpenCV
如  图像采集.py

## 2.2 图像标定
标定原理：https://www.bilibili.com/video/BV1Q34y1n7ot

双目标定基础：https://blog.csdn.net/sinat_16643223/article/details/115363497

使用Matlab双目标定工具箱进行标定：
https://blog.csdn.net/weixin_43956351/article/details/94394892






