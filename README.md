# rascal-beta
RAS-Cal app for HTC-2022
RAS-Cal: The Health Pal

**Goal:**
Our goal is to make effective health monitoring accessible to all at an easy and pleasing way to improve the health of general masses and to monitor the 
status of our users to meet the UN sustainability goals while not compromising on ethics.

**Motivation**: Continuous health monitoring has been a topic of immense importance in the recent times (after the covid pandemic).
The world health statistics report also emphasizes the importance of health monitoring for the sustainable development goals.
Non-profit organizations around the world have played an immense role to extend health monitoring facilities for the people. 
Effective and affordable health monitoring applications have been undergoing changes through time with development of new hardware and software tools. 
A report suggests that there are over 50k apps for health care available, making it difficult for a user to choose the right app. 

**Application**:
In this product which we have named “RAS-Cal” we propose development of a single framework encompassing of multiple technologies allowing essential
information to be passed to the user and other health care officials with the goal to improve the overall health of general masses.
The idea revolves around collecting data through all possible sources, such as voice from users, though health monitoring devices, and various health apps 
installed in the users’ phone. The voice data collected is transformed to text via an API interface further the outputs are used by a web scrapping 
framework to extract important information to allow processing and give insights to the user. In this product, we will ensure that the data collected 
will be used in accordance with strict security and other privacy guidelines setup to eliminate any kind of violations or data breaches possible 
(e.g., following HIPAA Health Insurance Portability and Accountability Act guidelines) . 

This data is then processed at a two levels structure – (i) on the device (called edge intelligence technology) and (ii) cloud processing. 
The edge intelligence will allow for rapid-in-event decision making and in scenarios where cloud is not available (no internet facility). 
The cloud processing will be essential to provide data-driven insights via deep neural network-based architectures which involve extreme computations. 
This separation of computational power to the cloud will allow the app to be faster and occupy lower storage space. In this project for proof of concept,
we have used a freely available code from GitHub to show fuzzy logic based recommender system which will allow for rapid recommendations to the user, 
and can potentially serve as edge -intelligence. In usage in real world situation, the rule base of the fuzzy recommender system will have to be tuned 
by a health expert to allow accurate, reliable and in accordance to the health regulatory board (e.g., Health Canada and Food and Drug administration) 
based recommendations.
Design and aesthetics are part and parcel of any product. 
Therefore, we have used flask framework to integrate our python files in a web application. 
Further, we have deployed this in the Amazon web services (AWS) servers. To enable easy access of our services, as a first step we have developed an app in the MIT app inventor 
which allows the users to access our services at the tap of a button. This showcases the utility of our application. In future, we can extend it to android and macOS
environments to make it easy to access.

**Demo**
In the [demo video](https://www.youtube.com/watch?v=VSc8lBewxj4), we show a live recording of the calorie intake aspect of the application. While our accents have allowed us to accurately capture the word "Rajma",
we used prerecorded audio files for a native english speaker (main_demo.py) from [Cambridge dictionary](https://dictionary.cambridge.org/pronunciation/english) for "cinnamon bun". These files were
were provided as a .wav to the speech recognition platform.
