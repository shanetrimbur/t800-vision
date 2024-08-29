# T800 Vision

Welcome to the T800 Vision project! This is an early-stage project inspired by the legendary Terminator T800's vision system. The goal is to build an advanced, low-footprint, real-time object detection system that brings the T800's capabilities to everyone. DISCLAIMER: THIS DOES NOT DETECT HUMMUS. WORKING ON THAT FEATURE AND WILL GET BACK TO YOU ASAP!

## Project Overview

Currently, the T800 Vision system is focused on detecting people using TensorFlow and OpenCV. The model is based on the SSD MobileNet V2 architecture, which is known for its balance between speed and accuracy, making it ideal for real-time applications. The project leverages models from the TensorFlow Model Zoo, specifically designed for TensorFlow 2.x, as outlined in [TensorFlow Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md).

### Features

- **Real-time Person Detection**: The system can detect people in a video stream with reasonable accuracy.
- **Bounding Box Visualization**: Detected people are highlighted with bounding boxes in the video feed.
- **Low Footprint**: The system is designed to be lightweight, making it suitable for use on devices with limited resources.

### Ideal for IoT and Edge Computing

The T800 Vision system is particularly well-suited for IoT (Internet of Things) and minimal edge computing setups. Its low compute and low resource requirements make it an excellent choice for DDIL (Disconnected, Intermittent, and Limited) environments, where processing power and connectivity may be constrained. This setup allows for real-time person detection and other vision-based tasks on devices like Raspberry Pi, Jetson Nano, and other low-power edge devices.

### Future Goals

While the current implementation focuses on detecting people, the vision is to expand this project into a full-fledged T800-style vision system capable of recognizing a wide range of objects, including everyday items and potential threats. Future updates will aim to include:

- **Advanced Object Detection**: Identify various objects such as vehicles, electronics, and more.
- **Gesture Recognition**: Recognize hand gestures for more interactive applications.
- **Edge Deployment**: Further optimize the model for deployment on edge devices like smartphones and Raspberry Pi.

## Installation

To get started with the T800 Vision system, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shanetrimbur/t800-vision.git
   cd t800-vision
