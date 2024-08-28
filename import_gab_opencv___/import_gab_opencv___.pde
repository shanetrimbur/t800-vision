import gab.opencv.*;
import processing.video.*;
import java.util.ArrayList;
import java.awt.Rectangle; // Import Rectangle from java.awt

Capture video;
OpenCV opencv;
ArrayList<String> detectedItems = new ArrayList<String>();

void setup() {
  size(640, 480);
  video = new Capture(this, width, height);
  
  // Initialize OpenCV with the video feed
  opencv = new OpenCV(this, width, height);
  
  // Load a specific Haar cascade for hand detection
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE); // Example: Using a face detection cascade
  video.start();
}

void draw() {
  opencv.loadImage(video);

  // Detect items (e.g., faces in this example)
  Rectangle[] faces = opencv.detect(); // Detect objects and return bounding boxes

  // Display video feed
  image(video, 0, 0);

  // Draw bounding boxes around detected faces or hands
  for (int i = 0; i < faces.length; i++) {
    // Example: Draw a rectangle around each detected face or hand
    noFill();
    stroke(255, 0, 0);
    strokeWeight(2);
    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height);
    
    // Add to detected items list with metadata
    detectedItems.add("Detected Face at Position: (" + faces[i].x + ", " + faces[i].y + ")");
  }

  // Scroll and display detected gestures at the bottom
  fill(0);
  rect(0, height - 100, width, 100); // Background for text area
  fill(255);
  textSize(12);
  int y = height - 80;
  for (int i = max(0, detectedItems.size() - 5); i < detectedItems.size(); i++) {
    text(detectedItems.get(i), 10, y);
    y += 20;
  }
}

void captureEvent(Capture video) {
  video.read();
}
