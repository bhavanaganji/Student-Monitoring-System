# LIVE MONITORING OF STUDENT BEHAVIOUR DURING ONLINE CLASSES
This project presents a real-time, computer vision-based system to monitor student engagement during online classes. Using facial expression analysis, eye and mouth aspect ratios, and head pose estimation, the system detects key behavioural indicators such as drowsiness, yawning, and distraction. Educators receive a live dashboard showing these engagement metrics, enabling timely interventions and enhanced online learning effectiveness

Tech Stack:
Languages: Python, HTML/CSS (for web UI)
Libraries/Frameworks: OpenCV, dlib, Flask, NumPy
Facial Metrics: EAR (Eye Aspect Ratio), MAR (Mouth Aspect Ratio), Euler Angles for head pose
Frontend Interface: HTML, JS 
Backend: Flask (Python)

Features:
1.Real-time webcam capture and frame processing
2.Drowsiness detection using EAR
3.Yawning detection using MAR
4.Head pose estimation for attention tracking
5.Student-wise and class-wise engagement dashboard
6.Ethical, unobtrusive monitoring system

Student Browser (Client) ─► Flask Server ─► Behavioural Analysis Engine ─► Teacher Dashboard
           |                             |                           |
    Webcam Frame Capture     Frame Routing & Metadata     Real-time Metrics Display

Working:
Face Detection:
dlib detects student face from webcam input.

Facial Landmark Detection:
Extracts 68 facial landmarks using shape_predictor_68.

Metric Computation:
EAR: Used for detecting drowsiness.
MAR: Used to detect yawning.
Euler Angles: Determines head orientation and distraction.

Output:
Tuple of (EAR, MAR, Head Pose, Face Count) for each frame.

Dashboard:
Realtime chart display (line plots) of student engagement metrics.

Results:

Behaviour	                 Metric	                Threshold	                 Status

Drowsiness	              EAR < 0.25	               LOW	                   Drowsy
Yawning	                  MAR > 0.7	                 HIGH	                   Yawning
Distraction	              Yaw not in [-10°, +10°]	   SIDE	                   Distracted

Graphical output displays continuous engagement tracking.
