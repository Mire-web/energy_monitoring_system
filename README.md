# Energy Monitoring System

![Project Logo](https://via.placeholder.com/150) <!-- Replace with actual logo if available -->

The Energy Monitoring System is a full-stack application designed to monitor and manage energy consumption in real-time. It consists of a backend server built with Node.js and Express, and a frontend interface developed using React.js. The system provides users with insights into their energy usage, helping them make informed decisions to optimize consumption.

## Features

- **Real-time Energy Monitoring**: Track energy usage in real-time with interactive charts and graphs.
- **User Authentication**: Secure login and registration system for users.
- **Device Management**: Add, remove, and manage energy-consuming devices.
- **Data Visualization**: Interactive dashboards with charts and historical data analysis.
- **Alerts and Notifications**: Set up alerts for unusual energy consumption patterns.
- **API Integration**: RESTful API for seamless integration with other systems.

## Technologies Used

### Backend
- **Node.js**: JavaScript runtime for building the server.
- **Express.js**: Web application framework for Node.js.
- **MongoDB**: NoSQL database for storing energy data and user information.
- **Socket.IO**: Real-time bidirectional communication for live updates.
- **JWT**: JSON Web Tokens for secure user authentication.

### Frontend
- **React.js**: JavaScript library for building user interfaces.
- **Redux**: State management library for React.
- **Chart.js**: For rendering interactive charts and graphs.
- **Axios**: HTTP client for making API requests.
- **Material-UI**: React components for faster and easier web development.

### DevOps
- **Docker**: Containerization for consistent development and deployment.
- **GitHub Actions**: CI/CD pipeline for automated testing and deployment.
- **Nginx**: Reverse proxy server for serving the frontend and backend.

## Installation

### Prerequisites
- Node.js (v14 or higher)
- MongoDB (v4.4 or higher)
- Docker (optional)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mire-web/energy_monitoring_system.git
   cd energy_monitoring_system

2. **Install Dependencies**
# Backend
cd backend
npm install

# Frontend
cd ../frontend/energy_monitor
npm install

3. **Set Up Environment Variables**
   Create a .env file in the backend directory:
   ```
   MONGO_URI=mongodb://localhost:27017/energy_monitoring
   JWT_SECRET=your_jwt_secret
   PORT=5000
   ```
   Create a .env file in the frontend directory:
   ```
   REACT_APP_API_URL=http://localhost:5000
   ```
4. **Run the Backend Server**
   ```npm start```
5. **Run the Frontend Development Server**
   ```
   cd frontend/energy_monitor
   npm start
6. **Access the Application**
   Open your browser and navigate to http://localhost:3000
