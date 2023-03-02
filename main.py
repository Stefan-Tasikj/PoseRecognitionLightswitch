import cv2
import mediapipe as mp
import poses as check
import LED_Control as LED

parts = {}
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
detectedpose = False
change = False
# Create camera feed and store landmarks to a dictionary
cap = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        change = detectedpose
        # Set image to RGB for MediaPipe
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)
        # Set back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        try:
            # Write the relevant vertices to a dictionary
            landmarks = results.pose_landmarks.landmark
            parts['Lshoulder'] = [landmarks[11].x, landmarks[11].y]
            parts['Rshoulder'] = [landmarks[12].x, landmarks[12].y]
            parts['Lelbow'] = [landmarks[13].x, landmarks[13].y]
            parts['Relbow'] = [landmarks[14].x, landmarks[14].y]
            parts['Lwrist'] = [landmarks[15].x, landmarks[15].y]
            parts['Rwrist'] = [landmarks[16].x, landmarks[16].y]
            # checks if the vertices match a pose
            detectedpose = check.matches_pose(parts)
        except:
            print("Landmarks not detected")
        # Draw the vertices on top of the video feed
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(25, 17, 112), thickness=3, circle_radius=5),
                                  mp_drawing.DrawingSpec(color=(81, 250, 209), thickness=2))
        print(parts)
        # Label on top of the video feed that displays if a pose is detected or not
        cv2.putText(frame, str(detectedpose), (10, 400), cv2.FONT_HERSHEY_PLAIN, 4, (0, 50, 250), 3)
        # Only call the LED switch function if the detectedpose value changes, instead of looping the call repeatedly
        if not detectedpose == change:
            if detectedpose:
                LED.gestureTrue()
            else:
                LED.gestureFalse()
        cv2.imshow('Video Feed with Landmark overlays', frame)
        #quits the videofeed if q is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
