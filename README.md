


1. What it does?
- The project detects Distributed Denial of Service (DDoS) attacks in real-time using machine learning. It classifies network traffic as either malicious (DDoS) or benign by analyzing features from the traffic dataset. This allows the system to block harmful requests early and maintain the availability of services even during high-volume attacks.

2. How we built the project?
- The project uses the ACK/PUSH-ACK DDoS dataset with approximately 0.5 million records. Data preprocessing involved noise filtering, handling missing values, and transforming the 3-class problem (DDoS-PSH-ACK, DDoS-ACK, Benign) into a 2-class problem (DDoS vs. Benign). Principal Component Analysis (PCA) reduced the number of features from 27 to 9.
- For detection, we employed Apache Flink to handle large-scale data processing in real-time and used the Gradient Boosting algorithm for classification. The project was developed with pyflink to create a Flink execution and table environment, and GradientBoostingClassifier (from sklearn) to train the model.
- The system has a frontend interface for initiating and visualizing DDoS attacks, and the attacker machines communicate with the central system via a REST API and port forwarding.

3. Challenges we ran into while building the project?
- One of the challenges was ensuring real-time detection while maintaining high accuracy on large datasets.
Handling the preprocessing of the dataset (noise, missing values, transforming multi-class to binary classification) required careful consideration to avoid information loss.
- Optimizing the machine learning model for better performance without overfitting, particularly tuning the Gradient Boosting parameters, was challenging.
- Efficiently managing communication between attacker machines and the central prediction system also posed challenges.

4. Accomplishments that we're proud of while working on this project?
- Achieving a high model accuracy of 99.41% using the Gradient Boosting algorithm with a big data approach.
- The system’s ability to detect DDoS attacks in real-time, with detection occurring within milliseconds.
- Successfully reducing the dimensionality of the dataset with PCA while maintaining model performance.
- Developing a REST API to initiate attacks and predict outcomes efficiently, integrated with a live web application for visualization.

5. What we learned while working on this project?
- We gained deep insights into real-time machine learning and big data processing with Apache Flink.
- The importance of feature selection and preprocessing in achieving high model performance.
- We learned how to tune machine learning models for optimal performance and prevent overfitting using techniques like gradient boosting.
- Experience in setting up real-time attack simulation environments with REST APIs and integrating ngrok for port forwarding.

6. What's next for project development process?
- The next step is to explore deep learning models, such as convolutional neural networks (CNNs), to further improve detection accuracy and efficiency.
- We plan to test the model with even larger datasets and improve the scalability of the system.
- Enhancing the real-time component and automating the response to detected attacks would make the system more robust and reactive under real-world conditions.

### Run streamlit using the following command.
streamlit run ./dashboard.py --server.port 6879 